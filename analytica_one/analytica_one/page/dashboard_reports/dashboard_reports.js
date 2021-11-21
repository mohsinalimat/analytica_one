frappe.pages['dashboard-reports'].on_page_load = (wrapper) => {
	// init page
	const page = frappe.ui.make_app_page({
		'parent': wrapper,
		'title': 'Dashboard Reports',
		'single_column': true,
	});

	page.add_inner_button(__("Generate Report"), function () {
		frappe.call({
			method: "analytica_one.analytica_one.doctype.metabase_settings.metabase_settings.set_wake",
			args: { "val": '1'}
			
		});
	});
	
	new DashboardReports(page, wrapper);
};

class DashboardReports {
	constructor(page, wrapper) {
		this.currentDashboard = false;
		this.page = page;
		this.wrapper = wrapper;
		this.pageMain = $(page.main);
		console.log(this.pageMain);
		this.pageAction = (
			$(this.wrapper)
				.find('div.page-head div.page-actions')
		);
		this.pageTitle = $(this.wrapper).find('div.title-text');
		console.log(this.pageTitle);
		this.init();
	}

	init() {
		this.createSelectionField();
	}

	showIframe() {
		console.log('called showif')
		this.getSettings().then(
			(r) => {
				// set variable
				console.log(r.message);
				this.settings = r.message;
				this.resizer = this.settings.resizer;
				this.iframeUrl = this.settings.iframeUrl;
				this.name = this.settings.name;
				console.log('inside showiframe')
				if (this.iframeUrl && this.resizer) {
					// prepare html
					const iFrameHtml = `
						<script id="resizer" src="${this.resizer}"></script>
						<iframe
							src="${this.iframeUrl}"
							frameborder="0"
							width=100%
							onload="iFrameResize({}, this)"
							allowtransparency
						></iframe>
					`;
					console.log(iFrameHtml);
					// append html to page
					this.iFrame = $(iFrameHtml).appendTo(this.pageMain);
					console.log(this.iFrame);
				}
			}
		);
	}

	getSettings() {
		console.log('INSIDE SETT '+this.dashboardName);
		return frappe.call({
			'method': 'analytica_one.analytica_one.doctype.dashboard_picker.pick.get_url',
			'args': {
				'dashboard': this.dashboardName,
			},
		});
	}

	createSelectionField() {
		// create dashboard selection field
		this.selectionField = frappe.ui.form.make_control({
			'parent': this.pageAction,
			'df': {
				'fieldname': 'Report',
				'fieldtype': 'Link',
				'options': 'Dashboard Picker',
				'onchange': () => {
					const dashboardName = this.selectionField.get_value();
					// console.log('DASHBO '+dashboardName);
					if (dashboardName) {
						frappe.show_alert({
							message:__('Loading ' +dashboardName+ '... Please wait!'),
							indicator:'green'
						    }, 10);
						this.dashboardName = dashboardName;
						if (this.currentDashboard != this.dashboardName) {
							console.log('inside if');
							// clear page html
							this.pageMain.empty();

							this.showIframe();
							console.log('frame '+this.showIframe);
							this.changeTitle();
							console.log('title '+this.changeTitle);

							// set current dashboard
							this.currentDashboard = this.dashboardName;
							console.log('test '+this.currentDashboard);
						}
						// clear input
						this.selectionField.set_input('');
					}
				},
				'get_query': () => {
					return {
						'filters': {
							'is_active': 1,
						},
					};
				},
				'placeholder': 'Select Report',
			},
			'render_input': true,
		});

		// change css
		this.pageAction.removeClass('page-actions');
		this.selectionField.$wrapper.css('text-align', 'left');
	}

	changeTitle() {
		this.pageTitle.text(`${this.dashboardName} Report`);
	}
}

frappe.pages['analyticaone-reports'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Analyticaone Reports',
		single_column: true
	});
	$(frappe.render_template('analyticaone_reports')).appendTo(page.body);
}
frappe.pages['weekly-report'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Weekly Report',
		single_column: true
	});
}
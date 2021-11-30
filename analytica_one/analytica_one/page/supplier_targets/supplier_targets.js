frappe.pages['supplier-targets'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Supplier Targets',
		single_column: true
	});
}
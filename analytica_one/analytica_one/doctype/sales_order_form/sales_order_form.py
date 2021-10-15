# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import json

import frappe
import frappe.utils
from frappe import _
from frappe.contacts.doctype.address.address import get_company_address
from frappe.desk.notifications import clear_doctype_notifications
from frappe.model.mapper import get_mapped_doc
from frappe.model.utils import get_fetch_values
from frappe.utils import add_days, cint, cstr, flt, get_link_to_form, getdate, nowdate, strip_html
from six import string_types

from erpnext.accounts.doctype.sales_invoice.sales_invoice import (
	unlink_inter_company_doc,
	update_linked_doc,
	validate_inter_company_party,
)
from erpnext.controllers.selling_controller import SellingController
from erpnext.manufacturing.doctype.production_plan.production_plan import (
	get_items_for_material_requests,
)
from erpnext.selling.doctype.customer.customer import check_credit_limit
from erpnext.setup.doctype.item_group.item_group import get_item_group_defaults
from erpnext.stock.doctype.item.item import get_item_defaults
from erpnext.stock.stock_balance import get_reserved_qty, update_bin_qty

form_grid_templates = {
	"items": "templates/form_grid/item_grid.html"
}

class WarehouseRequired(frappe.ValidationError): pass

class SalesOrderForm(SellingController):
	pass

@frappe.whitelist()
def make_sales_order(source_name, target_doc=None):
	frappe.msgprint('called')
#	quotation = frappe.db.get_value("Quotation", source_name, ["transaction_date", "valid_till"], as_dict = 1)
#	if quotation.valid_till and (quotation.valid_till < quotation.transaction_date or quotation.valid_till < getdate(nowdate())):
#		frappe.throw(_("Validity period of this quotation has ended."))
	return _make_sales_order(source_name, target_doc)
@frappe.whitelist()
def _make_sales_order(source_name, target_doc=None, ignore_permissions=False):
	frappe.msgprint('sales '+str(source_name))
	#customer = _make_customer(source_name, ignore_permissions)

	def set_missing_values(source, target):
		frappe.msgprint('set miss')
		#if customer:
		#	target.customer = customer.name
		#	target.customer_name = customer.customer_name
		if source.referral_sales_partner:
			target.sales_partner=source.referral_sales_partner
			target.commission_rate=frappe.get_value('Sales Partner', source.referral_sales_partner, 'commission_rate')
		target.ignore_pricing_rule = 1
		target.flags.ignore_permissions = ignore_permissions
		target.run_method("set_missing_values")
		target.run_method("calculate_taxes_and_totals")

	def update_item(obj, target, source_parent):
		frappe.msgprint('update')
		target.stock_qty = flt(obj.qty) * flt(obj.conversion_factor)

		if obj.against_blanket_order:
			target.against_blanket_order = obj.against_blanket_order
			target.blanket_order = obj.blanket_order
			target.blanket_order_rate = obj.blanket_order_rate

	doclist = get_mapped_doc("Sales Order Form", source_name, {
			"Sales Order Form": {
				"doctype": "Sales Order",
				"validation": {
					"docstatus": ["=", 1]
				}
			},
			"Sales Order Form Item": {
				"doctype": "Sales Order Item",
				"field_map": {
					"parent": "prevdoc_docname"
				},
				"postprocess": update_item
			},
			"Sales Taxes and Charges": {
				"doctype": "Sales Taxes and Charges",
				"add_if_empty": True
			},
			"Sales Team": {
				"doctype": "Sales Team",
				"add_if_empty": True
			},
			"Payment Schedule": {
				"doctype": "Payment Schedule",
				"add_if_empty": True
			}
		}, target_doc, set_missing_values, ignore_permissions=ignore_permissions)

	# postprocess: fetch shipping address, set missing values

	return doclist
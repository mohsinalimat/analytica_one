# Copyright (c) 2021, THE ELECTRONIC COMMERCE & DATA CONSULTANTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SupplierRequestForm(Document):
	def validate(self):
		exist_sup = frappe.db.sql("""select name from `tabSupplier` where supplier_name = %s and supplier_group = %s""",(self.supplier_name,self.supplier_group),as_dict=1)
		
		if exist_sup:
			frappe.throw("Supplier Name is already exist in Supplier!")

	def on_submit(self):
		supp = frappe.new_doc('Supplier')
		supp.supplier_name = self.supplier_name
		supp.supplier_group = self.supplier_group
		supp.country = self.country
		supp.tax_id = self.tax_id
		supp.tax_category = self.tax_category
		supp.tax_withholding_category = self.tax_withholding_category
		supp.is_transporter = self.is_transporter
		supp.is_internal_supplier = self.is_internal_supplier
		supp.supplier_type = self.supplier_type
		supp.default_currency = self.billing_currency

		supp.save()

		adrs = frappe.new_doc('Address')
		adrs.address_title = self.address_title
		adrs.address_type = self.address_type
		adrs.address_line1 = self.address_line_1
		adrs.address_line2 = self.address_line_2
		adrs.city = self.city
		adrs.country = self.county
		adrs.pincode = self.pincode
		adrs.email_id = self.email_id
		adrs.phone = self.phone
		adrs.fax = self.fax
		adrs.is_primary_address = self.is_primary_address
	
		adrs.append('links', {
			"link_doctype": "Supplier",
			"link_name" : self.supplier_name,
			"link_title": self.address_title
		})
		adrs.save()


		ct = frappe.new_doc('Contact')
		ct.first_name = self.first_name
		ct.middle_name = self.middle_name
		ct.last_name = self.last_name
		ct.email_id = self.email_ad
		ct.user = self.user
		ct.status = self.status
		ct.salutation = self.salutation
		ct.designation = self.designation
		ct.gender = self.gender
		ct.phone = self.phone_no
		ct.company_name = self.company_name

		ct.append('links', {
			"link_doctype": "Supplier",
			"link_name" : self.supplier_name,
			"link_title": self.supplier_name
		})
		ct.save()


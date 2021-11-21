# Copyright (c) 2021, THE ELECTRONIC COMMERCE & DATA CONSULTANTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomerRequestForm(Document):
	def validate(self):
		exist_sup = frappe.db.sql("""select name from `tabCustomer` where customer_name = %s and customer_group = %s""",(self.customer_name,self.customer_group),as_dict=1)
		
		if exist_sup:
			frappe.throw("Customer Name is already exist in Customer!")

	def on_submit(self):
		cust = frappe.new_doc('Customer')
		cust.salutation = self.salutation
		cust.customer_name = self.customer_name
		cust.customer_type = self.customer_type
		cust.customer_group = self.customer_group
		cust.territory = self.territory
		cust.default_currency = self.default_currency

		cust.save()

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
			"link_doctype": "Customer",
			"link_name" : self.customer_name,
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
			"link_doctype": "Customer",
			"link_name" : self.customer_name,
			"link_title": self.customer_name
		})

		ct.save()
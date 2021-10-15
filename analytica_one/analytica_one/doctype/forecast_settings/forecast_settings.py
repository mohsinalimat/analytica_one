# Copyright (c) 2021, THE ELECTRONIC COMMERCE & DATA CONSULTANTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ForecastSettings(Document):
	pass

	# def onload(self):
	# 	if not self.employee_forecast:
	# 		emp_list = frappe.db.sql("""select name, employee_name, company from `tabEmployee` where status = %s""",('Active'),as_dict=1)
	# 		if emp_list:
	# 			for i in emp_list:
		# 			child = self.append('employee_forecast',{})
		# 			child.employee = i.name
		# 			child.employee_name = i.employee_name
		# 			child.company = i.company
				

		# if not self.supplier_forecast:
		# 	supp_list = frappe.db.sql("""select name from `tabSupplier`""",as_dict=1)
		# 	for j in supp_list:
		# 		child = self.append('supplier_forecast',{})
		# 		child.supplier = j.name
			

	# def validate(self):
	# 	if self.supplier_forecast:
	# 		for i in self.get('supplier_forecast'):
	# 			i.total_value_ksa = i.ksa_central + i.ksa_ea_hpi + i.ksa_western + i.ksa_aramco + i.ksa_service
	# 			i.target = i.ksa_central+ i.ksa_ea_hpi + i.ksa_western + i.ksa_aramco + i.ksa_service + i.qatar + i.jordan + i.bahrain
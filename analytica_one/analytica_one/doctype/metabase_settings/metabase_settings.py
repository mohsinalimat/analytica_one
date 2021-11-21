# Copyright (c) 2021, THE ELECTRONIC COMMERCE & DATA CONSULTANTS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MetabaseSettings(Document):
	pass

@frappe.whitelist()
def set_wake(val):
	mb = frappe.get_doc('Metabase Settings')
	mbwake = (int(mb.wake) + int(val))
	mb.wake = int(mbwake)
	
	mb.save()

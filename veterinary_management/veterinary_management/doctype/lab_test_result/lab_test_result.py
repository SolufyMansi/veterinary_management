# Copyright (c) 2026, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LabTestResult(Document):
	def on_submit(self):
		self.db_set("status","Completed")
	def before_insert(self):
		if self.lab_test_template:
			template = frappe.get_doc("Lab Test Template", self.lab_test_template)
			template_parameters = template.parameters or []
			self.results = []
			for param in template_parameters:
				row = self.append("results", {})
				row.parameter = param.parameter_name
				row.unit = param.unit
				row.normal_min = param.normal_min
				row.normal_max = param.normal_max
				row.result = "" 
	def on_update(self):
		if self.lab_test_template:
			template = frappe.get_doc("Lab Test Template", self.lab_test_template)
			template_parameters = template.parameters or []
			self.results = []
			for param in template_parameters:
				row = self.append("results", {})
				row.parameter = param.parameter_name
				row.unit = param.unit
				row.normal_min = param.normal_min
				row.normal_max = param.normal_max
				row.result = "" 


		# patient = frappe.get_doc("Patient", doc.patient)
		# patient.append("lab_test_history", {
		# 	"test_date": doc.test_date,
		# 	"test_name": doc.lab_test_template,
		# 	"reference": doc.name
		# })
		# patient.save(ignore_permissions=True)
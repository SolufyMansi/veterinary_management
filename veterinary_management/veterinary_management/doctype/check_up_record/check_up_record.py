# Copyright (c) 2026, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CheckUpRecord(Document):
	def on_submit(self):
		self.db_set("status", "Completed")
		self.save()

	@frappe.whitelist()
	def create_lab_test_result(self, patient, test_types, appointment, reference_doctype, reference_name):
		created_tests = [] 
		test_types = [test_type.strip() for test_type in test_types.split(',')]

		for test_type in test_types:
			lab_test_templates = frappe.get_all(
				'Lab Test Template', 
				filters={'test_category': test_type}, 
				fields=['name', 'test_category']
			)

			# Check if templates exist for the test category
			# if not lab_test_templates:
			# 	frappe.msgprint(f"No templates found for test category: {test_type}")
			# 	continue  # Skip to the next test type if no templates are found
			for template in lab_test_templates:
				new_lab_test_result = frappe.get_doc({
					'doctype': 'Lab Test Result',
					'patient': patient,
					'status': 'Pending', 
					'lab_test_template': template.name,
					'test_category': template.test_category,
					'appointment': appointment,
					'reference_doctype': reference_doctype,
					'reference_name': reference_name
				})
				new_lab_test_result.insert(ignore_permissions=True) 
				created_tests.append(template.test_category)  
		if created_tests:
			return f"Created Lab Test Results for the following categories: {', '.join(created_tests)}."
		else:
			return "No Lab Test Result records were created."

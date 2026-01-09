# Copyright (c) 2025, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VaccinationRecord(Document):
	def after_insert(self):
		vaccination_datails(self)
def vaccination_datails(doc):
	animal=frappe.db.get_all("Vaccination Record",{"animal":doc.animal},["name","animal","vaccine","date_administered","next_due_date"])
	if not animal:
		return
	custom_html = """
        <table>
            <tr>
                <td><b>Vaccine</b></td>
                <td><b>Date Administered</b></td>
                <td><b>Next Due Date</b></td>
            </tr>
    """
	current_req = True
	for row in animal:
		custom_html += f"""
            <tr>
                <td>{row.vaccine }</td>
                <td>{row.date_administered}</td>
                <td>{row.next_due_date}</td>
            </tr>
        """
	custom_html += f"""</table>"""
	# frappe.throw(f"{animal}")
	for row in animal:
		frappe.db.set_value("Patient",doc.animal, "vaccination_record",custom_html,update_modified=False
    )   
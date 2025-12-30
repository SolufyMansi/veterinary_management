
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def setup():
    create_module_if_missing()
    create_vm_herd()
    create_vm_animal()
    create_vm_appointment()
    create_vm_prescription()
    create_vm_consultation()
    create_vm_vaccination_record()
    create_vm_medical_procedure()
    frappe.db.commit()

def create_module_if_missing():
    if not frappe.db.exists("Module Def", "Veterinary Management"):
        doc = frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "Veterinary Management",
            "app_name": "veterinary_management"
        })
        doc.insert(ignore_permissions=True)

def create_doctype(name, fields, **kwargs):
    if frappe.db.exists("DocType", name):
        print(f"DocType {name} already exists.")
        return

    doc = frappe.get_doc({
        "doctype": "DocType",
        "module": "Veterinary Management",
        "name": name,
        "custom": 0,
        "beta": 0,
        "fields": fields,
        "permissions": [{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}],
        **kwargs
    })
    doc.insert(ignore_permissions=True)
    print(f"Created DocType {name}")

def create_vm_herd():
    fields = [
        {"fieldname": "herd_name", "label": "Herd Name", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "species", "label": "Species", "fieldtype": "Data"},
        {"fieldname": "location", "label": "Location", "fieldtype": "Data"},
        {"fieldname": "count", "label": "Count", "fieldtype": "Int"}
    ]
    create_doctype("VM Herd", fields, naming_rule="Expression", autoname="HERD-.#####")

def create_vm_animal():
    fields = [
        {"fieldname": "animal_name", "label": "Name", "fieldtype": "Data"},
        {"fieldname": "species", "label": "Species", "fieldtype": "Data", "reqd": 1, "in_list_view": 1},
        {"fieldname": "breed", "label": "Breed", "fieldtype": "Data"},
        {"fieldname": "sex", "label": "Sex", "fieldtype": "Select", "options": "Male\nFemale"},
        {"fieldname": "dob", "label": "Date of Birth", "fieldtype": "Date"},
        {"fieldname": "customer", "label": "Owner", "fieldtype": "Link", "options": "Customer", "reqd": 1},
        {"fieldname": "microchip_id", "label": "Microchip ID", "fieldtype": "Data"},
        {"fieldname": "herd", "label": "Herd", "fieldtype": "Link", "options": "VM Herd"}
    ]
    create_doctype("VM Animal", fields, naming_rule="Expression", autoname="ANI-.#####")

def create_vm_appointment():
    fields = [
        {"fieldname": "customer", "label": "Customer", "fieldtype": "Link", "options": "Customer", "reqd": 1},
        {"fieldname": "vm_animal", "label": "Animal", "fieldtype": "Link", "options": "VM Animal"},
        {"fieldname": "doctor", "label": "Doctor", "fieldtype": "Link", "options": "User"},
        {"fieldname": "appointment_date", "label": "Date & Time", "fieldtype": "Datetime", "reqd": 1},
        {"fieldname": "status", "label": "Status", "fieldtype": "Select", "options": "Scheduled\nCompleted\nCancelled", "default": "Scheduled"}
    ]
    create_doctype("VM Appointment", fields, naming_rule="Expression", autoname="APT-.#####")

def create_vm_consultation():
    fields = [
        {"fieldname": "appointment", "label": "Appointment", "fieldtype": "Link", "options": "VM Appointment"},
        {"fieldname": "symptoms", "label": "Symptoms", "fieldtype": "Text"},
        {"fieldname": "diagnosis", "label": "Diagnosis", "fieldtype": "Text"},
        {"fieldname": "treatment_plan", "label": "Treatment Plan", "fieldtype": "Text"},
        {"fieldname": "prescriptions", "label": "Prescriptions", "fieldtype": "Table", "options": "VM Prescription"}
    ]
    create_doctype("VM Consultation", fields, naming_rule="Expression", autoname="CNS-.#####")

def create_vm_prescription():
    fields = [
        {"fieldname": "item_code", "label": "Medicine", "fieldtype": "Link", "options": "Item", "in_list_view": 1},
        {"fieldname": "dosage", "label": "Dosage", "fieldtype": "Data", "in_list_view": 1},
        {"fieldname": "quantity", "label": "Quantity", "fieldtype": "Float", "in_list_view": 1}
    ]
    create_doctype("VM Prescription", fields, istable=1)

def create_vm_vaccination_record():
    fields = [
        {"fieldname": "animal", "label": "Animal", "fieldtype": "Link", "options": "VM Animal", "reqd": 1},
        {"fieldname": "vaccine", "label": "Vaccine", "fieldtype": "Link", "options": "Item"},
        {"fieldname": "date_administered", "label": "Date Administered", "fieldtype": "Date", "reqd": 1},
        {"fieldname": "next_due_date", "label": "Next Due Date", "fieldtype": "Date"}
    ]
    create_doctype("VM Vaccination Record", fields, naming_rule="Expression", autoname="VAC-.#####")

def create_vm_medical_procedure():
    fields = [
        {"fieldname": "animal", "label": "Animal", "fieldtype": "Link", "options": "VM Animal", "reqd": 1},
        {"fieldname": "procedure_name", "label": "Procedure Name", "fieldtype": "Data", "reqd": 1},
        {"fieldname": "surgeon", "label": "Surgeon", "fieldtype": "Link", "options": "User"}
    ]
    create_doctype("VM Medical Procedure", fields, naming_rule="Expression", autoname="PROC-.#####")


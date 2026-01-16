import frappe
from frappe import _

@frappe.whitelist()
def update_visit_date(doc,method=None):
    if doc.status=="Completed":
        pet=frappe.get_doc("Patient",doc.custom_pet)
        pet.db_set("last_visit_date",doc.scheduled_time)
        pet.save()
# def validate_double_booking(doc, method=None):
#     # frappe.throw("::::::::::")
#     conf_app = frappe.get_all('Appointment', filters={
#         'scheduled_time': doc.scheduled_time,
#         'custom_pet': doc.custom_pet,
#         'custom_doctor':doc.custom_doctor,
#         'name': ['!=', doc.name]  
#     }, fields=["name"])

#     if conf_app:
#         frappe.throw(_("This vet is already booked for this time."))

def validate_double_booking(doc, method=None):
    existing_appointments = frappe.get_all(
        'Appointment',
        filters={
            'custom_doctor': doc.custom_doctor,
            'custom_scheduled_date': doc.custom_scheduled_date,
            'custom_schedule_time': doc.custom_schedule_time,
            'name': ['!=', doc.name]  
        },
        fields=['name']
    )

    if existing_appointments:
        frappe.throw(_("This vet is already booked at this date and time."))
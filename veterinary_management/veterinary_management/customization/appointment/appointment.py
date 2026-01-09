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
    pass
    # start_time = f"{doc.custom_scheduled_date} {doc.custom_schedule_time}"
    # from datetime import datetime, timedelta
    # start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    # end_time = start_time + timedelta(minutes=doc.custom_duration)
    # overlapping_appointments = frappe.get_all('Appointment', filters={
    #     'custom_doctor': doc.custom_doctor,  
    #     'name': ['!=', doc.name],  
    #     'custom_scheduled_date': doc.custom_scheduled_date,  
    # }, fields=["name", "custom_scheduled_date", "custom_schedule_time", "custom_duration"])

    # for app in overlapping_appointments:
    #     existing_start_time = f"{app.custom_scheduled_date} {app.custom_schedule_time}"
    #     existing_start_time = datetime.strptime(existing_start_time, '%Y-%m-%d %H:%M:%S')
    #     existing_end_time = existing_start_time + timedelta(minutes=app.custom_duration)
    #     if (start_time < existing_end_time and end_time > existing_start_time):  
    #         frappe.throw(_("This vet is already booked during this time."))


# import frappe

# @frappe.whitelist()
# def get_appointments(date=None, status=None):
#     filters = {}

#     if date:
#         filters["custom_scheduled_date"] = date

#     if status:
#         filters["status"] = status

#     return frappe.get_all(
#         "Appointment",
#         filters=filters,
#         fields=[
#             "name",
#             "custom_scheduled_date",
#             "custom_schedule_time",
#             "status",
#             "custom_doctor_name",
#             "customer_name"
#         ],
#         order_by="custom_scheduled_date desc",
#         limit_page_length=50
#     )

import frappe

@frappe.whitelist()
def get_appointments(date=None, status=None):
    filters = {}

    if date:
        filters["custom_scheduled_date"] = date

    if status:
        filters["status"] = status

    return frappe.get_all(
        "Appointment",
        filters=filters,
        fields=[
            "name",
            "custom_scheduled_date",
            "custom_schedule_time",
            "status",
            "custom_doctor_name",
            "customer_name"
        ],
        order_by="custom_scheduled_date desc",
        limit_page_length=50
    )


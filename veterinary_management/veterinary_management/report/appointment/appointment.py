# Copyright (c) 2025, Sahil Suthar and contributors
# For license information, please see license.txt
import frappe
from frappe import _
from frappe.query_builder import DocType


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	return [
		{
			_("label"): "ID",
			_("fieldname"): "appointment_id",
			_("fieldtype"): "Link",
			_("options"): "Appointment",
			_("width"): 150,
		},
		{
			_("label"): "Scheduled Time",
			_("fieldname"): "scheduled_time",
			_("fieldtype"): "Datetime",
			_("width"): 200,
		},
		{
			_("label"): "Pet Name",
			_("fieldname"): "customer_name",
			_("fieldtype"): "Data",
			_("width"): 200,
		},
		{
			_("label"): "Pet Owner Name",
			_("fieldname"): "custom_owner_name",
			_("fieldtype"): "Data",
			_("width"): 200,
		},
		{
			_("label"): "Appointment Reason",
			_("fieldname"): "custom_reason",
			_("fieldtype"): "Data",
			_("width"): 150,
		},
		
		{
			_("label"): "Status",
			_("fieldname"): "status",
			_("fieldtype"): "Data",
			_("width"): 100,
		},
		
	]


def get_data(filters):
	Appointment = DocType("Appointment")
	Employee = DocType("Employee")
	query = (
		frappe.qb.from_(Appointment)
		.select(
			Appointment.name.as_("appointment_id"),
			Appointment.custom_reason,
			Appointment.scheduled_time,
			Appointment.customer_name,
			Appointment.custom_owner_name,
			Appointment.status,
		)
	)

	# Apply filters if any
	# if filters and filters.get("employee"):
	#     query = query.where(Employee.name == filters["employee"])

	if filters and filters.get("status"):
		query = query.where(Appointment.status == filters["status"])

	if filters and filters.get("custom_reason"):
		query = query.where(Appointment.custom_reason == filters["custom_reason"])
	if filters and filters.get("scheduled_time"):
			query = query.where(Appointment.scheduled_time == filters["scheduled_time"])
	result = query.run(as_dict=True)
	return result

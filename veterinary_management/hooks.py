app_name = "veterinary_management"
app_title = "Veterinary Management"
app_publisher = "Solufy"
app_description = "Veterinary Management Application"
app_email = "info@solufy.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
after_migrate = "veterinary_management.migrate.after_migrate"
add_to_apps_screen = [
	{
		"name": "veterinary_management",
		"logo": "/assets/veterinary_management/logo.svg",
		"title": "Veterinary Management",
		"route": "/app/veterinary-management"
	}
]
fixtures=["Translation"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/veterinary_management/css/veterinary_management.css"
# app_include_js = "/assets/veterinary_management/js/veterinary_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/veterinary_management/css/veterinary_management.css"
# web_include_js = "/assets/veterinary_management/js/veterinary_management.js"

# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "veterinary_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Appointment" : "veterinary_management/customization/appointment/appointment.js",
              "Customer"    :"veterinary_management/customization/customer/customer.js",
              "ToDo":"veterinary_management/customization/todo/todo.js",
			  }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "veterinary_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "veterinary_management.utils.jinja_methods",
# 	"filters": "veterinary_management.utils.jinja_filters"
# }

# Installation
# ------------
#
# before_install = "veterinary_management.install.before_install"
after_install = "veterinary_management.install.after_install"
#
# Uninstallation
# ------------
#
# before_uninstall = "veterinary_management.uninstall.before_uninstall"
# after_uninstall = "veterinary_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "veterinary_management.utils.before_app_install"
# after_app_install = "veterinary_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "veterinary_management.utils.before_app_uninstall"
# after_app_uninstall = "veterinary_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "veterinary_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Appointment": {
		"on_update": ["veterinary_management.veterinary_management.customization.appointment.appointment.update_visit_date","veterinary_management.veterinary_management.customization.appointment.appointment.validate_double_booking"],
		},
	"Sales Invoice": {
		"on_submit": "veterinary_management.veterinary_management.customization.sales_invoice.sales_invoice.on_submit",
		},
    # "ToDo": {
	# 	"before_save": "veterinary_management.veterinary_management.customization.todo.todo.before_save",
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"veterinary_management.tasks.all"
# 	],
# 	"daily": [
# 		"veterinary_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"veterinary_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"veterinary_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"veterinary_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "veterinary_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "veterinary_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "veterinary_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["veterinary_management.utils.before_request"]
# after_request = ["veterinary_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["veterinary_management.utils.before_job"]
# after_job = ["veterinary_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"veterinary_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


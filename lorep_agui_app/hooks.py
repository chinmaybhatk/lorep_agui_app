from . import __version__ as app_version

app_name = "lorep_agui_app"
app_title = "Lorep AgUI App"
app_publisher = "Your Company"
app_description = "Custom Frappe v15 app with AgUI integration"
app_email = "developer@company.com"
app_license = "MIT"
app_version = app_version

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lorep_agui_app/css/lorep_agui_app.css"
# app_include_js = "/assets/lorep_agui_app/js/lorep_agui_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/lorep_agui_app/css/lorep_agui_app.css"
# web_include_js = "/assets/lorep_agui_app/js/lorep_agui_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lorep_agui_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "lorep_agui_app.utils.jinja_methods",
#	"filters": "lorep_agui_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lorep_agui_app.install.before_install"
# after_install = "lorep_agui_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lorep_agui_app.uninstall.before_uninstall"
# after_uninstall = "lorep_agui_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lorep_agui_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"lorep_agui_app.tasks.all"
#	],
#	"daily": [
#		"lorep_agui_app.tasks.daily"
#	],
#	"hourly": [
#		"lorep_agui_app.tasks.hourly"
#	],
#	"weekly": [
#		"lorep_agui_app.tasks.weekly"
#	],
#	"monthly": [
#		"lorep_agui_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "lorep_agui_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "lorep_agui_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "lorep_agui_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lorep_agui_app.utils.before_request"]
# after_request = ["lorep_agui_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["lorep_agui_app.utils.before_job"]
# after_job = ["lorep_agui_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"lorep_agui_app.auth.validate"
# ]
from . import __version__ as app_version

app_name = "erpnext_chinese"
app_title = "ERPNext Chinese"
app_publisher = "yuzelin"
app_description = "ERPNext中文汉化，简化，优化"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "yuxinyong@163.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_chinese/css/erpnext_chinese.css"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_chinese/css/erpnext_chinese.css"
# web_include_js = "/assets/erpnext_chinese/js/erpnext_chinese.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

#doctype_list_js = {"Quality Inspection" : "public/js/quality_inspection_list.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "erpnext_chinese.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_chinese.install.before_install"
#after_install = "erpnext_chinese.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_chinese.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Purchase Order":{
# 		"before_validate": "erpnext_chinese.api.doc_event.po_validate"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_chinese.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_chinese.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_chinese.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_chinese.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_chinese.tasks.monthly"
# 	]
# }

# Testing
# ------

# before_tests = "erpnext_chinese.install.before_tests"

# Overriding Methods
# ------------------------------
#
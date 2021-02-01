# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "global_trade"
app_title = "Global Trade"
app_publisher = "tüit GmBH"
app_description = "ERPNext App for internation goods trading."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "administrator@tueit.de"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/global_trade/css/global_trade.css"
# app_include_js = "/assets/global_trade/js/global_trade.js"

# include js, css files in header of web template
# web_include_css = "/assets/global_trade/css/global_trade.css"
# web_include_js = "/assets/global_trade/js/global_trade.js"

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

# Website user home page (by function)
# get_website_user_home_page = "global_trade.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "global_trade.install.before_install"
# after_install = "global_trade.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "global_trade.notifications.get_notification_config"

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
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"global_trade.tasks.all"
# 	],
# 	"daily": [
# 		"global_trade.tasks.daily"
# 	],
# 	"hourly": [
# 		"global_trade.tasks.hourly"
# 	],
# 	"weekly": [
# 		"global_trade.tasks.weekly"
# 	]
# 	"monthly": [
# 		"global_trade.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "global_trade.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "global_trade.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "global_trade.task.get_dashboard_data"
# }


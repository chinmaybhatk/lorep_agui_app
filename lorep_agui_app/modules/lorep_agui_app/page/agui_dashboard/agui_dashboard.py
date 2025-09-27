import frappe

@frappe.whitelist()
def get_agui_config():
	"""Get AgUI configuration for the dashboard"""
	return {
		"app_name": "lorep_agui_app",
		"agent_endpoint": "/api/method/lorep_agui_app.api.agent.process_request",
		"websocket_url": frappe.utils.get_url() + "/ws"
	}

@frappe.whitelist()
def get_dashboard_data():
	"""Get initial dashboard data"""
	return {
		"user": frappe.session.user,
		"company": frappe.defaults.get_user_default("Company"),
		"modules": frappe.get_installed_apps()
	}
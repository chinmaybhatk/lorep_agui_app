import frappe
import json
import openai
from typing import List, Dict

@frappe.whitelist()
def process_request(message: str, history: List[Dict] = None):
	"""Process user request through OpenAI agent"""
	try:
		# Get OpenAI configuration
		openai_config = get_openai_config()
		if not openai_config:
			return {"content": "OpenAI configuration not found. Please configure in Site Config."}
		
		# Initialize OpenAI client
		client = openai.OpenAI(api_key=openai_config.get("api_key"))
		
		# Prepare conversation history
		messages = []
		
		# System prompt for Frappe personal assistant
		system_prompt = get_system_prompt()
		messages.append({"role": "system", "content": system_prompt})
		
		# Add conversation history
		if history:
			for msg in history[-10:]:  # Keep last 10 messages for context
				messages.append({
					"role": msg.get("role", "user"),
					"content": msg.get("content", "")
				})
		
		# Add current user message
		messages.append({"role": "user", "content": message})
		
		# Call OpenAI
		response = client.chat.completions.create(
			model=openai_config.get("model", "gpt-3.5-turbo"),
			messages=messages,
			max_tokens=1000,
			temperature=0.7
		)
		
		assistant_message = response.choices[0].message.content
		
		# Log conversation for future reference
		log_conversation(message, assistant_message)
		
		return {"content": assistant_message}
		
	except Exception as e:
		frappe.log_error(f"AgUI Agent Error: {str(e)}")
		return {"content": f"Sorry, I encountered an error: {str(e)}"}

def get_openai_config():
	"""Get OpenAI configuration from site config"""
	try:
		# Try to get from site config first
		config = frappe.get_site_config()
		if config.get("openai_api_key"):
			return {
				"api_key": config.get("openai_api_key"),
				"model": config.get("openai_model", "gpt-3.5-turbo")
			}
		
		# Fallback to environment variable
		import os
		api_key = os.getenv("OPENAI_API_KEY")
		if api_key:
			return {
				"api_key": api_key,
				"model": os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
			}
		
		return None
	except Exception as e:
		frappe.log_error(f"OpenAI Config Error: {str(e)}")
		return None

def get_system_prompt():
	"""Get system prompt for the personal assistant"""
	user = frappe.session.user
	company = frappe.defaults.get_user_default("Company") or "Your Company"
	
	return f"""You are a helpful personal assistant integrated into Frappe/ERPNext for {user} at {company}.

You can help with:
1. Frappe/ERPNext queries and operations
2. General business questions
3. Data analysis and reporting suggestions
4. Workflow optimization
5. Documentation and help

Current context:
- User: {user}
- Company: {company}
- System: Frappe v15 with AgUI integration

Please be concise, helpful, and professional. If you need to perform actions in Frappe, explain what the user should do or what permissions might be needed."""

@frappe.whitelist()
def get_user_context():
	"""Get current user context for the assistant"""
	try:
		user = frappe.session.user
		user_doc = frappe.get_doc("User", user)
		
		context = {
			"user": user,
			"full_name": user_doc.full_name,
			"email": user_doc.email,
			"roles": [role.role for role in user_doc.roles],
			"company": frappe.defaults.get_user_default("Company"),
			"language": user_doc.language or "en"
		}
		
		return context
	except Exception as e:
		frappe.log_error(f"User Context Error: {str(e)}")
		return {"user": frappe.session.user}

def log_conversation(user_message: str, assistant_response: str):
	"""Log conversation for analytics and improvement"""
	try:
		frappe.get_doc({
			"doctype": "AgUI Conversation",
			"user": frappe.session.user,
			"user_message": user_message,
			"assistant_response": assistant_response,
			"timestamp": frappe.utils.now()
		}).insert(ignore_permissions=True)
	except Exception:
		# Silently fail if logging doesn't work
		pass

@frappe.whitelist()
def get_quick_actions():
	"""Get quick actions for the assistant"""
	return [
		{
			"title": "Create New Document",
			"description": "Help me create a new document",
			"action": "create_document"
		},
		{
			"title": "Search Records",
			"description": "Search for existing records",
			"action": "search_records"
		},
		{
			"title": "Generate Report",
			"description": "Help me generate a report",
			"action": "generate_report"
		},
		{
			"title": "System Help",
			"description": "Get help with Frappe/ERPNext",
			"action": "system_help"
		}
	]
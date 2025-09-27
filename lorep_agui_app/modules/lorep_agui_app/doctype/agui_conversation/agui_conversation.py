import frappe
from frappe.model.document import Document

class AgUIConversation(Document):
	def before_insert(self):
		if not self.timestamp:
			self.timestamp = frappe.utils.now()
		if not self.session_id:
			self.session_id = frappe.generate_hash(length=10)
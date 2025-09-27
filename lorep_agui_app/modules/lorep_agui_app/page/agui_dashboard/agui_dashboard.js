frappe.pages['agui_dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Personal Assistant',
		single_column: true
	});

	// Add custom CSS for chat interface
	const style = document.createElement('style');
	style.textContent = `
		.agui-chat-container {
			height: calc(100vh - 160px);
			display: flex;
			flex-direction: column;
			background: #f8f9fa;
			border-radius: 8px;
			overflow: hidden;
			box-shadow: 0 2px 10px rgba(0,0,0,0.1);
		}
		.agui-chat-header {
			background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
			color: white;
			padding: 16px;
			text-align: center;
			font-weight: 600;
		}
		.agui-quick-actions {
			padding: 12px;
			background: white;
			border-bottom: 1px solid #e9ecef;
			display: flex;
			gap: 8px;
			flex-wrap: wrap;
		}
		.agui-quick-btn {
			background: #e9ecef;
			border: none;
			padding: 6px 12px;
			border-radius: 16px;
			font-size: 12px;
			cursor: pointer;
			transition: all 0.2s;
		}
		.agui-quick-btn:hover {
			background: #dee2e6;
			transform: translateY(-1px);
		}
	`;
	document.head.appendChild(style);

	// Add React container
	$(page.body).html(`
		<div id="agui-react-root" class="agui-chat-container"></div>
		<script src="https://unpkg.com/react@18/umd/react.development.js"></script>
		<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
		<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
		<div id="agui-scripts"></div>
	`);

	// Load AgUI components
	loadAgUIComponents();
};

function loadAgUIComponents() {
	// Create the AgUI React component
	const aguiScript = document.createElement('script');
	aguiScript.type = 'text/babel';
	aguiScript.text = `
		const { useState, useEffect } = React;

		function PersonalAssistant() {
			const [messages, setMessages] = useState([
				{ 
					role: 'assistant', 
					content: 'Hello! I\\'m your personal assistant. How can I help you with Frappe/ERPNext today?' 
				}
			]);
			const [input, setInput] = useState('');
			const [isLoading, setIsLoading] = useState(false);
			const [quickActions, setQuickActions] = useState([]);
			const [userContext, setUserContext] = useState({});

			useEffect(() => {
				// Load quick actions and user context
				frappe.call({
					method: 'lorep_agui_app.api.agent.get_quick_actions',
					callback: function(r) {
						if (r.message) {
							setQuickActions(r.message);
						}
					}
				});

				frappe.call({
					method: 'lorep_agui_app.api.agent.get_user_context',
					callback: function(r) {
						if (r.message) {
							setUserContext(r.message);
						}
					}
				});
			}, []);

			const sendMessage = async (messageText = input) => {
				if (!messageText.trim()) return;

				const userMessage = { role: 'user', content: messageText };
				setMessages(prev => [...prev, userMessage]);
				setInput('');
				setIsLoading(true);

				try {
					const response = await frappe.call({
						method: 'lorep_agui_app.api.agent.process_request',
						args: {
							message: messageText,
							history: messages
						}
					});

					if (response.message) {
						setMessages(prev => [...prev, {
							role: 'assistant',
							content: response.message.content
						}]);
					}
				} catch (error) {
					console.error('Error:', error);
					setMessages(prev => [...prev, {
						role: 'assistant',
						content: 'Sorry, there was an error processing your request. Please check the OpenAI configuration in site_config.json.'
					}]);
				} finally {
					setIsLoading(false);
				}
			};

			const handleQuickAction = (action) => {
				const actionMessages = {
					'create_document': 'Help me create a new document',
					'search_records': 'I need to search for records',
					'generate_report': 'Can you help me generate a report?',
					'system_help': 'I need help with the system'
				};
				sendMessage(actionMessages[action.action] || action.title);
			};

			return React.createElement('div', { 
				style: { height: '100%', display: 'flex', flexDirection: 'column' }
			}, [
				// Header
				React.createElement('div', {
					key: 'header',
					className: 'agui-chat-header'
				}, [
					React.createElement('div', { key: 'title' }, '🤖 Personal Assistant'),
					React.createElement('div', { 
						key: 'subtitle',
						style: { fontSize: '12px', opacity: 0.9, marginTop: '4px' }
					}, userContext.full_name ? \`Welcome, \${userContext.full_name}\` : 'AI-Powered Frappe Assistant')
				]),

				// Quick Actions
				React.createElement('div', {
					key: 'quick-actions',
					className: 'agui-quick-actions'
				}, quickActions.map((action, idx) => 
					React.createElement('button', {
						key: idx,
						className: 'agui-quick-btn',
						onClick: () => handleQuickAction(action),
						title: action.description
					}, action.title)
				)),
				
				// Messages
				React.createElement('div', {
					key: 'messages',
					style: {
						flex: 1,
						overflow: 'auto',
						padding: '16px',
						background: 'white'
					}
				}, messages.map((msg, idx) => 
					React.createElement('div', {
						key: idx,
						style: {
							marginBottom: '16px',
							display: 'flex',
							justifyContent: msg.role === 'user' ? 'flex-end' : 'flex-start'
						}
					}, React.createElement('div', {
						style: {
							maxWidth: '70%',
							padding: '12px 16px',
							borderRadius: '18px',
							backgroundColor: msg.role === 'user' ? '#007bff' : '#f1f3f4',
							color: msg.role === 'user' ? 'white' : '#333',
							wordWrap: 'break-word',
							fontSize: '14px',
							lineHeight: '1.4',
							boxShadow: '0 1px 2px rgba(0,0,0,0.1)'
						}
					}, msg.content))
				)),

				// Typing indicator
				isLoading && React.createElement('div', {
					key: 'typing',
					style: {
						padding: '16px',
						textAlign: 'center',
						color: '#666',
						fontSize: '14px'
					}
				}, '🤖 Assistant is typing...'),

				// Input area
				React.createElement('div', {
					key: 'input',
					style: {
						padding: '16px',
						borderTop: '1px solid #e9ecef',
						backgroundColor: 'white',
						display: 'flex',
						gap: '12px',
						alignItems: 'center'
					}
				}, [
					React.createElement('input', {
						key: 'text-input',
						type: 'text',
						value: input,
						onChange: (e) => setInput(e.target.value),
						onKeyPress: (e) => e.key === 'Enter' && !e.shiftKey && sendMessage(),
						placeholder: 'Ask me anything about Frappe, ERPNext, or your business...',
						disabled: isLoading,
						style: {
							flex: 1,
							padding: '12px 16px',
							border: '2px solid #e9ecef',
							borderRadius: '25px',
							outline: 'none',
							fontSize: '14px',
							transition: 'border-color 0.2s'
						}
					}),
					React.createElement('button', {
						key: 'send-btn',
						onClick: () => sendMessage(),
						disabled: isLoading || !input.trim(),
						style: {
							padding: '12px 20px',
							backgroundColor: '#007bff',
							color: 'white',
							border: 'none',
							borderRadius: '25px',
							cursor: (isLoading || !input.trim()) ? 'not-allowed' : 'pointer',
							fontWeight: '600',
							fontSize: '14px',
							opacity: (isLoading || !input.trim()) ? 0.6 : 1,
							transition: 'all 0.2s'
						}
					}, isLoading ? '⏳' : '📤')
				])
			]);
		}

		ReactDOM.render(React.createElement(PersonalAssistant), document.getElementById('agui-react-root'));
	`;

	document.getElementById('agui-scripts').appendChild(aguiScript);
}
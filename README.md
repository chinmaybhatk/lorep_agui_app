# Lorep AgUI App

A custom Frappe v15 app integrating AgUI for AI-powered personal assistant functionality.

## Features

- 🤖 **Personal Assistant Chat Interface**: Modern chat UI integrated into Frappe desk
- 🧠 **OpenAI Integration**: Powered by OpenAI's GPT models for intelligent responses
- 📊 **Frappe Context**: Assistant understands your Frappe/ERPNext environment
- ⚡ **Quick Actions**: Pre-defined shortcuts for common tasks
- 💾 **Conversation Logging**: Automatic conversation history tracking
- 🎨 **Modern UI**: Clean, responsive chat interface with AgUI principles

## Installation

1. **Add to Frappe bench:**
   ```bash
   bench get-app https://github.com/chinmaybhatk/lorep_agui_app.git
   bench install-app lorep_agui_app --site your-site-name
   ```

2. **Configure OpenAI API:**
   Add to your `site_config.json`:
   ```json
   {
     "openai_api_key": "your-openai-api-key",
     "openai_model": "gpt-3.5-turbo"
   }
   ```

3. **Access the Assistant:**
   - Navigate to `Personal Assistant` page in your Frappe desk
   - Start chatting with your AI assistant!

## Usage

### Quick Actions
- **Create New Document**: Get help creating any Frappe document
- **Search Records**: Find existing records with natural language
- **Generate Report**: Get assistance with reporting and analytics
- **System Help**: Learn about Frappe/ERPNext features

### Example Interactions
- "How do I create a new customer?"
- "Show me sales reports for this month"
- "What permissions do I need to modify invoices?"
- "Help me set up a workflow for purchase orders"

## Technical Details

### Architecture
- **Backend**: Python API using OpenAI for LLM processing
- **Frontend**: React components embedded in Frappe pages
- **Data Storage**: Custom DocType for conversation logging
- **Integration**: Uses Frappe's authentication and permission system

### Files Structure
```
lorep_agui_app/
├── api/
│   └── agent.py              # OpenAI integration and API endpoints
├── modules/lorep_agui_app/
│   ├── doctype/
│   │   └── agui_conversation/ # Conversation logging DocType
│   └── page/
│       └── agui_dashboard/    # Main chat interface page
├── hooks.py                   # App configuration
└── pyproject.toml            # Package configuration
```

### API Endpoints
- `process_request()`: Process chat messages through OpenAI
- `get_user_context()`: Retrieve current user information
- `get_quick_actions()`: Get available quick action buttons

## Configuration

### OpenAI Models Supported
- `gpt-3.5-turbo` (recommended for cost efficiency)
- `gpt-4` (for enhanced capabilities)
- `gpt-4-turbo`

### Environment Variables (Alternative)
```bash
export OPENAI_API_KEY=your-api-key
export OPENAI_MODEL=gpt-3.5-turbo
```

## Customization

### Adding Custom Quick Actions
Edit `get_quick_actions()` in `api/agent.py`:
```python
{
    "title": "Custom Action",
    "description": "Your custom description",
    "action": "custom_action"
}
```

### Modifying System Prompt
Update `get_system_prompt()` in `api/agent.py` to customize the assistant's behavior and knowledge.

## Development

### Requirements
- Frappe Framework v15+
- Python 3.8+
- OpenAI Python package
- Valid OpenAI API key

### Local Development
```bash
# Install in development mode
bench get-app /path/to/lorep_agui_app
bench install-app lorep_agui_app

# Start development server
bench start
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Create an issue on GitHub
- Check Frappe documentation for general framework questions
- Refer to OpenAI documentation for API-related queries
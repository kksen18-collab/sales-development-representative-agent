# Sales Outreach - AI-Powered Multi-Agent Cold Email System

An intelligent, multi-agent system for generating and sending personalized cold sales emails using OpenAI's Agent Framework. This project leverages specialized AI agents that collaborate to research, draft, optimize, and deliver compelling sales emails while maintaining brand consistency and compliance.

## 🎯 Overview

Sales Outreach is a production-ready Python application that automates the cold email generation and delivery process. Instead of writing emails manually, you describe what you need, and the system orchestrates multiple specialized AI agents to:

1. **Generate** email drafts in different styles (professional, engaging, concise)
2. **Select** the best performing draft
3. **Optimize** the email with a compelling subject line
4. **Format** the email as HTML
5. **Send** the email via SendGrid

Perfect for B2B sales teams, SDRs, and founders who need to scale outreach while maintaining personalization and quality.

## 🏗️ Architecture

### Multi-Agent Orchestration

The system uses an agent orchestrator pattern with the following specialized agents:

```
Input Request
    ↓
Sales Manager Agent (Orchestrator)
    ├─→ Busy Sales Agent (Concise emails for time-pressed prospects)
    ├─→ Engaging Sales Agent (Witty, humorous approach)
    ├─→ Professional Sales Agent (Formal, serious tone)
    ├─→ Guardrail Name Check Agent (Compliance check)
    ├─→ Email Writer Agent (Formatting & subject line optimization)
    │   ├─→ Subject Writer Agent
    │   ├─→ HTML Converter Agent
    │   └─→ SendGrid Integration
```

### Agent Roles

| Agent | Purpose | Output |
|-------|---------|--------|
| **Sales Manager Agent** | Orchestrates the email generation process | Selects the best draft from three options |
| **Busy Sales Agent** | Generates concise, time-efficient emails | Quick, professional email draft |
| **Engaging Sales Agent** | Creates witty, humorous cold emails | Engaging email with personality |
| **Professional Sales Agent** | Writes formal, serious sales emails | Professional, technical email |
| **Guardrail Name Check Agent** | Validates recipient names for compliance | Compliance verification |
| **Email Writer Agent** | Formats and optimizes for delivery | Subject line + HTML email |
| **Subject Writer Agent** | Generates compelling subject lines | Optimized subject line |
| **HTML Converter Agent** | Converts text to professional HTML | HTML-formatted email body |

## ✨ Features

- **🤖 Multi-Agent AI System**: Specialized agents for different email styles
- **⚡ Intelligent Selection**: Automatically picks the best email draft
- **📧 SendGrid Integration**: Seamless email delivery
- **🛡️ Compliance Checks**: Built-in guardrails for brand safety
- **🎨 HTML Formatting**: Professional email rendering
- **🔄 Async/Await**: Non-blocking operations for scalability
- **📝 Customizable Prompts**: Easy to modify agent instructions
- **🔐 Environment-Based Configuration**: Secure API key management
- **📊 Structured Logging**: Debug-friendly logging throughout

## 📋 Prerequisites

- **Python**: 3.12 or higher
- **OpenAI API Key**: Required for using GPT models
- **SendGrid API Key**: Required for email delivery
- **Recipient Email Address**: For testing email delivery

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sales-outreach.git
cd sales-outreach
```

### 2. Set Up Python Environment

Using `uv` (recommended):
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
```

Or using `venv`:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
uv pip install -e .
# Or: pip install -e .
```

This installs all dependencies specified in `pyproject.toml`:
- `openai` - OpenAI API client
- `openai-agents` - Agent framework
- `sendgrid` - Email delivery service
- `pydantic` - Data validation
- `python-dotenv` - Environment variable management
- `gradio` - Optional UI framework
- `pypdf` - PDF processing

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-5.2  # Specify your preferred model

# SendGrid Configuration
SENDGRID_API_KEY=SG.your-sendgrid-api-key-here

# Email Configuration
SALES_OUTREACH_FROM_EMAIL=sender@yourcompany.com
SALES_OUTREACH_TO_EMAIL=prospect@company.com
```

**Security Note**: 
- Never commit `.env` to version control
- Store API keys in environment variables or secrets manager in production
- Validate API keys in `SalesOutreachSettings` (see `parameters.py`)

### Configuration File Location

Settings are loaded from:
1. Environment variables
2. `.env` file in `sales_outreach/` directory (default)

To change the settings file location, modify `SalesOutreachSettings.model_config` in [parameters.py](sales_outreach/parameters.py#L13).

## 📖 Usage

### Basic Usage

Run the interactive prompt-based system:

```bash
uv run python -m sales_outreach.app
# Or: python -m sales_outreach.app
```

You'll be prompted to enter your sales outreach request:

```
Enter the input request for the sales outreach agent: Send a cold email to a CEO at a fintech startup about our SOC2 compliance tool
```

The system will:
1. Generate three email drafts in different styles
2. Select the best one
3. Add an optimized subject line
4. Convert to HTML format
5. Send via SendGrid (if configured)
6. Return the final response

### Example Requests

```
"Send a cold email from Alice to CEO John Smith about our new SaaS platform"
"Generate a professional email for a VP of Engineering interested in compliance solutions"
"Create an engaging outreach email for a startup founder about our product"
```

### Programmatic Usage

```python
import asyncio
from sales_outreach.agent_orchestrator import AgentOrchestrator
from sales_outreach.parameters import SalesOutreachParameters, SalesOutreachSettings

async def main():
    settings = SalesOutreachSettings()
    params = SalesOutreachParameters(
        sales_outreach_input_message="Send a compelling cold email about our AI compliance tool"
    )
    
    orchestrator = AgentOrchestrator(params=params, settings=settings)
    await orchestrator.run()

if __name__ == "__main__":
    asyncio.run(main())
```

## 📁 Project Structure

```
sales-outreach/
├── main.py                          # Entry point
├── pyproject.toml                   # Project metadata & dependencies
├── README.md                        # This file
├── sales_outreach/
│   ├── __init__.py
│   ├── app.py                       # Main async application
│   ├── agent_orchestrator.py        # Multi-agent orchestration logic
│   ├── parameters.py                # Configuration & parameter models
│   ├── logger.py                    # Logging configuration
│   │
│   ├── _agents/                     # Specialized agent implementations
│   │   ├── agent_initializer.py     # Agent factory & initialization
│   │   ├── sales_manager_agent/     # Orchestrator agent
│   │   ├── busy_sales_agent/        # Concise email generation
│   │   ├── engaging_sales_agent/    # Engaging/humorous emails
│   │   ├── professional_sales_agent/# Professional emails
│   │   ├── guardrail_name_check_agent/ # Compliance validation
│   │   ├── emailer_agent/           # Email formatting & sending
│   │   ├── subject_writer_agent/    # Subject line generation
│   │   └── html_converter_agent/    # HTML conversion
│   │
│   ├── client/                      # External service clients
│   │   ├── agent_construct.py       # Agent builder wrapper
│   │   ├── openai.py                # OpenAI API client
│   │   └── sendgrid.py              # SendGrid email client
│   │
│   └── tools/                       # Agent tools & utilities
│       └── tools.py                 # Tool definitions for agents
│
└── sales_outreach.egg-info/         # Package metadata (generated)
```

## 🔧 Customization

### Modifying Agent Instructions

Each agent's instructions are defined in `instructions.py` within its folder. To customize:

```python
# Example: sales_outreach/_agents/professional_sales_agent/instructions.py
def instructions() -> str:
    return """You are a sales agent working for ComplAI...
    [Customize your instructions here]
    """
```

### Adding New Agents

1. Create a new folder: `sales_outreach/_agents/your_agent_name/`
2. Add `__init__.py` and `instructions.py`
3. Initialize in `agent_initializer.py`
4. Register tools in `tools.py`
5. Reference in `agent_orchestrator.py`

### Changing Email Templates

Modify the prompt instructions in:
- [professional_sales_agent/instructions.py](sales_outreach/_agents/professional_sales_agent/instructions.py)
- [engaging_sales_agent/instructions.py](sales_outreach/_agents/engaging_sales_agent/instructions.py)
- [busy_sales_agent/instructions.py](sales_outreach/_agents/busy_sales_agent/instructions.py)

### Using Different Models

Update the `model` field in your `.env` file:

```bash
OPENAI_MODEL=gpt-4o  # or gpt-4, gpt-3.5-turbo, etc.
```

## 🧪 Testing & Development

### Running with Development Dependencies

```bash
uv pip install -e ".[dev]"
```

This includes `ruff` and other development tools.

### Code Formatting & Linting

```bash
ruff check . --fix
ruff format .
```

### View Application Logs

The application uses structured logging. Logs are output to console with the format:

```
2024-03-12 10:15:23,456 | sales_outreach | INFO | Final response: ...
```

Adjust log levels in [logger.py](sales_outreach/logger.py#L7).

### Tracing Agent Execution

The project uses OpenAI Agents Framework's built-in tracing to monitor and debug agent execution flows. Traces capture:
- **Agent decisions** and tool calls
- **Execution flow** through the agent hierarchy
- **Intermediate outputs** from each agent
- **Guardrail checks** and their results

#### Enabling Traces

Traces are automatically recorded when agents run. They're wrapped in the `trace()` context manager in [agent_orchestrator.py](sales_outreach/agent_orchestrator.py#L100):

```python
with trace("Automated Sales Development Representative"):
    result = await Runner.run(
        sales_outreach_agent,
        input=self.params.sales_outreach_input_message,
        run_config=RunConfig(...)
    )
```

#### Viewing Traces

OpenAI traces are sent to the **OpenAI Traces Dashboard** (available in your OpenAI account under [Platform > Traces](https://platform.openai.com/traces)). Traces appear there automatically when agents execute.

To also enable local trace logging:

```python
import logging

# Enable trace logging
logging.getLogger("agents").setLevel(logging.DEBUG)
```

Or set environment variable:
```bash
AGENTS_LOG_LEVEL=DEBUG
```

**Note**: Ensure your `OPENAI_API_KEY` is set for traces to be sent to OpenAI's servers.

#### Example Trace Output

```
Trace: Automated Sales Development Representative
├── Input: "Send a cold email to CEO about SOC2 tool"
├── Guardrail Check
│   └── Output: name_found=False, proceed=True
├── Sales Manager Agent
│   ├── Busy Sales Agent
│   │   └── Output: "Dear CEO, [concise email]"
│   ├── Engaging Sales Agent
│   │   └── Output: "Hey CEO, [witty email]"
│   ├── Professional Sales Agent
│   │   └── Output: "Dear CEO, [formal email]"
│   └── Selection: Professional Agent wins
├── Email Writer Agent
│   ├── Subject Writer
│   │   └── Output: "Achieve SOC2 Compliance in 30 Days"
│   ├── HTML Converter
│   │   └── Output: "<html>[formatted email]</html>"
│   └── SendGrid Send
│       └── Status: Success
└── Final Output: Email sent successfully
```

#### Custom Traces

To add traces to custom agents:

```python
from agents import trace

with trace("My Custom Agent Operation"):
    result = await my_async_operation()
    logger.info(f"Operation result: {result}")
```

This helps debug complex multi-agent workflows and understand decision-making processes.

## 🚨 Troubleshooting

### "Invalid OpenAI API Key"

**Error**: `ValueError: invalid openai api key`

**Solution**: Ensure your OpenAI API key starts with `sk-` and is correctly set in `.env`:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

### "Invalid SendGrid API Key"

**Error**: `ValueError: invalid sendgrid api key`

**Solution**: SendGrid keys must start with `SG.`. Verify in `.env`:
```bash
SENDGRID_API_KEY=SG.your-actual-key-here
```

### "No module named 'openai_agents'"

**Error**: `ModuleNotFoundError: No module named 'openai_agents'`

**Solution**: Ensure `openai-agents` is installed:
```bash
uv pip install openai-agents==0.11.1
# Or reinstall all dependencies:
uv pip install -e .
```

### "Email not being sent"

**Checklist**:
1. Verify SendGrid API key is correct
2. Check `SALES_OUTREACH_FROM_EMAIL` and `SALES_OUTREACH_TO_EMAIL` are valid
3. Check SendGrid dashboard for delivery logs
4. Ensure email addresses are verified in SendGrid if using free tier

### Async Runtime Issues

If you encounter event loop errors, ensure you're using:
```python
asyncio.run(main())  # Correct
# NOT: asyncio.get_event_loop().run_until_complete()  # Deprecated
```

## 📊 How It Works

### Step-by-Step Flow

1. **Input**: User provides a sales request via prompt or programmatically
2. **Validation**: Guardrail agent checks for compliance issues
3. **Generation**: Sales Manager orchestrates three agents to generate different email styles
4. **Selection**: Sales Manager evaluates and selects the best draft
5. **Optimization**: Email Writer Agent generates subject line and formats HTML
6. **Delivery**: SendGrid integration sends the email
7. **Output**: System returns confirmation and final email text

### Example Workflow

```
User Input: "Cold email for CEO about SOC2 tool"
    ↓
Guardrail Check: "Name in message? No - proceed"
    ↓
Busy Agent: "Here's a concise version..."
Engaging Agent: "Here's a witty version..."
Professional Agent: "Here's a formal version..."
    ↓
Selection: Professional Agent's email wins
    ↓
Subject Writer: "Achieving SOC2 Compliance in 30 Days"
HTML Converter: Formats email with professional styling
    ↓
SendGrid: Email sent successfully
    ↓
Output: Final email and delivery confirmation
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes and test thoroughly
4. **Commit** with clear messages: `git commit -m "Add feature X"`
5. **Push** to your fork: `git push origin feature/my-feature`
6. **Open** a Pull Request with a description of changes

### Development Guidelines

- Follow PEP 8 style guide (use `ruff format` to auto-format)
- Use type hints for all functions
- Add docstrings to classes and methods
- Test new agents thoroughly before merging
- Update this README if you add significant features

## 📜 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙋 Support & Questions

- **Issues**: Open an issue on GitHub for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Documentation**: Check this README and code docstrings for detailed information

## 📚 Related Resources

- [OpenAI Agent Framework](https://platform.openai.com/docs/guides/agents)
- [SendGrid Python Library](https://github.com/sendgrid/sendgrid-python)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Async/Await in Python](https://docs.python.org/3/library/asyncio.html)

## 🌟 Acknowledgments

Built with:
- **OpenAI Agents Framework** for multi-agent orchestration
- **SendGrid** for reliable email delivery
- **Pydantic** for data validation
- **Python 3.12+** for async capabilities

---

**Happy Selling! 🚀** If this project helped you, please consider giving it a star ⭐

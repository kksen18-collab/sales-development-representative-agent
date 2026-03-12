import logging
from typing import Any, Dict

from agents import function_tool
from sendgrid.helpers.mail import Content, Email, Mail, To

from sales_outreach._agents.agent_initializer import agent_initializer
from sales_outreach.client.sendgrid import SendGridClient

logger = logging.getLogger(__name__)


class Tools:
    def __init__(
        self, agent_initializer: agent_initializer, sendgrid_client: SendGridClient
    ):
        self.agent_initializer = agent_initializer
        self.sendgrid_client = sendgrid_client
        self.sales_tool_description = "Write a cold sales email"
        self.subject_writer_tool_description = (
            "Write a compelling subject line for a cold sales email"
        )
        self.html_converter_tool_description = (
            "Convert a text email body to an HTML email body"
        )

    @property
    def build(self) -> Dict[str, Any]:
        busy_sales_tool = self.agent_initializer.busy_sales_agent.as_tool(
            tool_name="busy_sales_tool",
            tool_description=self.sales_tool_description,
        )
        engaging_sales_tool = self.agent_initializer.engaging_sales_agent.as_tool(
            tool_name="engaging_sales_agent_tool",
            tool_description=self.sales_tool_description,
        )
        professional_sales_tool = (
            self.agent_initializer.professional_sales_agent.as_tool(
                tool_name="professional_sales_agent_tool",
                tool_description=self.sales_tool_description,
            )
        )
        subject_writer_tool = self.agent_initializer.subject_writer_agent.as_tool(
            tool_name="subject_writer_tool",
            tool_description=self.subject_writer_tool_description,
        )
        html_converter_tool = self.agent_initializer.html_converter_agent.as_tool(
            tool_name="html_converter_tool",
            tool_description=self.html_converter_tool_description,
        )

        @function_tool
        def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
            """Send out an email with the given subject and HTML body to all sales prospects"""
            from_email = Email(self.sendgrid_client.from_email)
            to_email = To(self.sendgrid_client.to_email)  # Change to your recipient
            content = Content("text/html", html_body)
            mail = Mail(from_email, to_email, subject, content).get()
            self.sendgrid_client.sg.client.mail.send.post(request_body=mail)
            return {"status": "success"}

        return {
            "busy_sales_tool": busy_sales_tool,
            "engaging_sales_agent_tool": engaging_sales_tool,
            "professional_sales_agent_tool": professional_sales_tool,
            "subject_writer_tool": subject_writer_tool,
            "html_converter_tool": html_converter_tool,
            "send_html_email": send_html_email,
        }

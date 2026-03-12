import logging

from sales_outreach._agents.busy_sales_agent.instructions import (
    instructions as busy_sales_agent_instructions,
)
from sales_outreach._agents.engaging_sales_agent.instructions import (
    instructions as engaging_sales_agent_instructions,
)
from sales_outreach._agents.guardrail_name_check_agent.instructions import (
    instructions as guardrail_agent_instructions,
)
from sales_outreach._agents.html_converter_agent.instructions import (
    instructions as html_converter_agent_instructions,
)
from sales_outreach._agents.professional_sales_agent.instructions import (
    instructions as professional_sales_agent_instructions,
)
from sales_outreach._agents.subject_writer_agent.instructions import (
    instructions as subject_writer_agent_instructions,
)
from sales_outreach.client.agent_construct import AgentClient
from sales_outreach.parameters import NameCheckOutput, SalesOutreachSettings

logger = logging.getLogger(__name__)


class agent_initializer:
    def __init__(self, settings: SalesOutreachSettings):
        self.settings = settings
        self.busy_sales_agent = AgentClient(name="Busy Sales Agent").build(
            instructions=busy_sales_agent_instructions(), model=self.settings.model
        )
        self.engaging_sales_agent = AgentClient(name="Engaging Sales Agent").build(
            instructions=engaging_sales_agent_instructions(), model=self.settings.model
        )
        self.professional_sales_agent = AgentClient(
            name="Professional Sales Agent"
        ).build(
            instructions=professional_sales_agent_instructions(),
            model=self.settings.model,
        )
        self.subject_writer_agent = AgentClient(name="Subject Writer Agent").build(
            instructions=subject_writer_agent_instructions(), model=self.settings.model
        )
        self.html_converter_agent = AgentClient(name="HTML Converter Agent").build(
            instructions=html_converter_agent_instructions(), model=self.settings.model
        )
        self.guardrail_name_check_agent = AgentClient(name="Guardrail Name Check Agent").build(
            instructions=guardrail_agent_instructions(),
            model=self.settings.model,
            output_type=NameCheckOutput,
        )

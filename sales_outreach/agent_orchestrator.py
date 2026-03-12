import logging

from agents import GuardrailFunctionOutput, RunConfig, Runner, input_guardrail, trace
from agents.models.openai_provider import OpenAIProvider

from sales_outreach._agents.agent_initializer import agent_initializer
from sales_outreach._agents.emailer_agent.handoff_description import (
    handoff_description as email_writer_agent_handoff_description,
)
from sales_outreach._agents.emailer_agent.instructions import (
    instructions as email_writer_agent_instructions,
)
from sales_outreach._agents.sales_manager_agent.instructions import (
    instructions as sales_manager_agent_instructions,
)
from sales_outreach.client.agent_construct import AgentClient
from sales_outreach.client.openai import OpenAIClient
from sales_outreach.client.sendgrid import SendGridClient
from sales_outreach.parameters import SalesOutreachParameters, SalesOutreachSettings
from sales_outreach.tools.tools import Tools

logger = logging.getLogger(__name__)


class AgentOrchestrator:
    def __init__(
        self, settings: SalesOutreachSettings, params: SalesOutreachParameters
    ):
        self.settings = settings
        self.params = params
        self.openai_client = OpenAIClient(api_key=self.settings.openai_api_key)
        self.agent_client = AgentClient(name="Agent Orchestrator")
        self.sendgrid_client = SendGridClient(
            self.settings.sendgrid_api_key,
            from_email=self.settings.sales_outreach_from_email,
            to_email=self.settings.sales_outreach_to_email,
        )
        self.agent_initializer = agent_initializer(settings=self.settings)
        self.tools = Tools(
            agent_initializer=self.agent_initializer,
            sendgrid_client=self.sendgrid_client,
        )
        self.input_message = self.params.sales_outreach_input_message

    @property
    def _build_sales_outreach_agent(self):
        tools_list = self.tools.build

        sales_tools = [
            tools_list["busy_sales_tool"],
            tools_list["engaging_sales_agent_tool"],
            tools_list["professional_sales_agent_tool"],
        ]

        email_tools = [
            tools_list["subject_writer_tool"],
            tools_list["html_converter_tool"],
            tools_list["send_html_email"],
        ]

        email_writer_agent = AgentClient(name="Email Writer Agent").build(
            instructions=email_writer_agent_instructions(),
            tools=email_tools,
            model=self.settings.model,
            handoff_description=email_writer_agent_handoff_description(),
        )

        handoffs = [email_writer_agent]

        @input_guardrail
        async def guardrail_against_name(ctx, agent, message=self.input_message):
            guardrail_name_check_result = await Runner.run(
                self.agent_initializer.guardrail_name_check_agent,
                message,
                context=ctx.context,
            )
            is_name_in_message = (
                guardrail_name_check_result.final_output.is_name_in_message
            )
            return GuardrailFunctionOutput(
                output_info={"found_name": guardrail_name_check_result.final_output},
                tripwire_triggered=is_name_in_message,
            )

        input_guardrails = [guardrail_against_name]

        sales_manager_agent = AgentClient(name="Sales Manager Agent").build(
            instructions=sales_manager_agent_instructions(),
            tools=sales_tools,
            model=self.settings.model,
            handoffs=handoffs,
            input_guardrails=input_guardrails,
        )

        return sales_manager_agent

    async def run(self):
        sales_outreach_agent = self._build_sales_outreach_agent
        with trace("Automated Sales Development Representative"):
            result = await Runner.run(
                sales_outreach_agent,
                input=self.params.sales_outreach_input_message,
                run_config=RunConfig(
                    model_provider=OpenAIProvider(
                        openai_client=self.openai_client.async_client
                    )
                ),
            )

            logger.info(f"Final response: {result.final_output}")

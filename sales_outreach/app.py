import asyncio
import os

from sales_outreach.agent_orchestrator import AgentOrchestrator
from sales_outreach.logger import setup_logging
from sales_outreach.parameters import SalesOutreachParameters, SalesOutreachSettings


async def main():
    setup_logging()
    settings = SalesOutreachSettings()
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key
    sales_outreach_input_message = input(
        "Enter the input request for the sales outreach agent: "
    )
    params = SalesOutreachParameters(
        sales_outreach_input_message=sales_outreach_input_message
    )
    agent_orchestrator = AgentOrchestrator(params=params, settings=settings)
    await agent_orchestrator.run()


if __name__ == "__main__":
    asyncio.run(main())

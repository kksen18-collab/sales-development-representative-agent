import logging

from agents import Agent

logger = logging.getLogger(__name__)


class AgentClient:
    def __init__(self, name: str):
        self.name = name

    def build(self, *, instructions: str, model: str, **kwargs) -> Agent:
        return Agent(name=self.name, instructions=instructions, model=model, **kwargs)

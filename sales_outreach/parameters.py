from pathlib import Path

from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings


class SalesOutreachSettings(BaseSettings):
    openai_api_key: str
    sendgrid_api_key: str
    model: str = "gpt-5.2"
    sales_outreach_from_email: str
    sales_outreach_to_email: str

    model_config = {
        "env_file": Path(__file__).parent / ".env",
    }

    @field_validator("openai_api_key")
    @classmethod
    def validate_openai_key(cls, v):
        if not v.startswith("sk-"):
            raise ValueError("invalid openai api key")
        return v

    @field_validator("sendgrid_api_key")
    @classmethod
    def validate_sendgrid_key(cls, v):
        if not v.startswith("SG."):
            raise ValueError("invalid sendgrid api key")
        return v


class SalesOutreachParameters(BaseModel):
    sales_outreach_input_message: str = (
        "Send out a cold sales email addressed to Dear CEO from Alice"
    )


class NameCheckOutput(BaseModel):
    is_name_in_message: bool
    name: str

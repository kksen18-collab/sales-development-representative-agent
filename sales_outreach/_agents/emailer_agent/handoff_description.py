import logging

logger = logging.getLogger(__name__)


def handoff_description() -> str:
    return """Convert an email to HTML and send it"""

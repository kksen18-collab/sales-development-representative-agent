import logging

import sendgrid

logger = logging.getLogger(__name__)


class SendGridClient:
    def __init__(self, sendgrid_api_key: str, from_email: str, to_email: str):
        self.sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
        self.from_email = from_email
        self.to_email = to_email

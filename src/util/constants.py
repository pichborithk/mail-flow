import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Constants:
    NAME: str = "name"
    EMAIL: str = "email"
    SUBJECT: str = "subject"
    CONTENT: str = "content"
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    MY_EMAIL = os.getenv("MY_EMAIL")
    PERSONAL_SITE_URL = os.getenv("PERSONAL_SITE_URL")


NAME = Constants.NAME
EMAIL = Constants.EMAIL
SUBJECT = Constants.SUBJECT
CONTENT = Constants.CONTENT
SENDER_EMAIL = Constants.SENDER_EMAIL
SENDER_PASSWORD = Constants.SENDER_PASSWORD
MY_EMAIL = Constants.MY_EMAIL
PERSONAL_SITE_URL = Constants.PERSONAL_SITE_URL

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SMSTemplate", "Settings"]


class Settings(BaseModel):
    payload_overrides: Optional[str] = None
    """A JSON object that overrides the payload sent to the SMS provider."""

    to_number: Optional[str] = None
    """An override for the phone number to send the SMS to.

    When not set, defaults to `recipient.phone_number`.
    """


class SMSTemplate(BaseModel):
    text_body: str
    """The message of the SMS."""

    settings: Optional[Settings] = None
    """
    The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides)
    for the SMS template.
    """

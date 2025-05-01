# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SMSTemplateParam", "Settings"]


class Settings(TypedDict, total=False):
    payload_overrides: Optional[str]
    """A JSON object that overrides the payload sent to the SMS provider."""

    to_number: Optional[str]
    """An override for the phone number to send the SMS to.

    When not set, defaults to `recipient.phone_number`.
    """


class SMSTemplateParam(TypedDict, total=False):
    text_body: Required[str]
    """The message of the SMS."""

    settings: Optional[Settings]
    """
    The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides)
    for the SMS template.
    """

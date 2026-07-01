# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PushTemplate", "Settings"]


class Settings(BaseModel):
    """
    The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides) for the push template.
    """

    delivery_type: Literal["silent", "content"]
    """The delivery type of the push notification.

    Set as silent to send a data-only notification. When set to `silent`, no body
    will be sent.
    """

    payload_overrides: Optional[str] = None
    """A JSON object that overrides the payload sent to the push provider."""


class PushTemplate(BaseModel):
    """A push notification template."""

    settings: Settings
    """
    The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides)
    for the push template.
    """

    text_body: str
    """The body of the push notification."""

    title: str
    """The title of the push notification."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PushTemplate", "Settings"]


class Settings(BaseModel):
    delivery_type: Optional[Literal["silent", "content"]] = None
    """The delivery type of the push notification.

    Defaults to `content`. Set as silent to send a data-only notification. When set
    to `data`, no body will be sent.
    """

    payload_overrides: Optional[str] = None
    """A JSON object that overrides the payload sent to the push provider."""


class PushTemplate(BaseModel):
    text_body: str
    """The body of the push notification."""

    title: str
    """The title of the push notification."""

    settings: Optional[Settings] = None
    """
    The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides)
    for the push template. Can be omitted.
    """

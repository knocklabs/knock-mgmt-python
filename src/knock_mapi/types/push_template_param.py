# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PushTemplateParam", "Settings"]


class Settings(TypedDict, total=False):
    delivery_type: Literal["silent", "content"]
    """The delivery type of the push notification.

    Defaults to `content`. Set as silent to send a data-only notification. When set
    to `data`, no body will be sent.
    """

    payload_overrides: str
    """A JSON object that overrides the payload sent to the push provider."""


class PushTemplateParam(TypedDict, total=False):
    text_body: Required[str]
    """The body of the push notification."""

    title: Required[str]
    """The title of the push notification."""

    settings: Optional[Settings]
    """
    The [settings](https://docs.knock.app/integrations/sms/settings-and-overrides)
    for the push template. Can be omitted.
    """

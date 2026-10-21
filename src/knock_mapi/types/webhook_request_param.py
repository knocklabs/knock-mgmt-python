# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookRequestParam"]


class WebhookRequestParam(TypedDict, total=False):
    """The request body for creating or updating an outbound webhook."""

    event_types: Required[SequenceNotStr[str]]
    """
    The list of event types that this webhook should be subscribed to, in dotted
    format (e.g. `message.sent`).
    """

    url: Required[str]
    """The URL that the webhook will send events to."""

    active: Optional[bool]
    """Whether the webhook should be active."""

    description: Optional[str]
    """An optional description of the webhook."""

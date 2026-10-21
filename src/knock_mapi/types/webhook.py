# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """An outbound webhook that receives event notifications."""

    id: str
    """The unique identifier for the webhook."""

    active: bool
    """Whether the webhook is currently active."""

    created_at: datetime
    """The timestamp of when the webhook was created."""

    event_types: List[str]
    """
    The list of event types that this webhook is subscribed to, in dotted format
    (e.g. `message.sent`).
    """

    updated_at: datetime
    """The timestamp of when the webhook was last updated."""

    url: str
    """The URL that the webhook will send events to."""

    description: Optional[str] = None
    """An optional description of the webhook."""

    secret_key: Optional[str] = None
    """The secret key used to sign webhook payloads.

    Only returned when a webhook is first created.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Channel"]


class Channel(BaseModel):
    id: str
    """The unique identifier for the channel."""

    created_at: datetime
    """The timestamp of when the channel was created."""

    key: str
    """Unique identifier for the channel within a project (immutable once created)."""

    name: str
    """The human-readable name of the channel."""

    provider: str
    """The ID of the provider that this channel uses to deliver messages.

    Learn more about the providers available
    [in our documentation](https://docs.knock.app/integrations/overview).
    """

    type: Literal["email", "in_app", "in_app_feed", "in_app_guide", "sms", "push", "chat", "http"]
    """The type of channel, determining what kind of messages it can send."""

    updated_at: datetime
    """The timestamp of when the channel was last updated."""

    archived_at: Optional[datetime] = None
    """The timestamp of when the channel was deleted."""

    custom_icon_url: Optional[str] = None
    """Optional URL to a custom icon for the channel.

    Only used for display purposes in the dashboard.
    """

    description: Optional[str] = None
    """Optional description of the channel's purpose or usage."""

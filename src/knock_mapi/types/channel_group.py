# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .channel_group_rule import ChannelGroupRule

__all__ = ["ChannelGroup"]


class ChannelGroup(BaseModel):
    """A group of channels with rules for when they are applicable."""

    channel_rules: List[ChannelGroupRule]
    """Rules for determining which channels should be used."""

    channel_type: Literal["email", "in_app", "in_app_feed", "in_app_guide", "sms", "push", "chat", "http"]
    """The type of channels contained in this group."""

    created_at: datetime
    """The timestamp of when the channel group was created."""

    key: str
    """Unique identifier for the channel group within a project."""

    name: str
    """The human-readable name of the channel group."""

    operator: Literal["any", "all"]
    """
    Determines how the channel rules are applied ('any' means any rule can match,
    'all' means all rules must match).
    """

    source: Literal["system", "user"]
    """Whether this channel group was created by the system or a user.

    Only user created channel groups can be modified.
    """

    updated_at: datetime
    """The timestamp of when the channel group was last updated."""

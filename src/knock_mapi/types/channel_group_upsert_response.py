# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .channel_group import ChannelGroup

__all__ = ["ChannelGroupUpsertResponse"]


class ChannelGroupUpsertResponse(BaseModel):
    """Wraps the ChannelGroup response under the `channel_group` key."""

    channel_group: ChannelGroup
    """A group of channels with rules for when they are applicable."""

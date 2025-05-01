# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InAppFeedChannelSettings"]


class InAppFeedChannelSettings(BaseModel):
    link_tracking: Optional[bool] = None
    """Whether to track link clicks on in-app feed notifications."""

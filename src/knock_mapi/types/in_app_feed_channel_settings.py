# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InAppFeedChannelSettings"]


class InAppFeedChannelSettings(BaseModel):
    """In-app feed channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    link_tracking: Optional[bool] = None
    """Whether to track link clicks on in-app feed notifications."""

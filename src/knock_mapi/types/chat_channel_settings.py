# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatChannelSettings"]


class ChatChannelSettings(BaseModel):
    email_based_user_id_resolution: Optional[bool] = None
    """Whether to resolve chat provider user IDs using a Knock user's email address.

    Only relevant for Slack channels for the time being.
    """

    link_tracking: Optional[bool] = None
    """Whether to track link clicks on chat notifications."""

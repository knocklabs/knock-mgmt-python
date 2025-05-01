# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SMSChannelSettings"]


class SMSChannelSettings(BaseModel):
    link_tracking: Optional[bool] = None
    """Whether to track link clicks on SMS notifications."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PushChannelSettings"]


class PushChannelSettings(BaseModel):
    token_deregistration: Optional[bool] = None
    """Whether to deregister a push-token when a push send hard bounces.

    This is to prevent the same token from being used for future pushes.
    """

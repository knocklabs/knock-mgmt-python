# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PushChannelSettingsParam"]


class PushChannelSettingsParam(TypedDict, total=False):
    token_deregistration: bool
    """Whether to deregister a push-token when a push send hard bounces.

    This is to prevent the same token from being used for future pushes.
    """

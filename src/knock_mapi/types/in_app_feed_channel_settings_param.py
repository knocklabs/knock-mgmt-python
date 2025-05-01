# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InAppFeedChannelSettingsParam"]


class InAppFeedChannelSettingsParam(TypedDict, total=False):
    link_tracking: bool
    """Whether to track link clicks on in-app feed notifications."""

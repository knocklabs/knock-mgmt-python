# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChatChannelSettingsParam"]


class ChatChannelSettingsParam(TypedDict, total=False):
    """Chat channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    email_based_user_id_resolution: bool
    """Whether to resolve chat provider user IDs using a Knock user's email address.

    Only relevant for Slack channels for the time being.
    """

    link_tracking: bool
    """Whether to track link clicks on chat notifications."""

    link_tracking_uses_short_links: bool
    """
    Whether tracked chat links should use compact short URLs instead of long tracked
    links. Only applied when link tracking is enabled. Not used by WhatsApp, which
    already uses short links.
    """

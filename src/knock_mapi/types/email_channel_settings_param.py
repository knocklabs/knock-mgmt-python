# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EmailChannelSettingsParam"]


class EmailChannelSettingsParam(TypedDict, total=False):
    bcc_address: Optional[str]
    """The BCC address on email notifications. Supports liquid."""

    cc_address: Optional[str]
    """The CC address on email notifications. Supports liquid."""

    from_address: Optional[str]
    """The email address from which this channel will send. Supports liquid."""

    from_name: Optional[str]
    """The name from which this channel will send. Supports liquid."""

    json_overrides: Optional[str]
    """
    A JSON template for any custom overrides to merge into the API payload that is
    sent to the email provider. Supports liquid.
    """

    link_tracking: bool
    """Whether to track link clicks on email notifications."""

    open_tracking: bool
    """Whether to track opens on email notifications."""

    reply_to_address: Optional[str]
    """The Reply-to address on email notifications. Supports liquid."""

    to_address: str
    """The email address to which this channel will send.

    Defaults to `recipient.email`. Supports liquid.
    """

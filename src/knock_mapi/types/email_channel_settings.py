# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EmailChannelSettings"]


class EmailChannelSettings(BaseModel):
    """Email channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    bcc_address: Optional[str] = None
    """The BCC address on email notifications. Supports liquid."""

    cc_address: Optional[str] = None
    """The CC address on email notifications. Supports liquid."""

    from_address: Optional[str] = None
    """The email address from which this channel will send. Supports liquid."""

    from_name: Optional[str] = None
    """The name from which this channel will send. Supports liquid."""

    json_overrides: Optional[str] = None
    """
    A JSON template for any custom overrides to merge into the API payload that is
    sent to the email provider. Supports liquid.
    """

    link_tracking: Optional[bool] = None
    """Whether to track link clicks on email notifications."""

    open_tracking: Optional[bool] = None
    """Whether to track opens on email notifications."""

    reply_to_address: Optional[str] = None
    """The Reply-to address on email notifications. Supports liquid."""

    to_address: Optional[str] = None
    """The email address to which this channel will send.

    Defaults to `recipient.email`. Supports liquid.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["HeadlessAccountClaimResponse"]


class HeadlessAccountClaimResponse(BaseModel):
    """A claim an agent started for a person, with the link and code to show them."""

    claim_url: str
    """
    The dashboard link the person opens and signs in with the email given when the
    claim started.
    """

    expires_at: datetime
    """When the link and code stop working."""

    user_code: str
    """A six-digit code to show the person, who types it on the claim page.

    Show it separately from the link.
    """

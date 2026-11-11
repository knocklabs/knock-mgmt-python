# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HeadlessAccountRetrieveStatusResponse"]


class HeadlessAccountRetrieveStatusResponse(BaseModel):
    """Where a headless account stands, from the point of view of the agent."""

    expires_at: Optional[datetime] = None
    """When an unclaimed account is deleted, or null once it has been claimed."""

    status: Literal["provisioning", "unclaimed", "claimed", "expired"]
    """
    Whether the account is still being set up, waiting to be claimed, claimed by a
    person, or expired because its claim window closed or its setup never finished.
    """

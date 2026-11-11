# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HeadlessAccountCreateResponse"]


class HeadlessAccountCreateResponse(BaseModel):
    """
    A headless account an agent created, with the service token the agent uses to work in it.
    """

    token: str
    """A service token for the Management API.

    It is only returned once and keeps working after a person claims the account.
    """

    expires_at: datetime
    """
    When the account and its token are deleted unless a person claims the account
    first.
    """

    status: Literal["provisioning"]
    """The account is still being set up. Poll the status endpoint."""

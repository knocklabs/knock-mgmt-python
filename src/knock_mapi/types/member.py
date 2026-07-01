# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .member_user import MemberUser

__all__ = ["Member"]


class Member(BaseModel):
    """A member of the account."""

    id: str
    """The unique identifier of the member."""

    created_at: datetime
    """The timestamp of when the member joined the account."""

    role: Literal["owner", "admin", "member", "production_only_member", "billing", "support"]
    """The member's role in the account."""

    updated_at: datetime
    """The timestamp of when the member was last updated."""

    user: MemberUser
    """Information about a user within the Knock dashboard.

    Not to be confused with an external user (recipient) of a workflow.
    """

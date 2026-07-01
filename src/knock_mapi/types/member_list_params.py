# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    email: str
    """Filter members by email address (exact match)."""

    limit: int
    """The number of entries to fetch per-page."""

    role: str
    """Filter members by role.

    One of: owner, admin, member, production_only_member, billing, support.
    """

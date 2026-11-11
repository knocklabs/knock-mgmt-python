# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HeadlessAccountClaimParams"]


class HeadlessAccountClaimParams(TypedDict, total=False):
    email: Required[str]
    """The email of the person who will own the account.

    Only they can finish the claim.
    """

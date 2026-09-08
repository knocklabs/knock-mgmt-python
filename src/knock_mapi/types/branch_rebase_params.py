# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BranchRebaseParams"]


class BranchRebaseParams(TypedDict, total=False):
    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

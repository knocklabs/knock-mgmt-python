# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VariableListParams"]


class VariableListParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    limit: int
    """The number of entries to fetch per-page."""

    type: Literal["public", "secret"]
    """Filter variables by type. Supports 'public' or 'secret'."""

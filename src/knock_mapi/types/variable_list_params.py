# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VariableListParams"]


class VariableListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug.

    When omitted, the account's default environment is used for authorization while
    the response remains project-scoped.
    """

    limit: int
    """The number of entries to fetch per-page."""

    type: Literal["public", "secret"]
    """Filter variables by type. Supports 'public' or 'secret'."""

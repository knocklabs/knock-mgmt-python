# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SchemaListParams"]


class SchemaListParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    item_type: str
    """Filter schemas by item type (`user`, `tenant`, or `object`)."""

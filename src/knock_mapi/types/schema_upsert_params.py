# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SchemaUpsertParams"]


class SchemaUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    collection: str
    """The object collection, required when `item_type` is `object`."""

    body: object

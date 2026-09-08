# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SchemaValidateParams"]


class SchemaValidateParams(TypedDict, total=False):
    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    collection: str
    """The object collection, required when `item_type` is `object`."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    body: object

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .partial_request_param import PartialRequestParam

__all__ = ["PartialValidateParams"]


class PartialValidateParams(TypedDict, total=False):
    partial: Required[PartialRequestParam]
    """A partial object with attributes to update or create a partial."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

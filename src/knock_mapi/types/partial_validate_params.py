# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .partial_request_param import PartialRequestParam

__all__ = ["PartialValidateParams"]


class PartialValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    partial: Required[PartialRequestParam]
    """A partial object with attributes to update or create a partial."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

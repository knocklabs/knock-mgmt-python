# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .reusable_request_request_param import ReusableRequestRequestParam

__all__ = ["ReusableRequestValidateParams"]


class ReusableRequestValidateParams(TypedDict, total=False):
    reusable_request: Required[ReusableRequestRequestParam]
    """
    A reusable request object with attributes to update or create a reusable
    request.
    """

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

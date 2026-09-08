# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .guide_request_param import GuideRequestParam

__all__ = ["GuideValidateParams"]


class GuideValidateParams(TypedDict, total=False):
    guide: Required[GuideRequestParam]
    """A request to create or update a guide."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

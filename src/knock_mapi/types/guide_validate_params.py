# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .guide_request_param import GuideRequestParam

__all__ = ["GuideValidateParams"]


class GuideValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    guide: Required[GuideRequestParam]
    """A request to create or update a guide."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

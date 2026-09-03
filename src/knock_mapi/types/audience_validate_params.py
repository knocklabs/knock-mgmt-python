# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .audience_request_param import AudienceRequestParam

__all__ = ["AudienceValidateParams"]


class AudienceValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    audience: Required[AudienceRequestParam]
    """An audience object with attributes to create or update an audience.

    Use `type: static` for audiences with explicitly managed members, or
    `type: dynamic` for audiences with segment-based membership.
    """

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

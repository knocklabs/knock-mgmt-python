# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .audience_request_param import AudienceRequestParam

__all__ = ["AudienceValidateParams"]


class AudienceValidateParams(TypedDict, total=False):
    audience: Required[AudienceRequestParam]
    """An audience object with attributes to create or update an audience.

    Use `type: static` for audiences with explicitly managed members, or
    `type: dynamic` for audiences with segment-based membership.
    """

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

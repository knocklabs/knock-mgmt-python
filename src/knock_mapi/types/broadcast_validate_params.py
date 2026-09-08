# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BroadcastValidateParams"]


class BroadcastValidateParams(TypedDict, total=False):
    broadcast: Required["BroadcastRequestParam"]
    """A broadcast request for upserting a broadcast."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""


from .broadcast_request_param import BroadcastRequestParam

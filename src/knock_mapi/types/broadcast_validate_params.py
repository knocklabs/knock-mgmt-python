# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BroadcastValidateParams"]


class BroadcastValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    broadcast: Required["BroadcastRequestParam"]
    """A broadcast request for upserting a broadcast."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """


from .broadcast_request_param import BroadcastRequestParam

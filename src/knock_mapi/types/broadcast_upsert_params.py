# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BroadcastUpsertParams"]


class BroadcastUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    broadcast: Required["BroadcastRequestParam"]
    """A broadcast request for upserting a broadcast."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """


from .broadcast_request_param import BroadcastRequestParam

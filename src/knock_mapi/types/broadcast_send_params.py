# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BroadcastSendParams"]


class BroadcastSendParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When to send the broadcast.

    If provided, the broadcast will be scheduled to send at this time. Must be in
    ISO 8601 UTC format. If not provided, the broadcast will be sent immediately.
    """

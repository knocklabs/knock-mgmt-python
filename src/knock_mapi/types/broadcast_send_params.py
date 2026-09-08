# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BroadcastSendParams"]


class BroadcastSendParams(TypedDict, total=False):
    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When to send the broadcast.

    If provided, the broadcast will be scheduled to send at this time. Must be in
    ISO 8601 UTC format. If not provided, the broadcast will be sent immediately.
    """

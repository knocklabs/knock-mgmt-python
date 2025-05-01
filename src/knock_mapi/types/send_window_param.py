# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SendWindowParam"]

_SendWindowParamReservedKeywords = TypedDict(
    "_SendWindowParamReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class SendWindowParam(_SendWindowParamReservedKeywords, total=False):
    day: Required[Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]]
    """The day of the week."""

    type: Required[Literal["send", "do_not_send"]]
    """The type of send window."""

    until: Optional[str]
    """The end time of the send window."""

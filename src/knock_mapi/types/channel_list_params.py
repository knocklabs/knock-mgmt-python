# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ChannelListParams"]


class ChannelListParams(TypedDict, total=False):
    id: str
    """A channel id to filter the results by."""

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["environment_settings"]]
    """Associated resources to include in the response.

    Accepts `environment_settings` to include per-environment channel configuration.
    """

    limit: int
    """The number of entries to fetch per-page."""

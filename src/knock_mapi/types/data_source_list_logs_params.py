# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataSourceListLogsParams"]


class DataSourceListLogsParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    id: str
    """The log ID to filter by."""

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    date: str
    """Returns event logs that were produced on this date."""

    ending_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return source logs at or before this timestamp."""

    event: str
    """The event name to filter by."""

    include: List[Literal["actions"]]
    """Associated resources to include in the response.

    Accepts `actions` to include the actions executed after receiving each source
    event.
    """

    limit: int
    """The number of entries to fetch per-page."""

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return source logs at or after this timestamp."""

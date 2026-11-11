# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WarehouseSyncSourceParam"]


class WarehouseSyncSourceParam(TypedDict, total=False):
    """
    The rows a warehouse sync reads: a table or view (`relation`), or the result of a SQL query (`sql`).
    """

    mode: Required[Literal["relation", "sql"]]
    """Whether the sync reads a table or view, or a SQL query."""

    name: Optional[str]
    """The name of the table or view. Required when `mode` is `relation`."""

    query: Optional[str]
    """The SQL query to read. Required when `mode` is `sql`."""

    schema: Optional[str]
    """The schema of the table or view. Required when `mode` is `relation`."""

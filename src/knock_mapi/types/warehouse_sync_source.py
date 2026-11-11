# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WarehouseSyncSource"]


class WarehouseSyncSource(BaseModel):
    """
    The rows a warehouse sync reads: a table or view (`relation`), or the result of a SQL query (`sql`).
    """

    mode: Literal["relation", "sql"]
    """Whether the sync reads a table or view, or a SQL query."""

    name: Optional[str] = None
    """The name of the table or view. Required when `mode` is `relation`."""

    query: Optional[str] = None
    """The SQL query to read. Required when `mode` is `sql`."""

    schema_: Optional[str] = FieldInfo(alias="schema", default=None)
    """The schema of the table or view. Required when `mode` is `relation`."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WarehouseSyncMappingParam"]


class WarehouseSyncMappingParam(TypedDict, total=False):
    """Maps one column from the warehouse to one field in Knock."""

    source_column: Required[str]
    """The column to read.

    Can be a dotted path into an object column, such as `PROPERTIES.plan`.
    """

    target_field: Required[str]
    """The Knock field to write the value to."""

    on_null: Literal["set_null", "preserve"]
    """What to do when the column is `NULL`.

    `set_null` clears the Knock field, and `preserve` keeps its current value.
    """

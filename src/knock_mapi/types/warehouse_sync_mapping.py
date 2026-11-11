# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WarehouseSyncMapping"]


class WarehouseSyncMapping(BaseModel):
    """Maps one column from the warehouse to one field in Knock."""

    source_column: str
    """The column to read.

    Can be a dotted path into an object column, such as `PROPERTIES.plan`.
    """

    target_field: str
    """The Knock field to write the value to."""

    on_null: Optional[Literal["set_null", "preserve"]] = None
    """What to do when the column is `NULL`.

    `set_null` clears the Knock field, and `preserve` keeps its current value.
    """

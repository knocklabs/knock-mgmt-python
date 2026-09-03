# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .item_schema import ItemSchema
from .shared.page_info import PageInfo

__all__ = ["SchemaListResponse"]


class SchemaListResponse(BaseModel):
    """A paginated list of ItemSchema.

    Contains a list of entries and page information.
    """

    entries: List[ItemSchema]
    """A list of entries."""

    page_info: PageInfo
    """The information about a paginated result."""

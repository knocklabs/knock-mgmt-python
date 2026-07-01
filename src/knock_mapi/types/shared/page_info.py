# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PageInfo"]


class PageInfo(BaseModel):
    """The information about a paginated result."""

    page_size: int
    """The number of entries to fetch per-page."""

    after: Optional[str] = None
    """The cursor to fetch entries after.

    Will only be present if there are more entries to fetch.
    """

    before: Optional[str] = None
    """The cursor to fetch entries before.

    Will only be present if there are more entries to fetch before the current page.
    """

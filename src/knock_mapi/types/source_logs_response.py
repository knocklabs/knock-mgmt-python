# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .source_log import SourceLog
from .shared.page_info import PageInfo

__all__ = ["SourceLogsResponse"]


class SourceLogsResponse(BaseModel):
    """A paginated list of source logs.

    Include `actions` in the `include` query parameter to return action details for each log.
    """

    entries: List[SourceLog]
    """The source logs for the requested source and environment."""

    page_info: PageInfo
    """The information about a paginated result."""

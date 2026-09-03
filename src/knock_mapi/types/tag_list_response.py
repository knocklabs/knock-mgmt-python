# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .tag import Tag
from .._models import BaseModel

__all__ = ["TagListResponse"]


class TagListResponse(BaseModel):
    """A list of tags in the project's catalog."""

    entries: List[Tag]
    """Tags, ordered by name."""

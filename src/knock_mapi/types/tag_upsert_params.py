# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TagUpsertParams", "Tag"]


class TagUpsertParams(TypedDict, total=False):
    tag: Required[Tag]
    """A request to create or update a tag.

    The tag name is taken from the path. On conflict, omitted description and color
    fields are set to null.
    """


class Tag(TypedDict, total=False):
    """A request to create or update a tag.

    The tag name is taken from the path. On conflict, omitted description and color fields are set to null.
    """

    color: Optional[str]
    """An optional hex color for the tag (e.g. #3B82F6)."""

    description: Optional[str]
    """An optional description of the tag."""

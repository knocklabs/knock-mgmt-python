# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .tag import Tag
from .._models import BaseModel

__all__ = ["TagUpsertResponse"]


class TagUpsertResponse(BaseModel):
    """Wraps the Tag response under the `tag` key."""

    tag: Tag
    """A named tag in a project's resource-tag catalog."""

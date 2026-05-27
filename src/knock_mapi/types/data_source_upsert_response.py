# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .source import Source
from .._models import BaseModel

__all__ = ["DataSourceUpsertResponse"]


class DataSourceUpsertResponse(BaseModel):
    """Wraps the Source response under the `source` key."""

    source: Source
    """A source that receives external events and maps them to Knock actions."""

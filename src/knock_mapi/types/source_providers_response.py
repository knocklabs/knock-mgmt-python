# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["SourceProvidersResponse", "Entry", "EntryProvider"]


class EntryProvider(BaseModel):
    """Provider display metadata."""

    description: str
    """Provider display description."""

    name: str
    """Provider display name."""


class Entry(BaseModel):
    """A source provider summary."""

    key: str
    """Provider key."""

    provider: EntryProvider
    """Provider display metadata."""

    version: str
    """Provider version."""


class SourceProvidersResponse(BaseModel):
    """Source providers available for creating sources."""

    entries: List[Entry]
    """Source providers."""

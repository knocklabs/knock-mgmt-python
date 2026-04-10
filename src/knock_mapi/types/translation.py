# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Translation"]


class Translation(BaseModel):
    """A translation object."""

    content: str
    """
    A JSON encoded string containing the key-value pairs of translation references
    and translation strings.
    """

    format: Literal["json", "po"]
    """
    Indicates whether content is a JSON encoded object string or a string in the PO
    format.
    """

    inserted_at: datetime
    """The timestamp of when the translation was created."""

    locale_code: str
    """The locale code for the translation object."""

    namespace: str
    """An optional namespace for the translation to help categorize your translations."""

    updated_at: datetime
    """The timestamp of when the translation was last updated."""

    tenant: Optional[str] = None
    """An optional tenant identifier to scope the translation to a specific tenant."""

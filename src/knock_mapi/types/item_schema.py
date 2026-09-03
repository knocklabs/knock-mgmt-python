# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ItemSchema", "Property"]


class Property(BaseModel):
    """A property definition within an item schema."""

    key: str
    """The property key."""

    description: Optional[str] = None
    """The description of the property."""

    item_type: Optional[str] = None
    """The referenced item type when the property stores an item reference."""

    preview_text: Optional[str] = None
    """The property preview text."""

    type: Optional[str] = None
    """The primitive or referenced item type for the property."""

    visible: Optional[bool] = None
    """Whether the property is visible in the schema management UI."""


class ItemSchema(BaseModel):
    """A managed schema configuration for users, tenants, or objects."""

    item_type: Literal["user", "tenant", "object"]
    """The item type the schema applies to."""

    properties: List[Property]
    """The managed properties for the schema."""

    item_id: Optional[str] = None
    """The object collection key. Only present for object schemas."""

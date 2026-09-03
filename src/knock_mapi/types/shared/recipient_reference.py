# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["RecipientReference", "ObjectRecipientReference"]


class ObjectRecipientReference(BaseModel):
    """An object reference."""

    id: str
    """The ID of the object."""

    collection: str
    """The collection of the object."""


RecipientReference: TypeAlias = Union[str, ObjectRecipientReference]

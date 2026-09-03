# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["RecipientReference", "ObjectRecipientReference"]


class ObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


RecipientReference: TypeAlias = Union[str, ObjectRecipientReference]

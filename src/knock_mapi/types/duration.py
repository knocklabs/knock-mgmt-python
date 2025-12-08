# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Duration"]


class Duration(BaseModel):
    """A duration of time, represented as a unit and a value."""

    unit: Literal["minutes", "hours", "days", "weeks", "months"]
    """The unit of time."""

    value: int
    """The value of the duration."""

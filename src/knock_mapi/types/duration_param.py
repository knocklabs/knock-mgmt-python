# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DurationParam"]


class DurationParam(TypedDict, total=False):
    """A duration of time, represented as a unit and a value."""

    unit: Required[Literal["minutes", "hours", "days", "weeks", "months"]]
    """The unit of time."""

    value: Required[int]
    """The value of the duration."""

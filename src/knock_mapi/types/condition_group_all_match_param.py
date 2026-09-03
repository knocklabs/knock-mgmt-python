# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .condition_param import ConditionParam

__all__ = ["ConditionGroupAllMatchParam"]


class ConditionGroupAllMatchParam(TypedDict, total=False):
    """A group of conditions that must all be met."""

    all: Iterable[ConditionParam]
    """A list of conditions."""

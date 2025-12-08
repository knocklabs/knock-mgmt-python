# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .condition_param import ConditionParam

__all__ = [
    "ConditionGroupParam",
    "ConditionGroupAllMatch",
    "ConditionGroupAnyMatch",
    "ConditionGroupAnyMatchAny",
    "ConditionGroupAnyMatchAnyConditionGroupAllMatch",
]


class ConditionGroupAllMatch(TypedDict, total=False):
    """A group of conditions that must all be met."""

    all: Iterable[ConditionParam]
    """A list of conditions."""


class ConditionGroupAnyMatchAnyConditionGroupAllMatch(TypedDict, total=False):
    """A group of conditions that must all be met."""

    all: Iterable[ConditionParam]
    """A list of conditions."""


ConditionGroupAnyMatchAny: TypeAlias = Union[ConditionParam, ConditionGroupAnyMatchAnyConditionGroupAllMatch]


class ConditionGroupAnyMatch(TypedDict, total=False):
    """A group of conditions that any must be met. Can contain nested alls."""

    any: Iterable[ConditionGroupAnyMatchAny]
    """An array of conditions or nested condition groups to evaluate."""


ConditionGroupParam: TypeAlias = Union[ConditionGroupAllMatch, ConditionGroupAnyMatch]

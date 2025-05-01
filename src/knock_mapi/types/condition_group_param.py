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
    all: Iterable[ConditionParam]
    """A list of conditions."""


class ConditionGroupAnyMatchAnyConditionGroupAllMatch(TypedDict, total=False):
    all: Iterable[ConditionParam]
    """A list of conditions."""


ConditionGroupAnyMatchAny: TypeAlias = Union[ConditionParam, ConditionGroupAnyMatchAnyConditionGroupAllMatch]


class ConditionGroupAnyMatch(TypedDict, total=False):
    any: Iterable[ConditionGroupAnyMatchAny]
    """An array of conditions or nested condition groups to evaluate."""


ConditionGroupParam: TypeAlias = Union[ConditionGroupAllMatch, ConditionGroupAnyMatch]

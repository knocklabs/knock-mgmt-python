# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .condition_param import ConditionParam
from .condition_group_all_match_param import ConditionGroupAllMatchParam

__all__ = ["ConditionGroupParam", "ConditionGroupAnyMatch", "ConditionGroupAnyMatchAny"]

ConditionGroupAnyMatchAny: TypeAlias = Union[ConditionParam, ConditionGroupAllMatchParam]


class ConditionGroupAnyMatch(TypedDict, total=False):
    """A group of conditions that any must be met. Can contain nested alls."""

    any: Iterable[ConditionGroupAnyMatchAny]
    """An array of conditions or nested condition groups to evaluate."""


ConditionGroupParam: TypeAlias = Union[ConditionGroupAllMatchParam, ConditionGroupAnyMatch]

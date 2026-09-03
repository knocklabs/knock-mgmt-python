# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .condition import Condition
from .condition_group_all_match import ConditionGroupAllMatch

__all__ = ["ConditionGroup", "ConditionGroupAnyMatch", "ConditionGroupAnyMatchAny"]

ConditionGroupAnyMatchAny: TypeAlias = Union[Condition, ConditionGroupAllMatch]


class ConditionGroupAnyMatch(BaseModel):
    """A group of conditions that any must be met. Can contain nested alls."""

    any: Optional[List[ConditionGroupAnyMatchAny]] = None
    """An array of conditions or nested condition groups to evaluate."""


ConditionGroup: TypeAlias = Union[ConditionGroupAllMatch, ConditionGroupAnyMatch]

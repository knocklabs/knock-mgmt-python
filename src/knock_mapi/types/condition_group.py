# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .condition import Condition

__all__ = [
    "ConditionGroup",
    "ConditionGroupAllMatch",
    "ConditionGroupAnyMatch",
    "ConditionGroupAnyMatchAny",
    "ConditionGroupAnyMatchAnyConditionGroupAllMatch",
]


class ConditionGroupAllMatch(BaseModel):
    all: Optional[List[Condition]] = None
    """A list of conditions."""


class ConditionGroupAnyMatchAnyConditionGroupAllMatch(BaseModel):
    all: Optional[List[Condition]] = None
    """A list of conditions."""


ConditionGroupAnyMatchAny: TypeAlias = Union[Condition, ConditionGroupAnyMatchAnyConditionGroupAllMatch]


class ConditionGroupAnyMatch(BaseModel):
    any: Optional[List[ConditionGroupAnyMatchAny]] = None
    """An array of conditions or nested condition groups to evaluate."""


ConditionGroup: TypeAlias = Union[ConditionGroupAllMatch, ConditionGroupAnyMatch]

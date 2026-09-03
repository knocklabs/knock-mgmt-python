# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .condition import Condition

__all__ = ["ConditionGroupAllMatch"]


class ConditionGroupAllMatch(BaseModel):
    """A group of conditions that must all be met."""

    all: Optional[List[Condition]] = None
    """A list of conditions."""

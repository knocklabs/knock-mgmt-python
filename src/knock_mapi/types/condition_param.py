# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConditionParam"]


class ConditionParam(TypedDict, total=False):
    """A condition to be evaluated."""

    operator: Required[
        Literal[
            "equal_to",
            "not_equal_to",
            "greater_than",
            "less_than",
            "greater_than_or_equal_to",
            "less_than_or_equal_to",
            "contains",
            "not_contains",
            "contains_all",
            "not_contains_all",
            "is_timestamp_before",
            "is_timestamp_after",
            "is_timestamp_between",
            "empty",
            "not_empty",
            "is_timestamp",
            "is_audience_member",
            "is_not_audience_member",
        ]
    ]
    """The operator to use in the evaluation of the condition."""

    variable: Required[str]
    """The variable to be evaluated.

    Variables can be either static values or dynamic properties. Static values will
    always be JSON decoded so will support strings, lists, objects, numbers, and
    booleans. Dynamic values should be path expressions.
    """

    argument: Optional[str]
    """The argument to be evaluated.

    Arguments can be either static values or dynamic properties. Static values will
    always be JSON decoded so will support strings, lists, objects, numbers, and
    booleans. Dynamic values should be path expressions.
    """

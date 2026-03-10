# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AudienceCondition"]


class AudienceCondition(BaseModel):
    """A condition to evaluate for audience membership."""

    operator: Literal[
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
        "is_timestamp_on_or_after",
        "is_timestamp_between",
        "empty",
        "not_empty",
        "exists",
        "not_exists",
        "is_timestamp",
        "is_audience_member",
        "is_not_audience_member",
    ]
    """The operator to use when evaluating the condition."""

    property: str
    """The property to be evaluated.

    Properties are dynamic values using path expressions like `recipient.plan` or
    `recipient.created_at`.
    """

    argument: Optional[str] = None
    """The argument to compare against.

    Can be a static value (string, number, boolean) or a dynamic path expression.
    """

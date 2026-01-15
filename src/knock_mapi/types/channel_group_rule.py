# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .channel import Channel
from .._models import BaseModel

__all__ = ["ChannelGroupRule"]


class ChannelGroupRule(BaseModel):
    """
    A rule that determines if a channel should be executed as part of a channel group.
    """

    channel: Channel
    """A configured channel, which is a way to route messages to a provider."""

    created_at: datetime
    """The timestamp of when the rule was created."""

    index: int
    """The order index of this rule within the channel group."""

    rule_type: Literal["if", "unless", "always"]
    """
    The type of rule (if = conditional, unless = negative conditional, always =
    always apply).
    """

    updated_at: datetime
    """The timestamp of when the rule was last updated."""

    argument: Optional[str] = None
    """For conditional rules, the value to compare against."""

    operator: Optional[
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
            "is_timestamp_before_date",
            "is_timestamp_after_date",
            "is_timestamp_between",
            "empty",
            "not_empty",
            "is_timestamp",
            "is_audience_member",
            "is_not_audience_member",
        ]
    ] = None
    """For conditional rules, the operator to apply."""

    variable: Optional[str] = None
    """For conditional rules, the variable to evaluate."""

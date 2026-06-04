# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChannelGroupUpsertParams", "ChannelGroup", "ChannelGroupChannelRule"]


class ChannelGroupUpsertParams(TypedDict, total=False):
    channel_group: Required[ChannelGroup]
    """A request to create or update a channel group."""


class ChannelGroupChannelRule(TypedDict, total=False):
    """
    A rule that determines if a channel should be executed as part of a channel group.
    """

    channel_key: Required[str]
    """The key of the channel this rule applies to."""

    rule_type: Required[Literal["if", "unless", "always"]]
    """
    The type of rule (if = conditional, unless = negative conditional, always =
    always apply).
    """

    argument: Optional[str]
    """For conditional rules, the value to compare against."""

    index: int
    """The order index of this rule within the channel group."""

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
            "is_timestamp_on_or_after",
            "is_timestamp_between",
            "is_between",
            "empty",
            "not_empty",
            "exists",
            "not_exists",
            "is_timestamp",
            "is_audience_member",
            "is_not_audience_member",
        ]
    ]
    """For conditional rules, the operator to apply."""

    variable: Optional[str]
    """For conditional rules, the variable to evaluate."""


class ChannelGroup(TypedDict, total=False):
    """A request to create or update a channel group."""

    channel_type: Required[Literal["email", "in_app", "in_app_feed", "in_app_guide", "sms", "push", "chat", "http"]]
    """The type of channels contained in this group."""

    name: Required[str]
    """The human-readable name of the channel group."""

    channel_rules: Iterable[ChannelGroupChannelRule]
    """Rules for determining which channels should be used."""

    operator: Literal["any", "all"]
    """
    Determines how the channel rules are applied ('any' means any rule can match,
    'all' means all rules must match). Defaults to 'any'.
    """

    visible_in: List[Literal["workflow", "broadcast"]]
    """Optional.

    Where the channel group is visible as a step destination. Defaults to both
    workflow and broadcast when creating; omitted on update preserves the existing
    value.
    """

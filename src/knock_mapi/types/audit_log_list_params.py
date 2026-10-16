# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    action: Union[str, SequenceNotStr[str]]
    """Filter by action. Accepts one action or an array of actions, matched exactly."""

    actor_id: Union[str, SequenceNotStr[str]]
    """Filter by the id of the user who performed the action.

    Accepts one id or an array of ids.
    """

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    environment: str
    """The environment slug.

    When omitted, the list is account-wide and does not use the account's default
    environment. When set, limits entries to that environment or branch and omits
    account-level entries.
    """

    limit: int
    """The number of entries to fetch per-page."""

    resource_type: Union[
        Literal[
            "account",
            "account_user",
            "api_key",
            "asset",
            "audience",
            "broadcast",
            "channel",
            "channel_group",
            "email_layout",
            "environment",
            "environment_defaults",
            "event_action_mapping",
            "external_audience",
            "goal",
            "guide",
            "guide_group",
            "invite",
            "member",
            "message_type",
            "object",
            "partial",
            "permission_group",
            "preference_category",
            "preference_center",
            "preference_center_domain",
            "reusable_request",
            "service_token",
            "signing_key",
            "source",
            "subscription",
            "tag",
            "translation",
            "user",
            "variable",
            "view",
            "webhook",
            "workflow",
        ],
        List[
            Literal[
                "account",
                "account_user",
                "api_key",
                "asset",
                "audience",
                "broadcast",
                "channel",
                "channel_group",
                "email_layout",
                "environment",
                "environment_defaults",
                "event_action_mapping",
                "external_audience",
                "goal",
                "guide",
                "guide_group",
                "invite",
                "member",
                "message_type",
                "object",
                "partial",
                "permission_group",
                "preference_category",
                "preference_center",
                "preference_center_domain",
                "reusable_request",
                "service_token",
                "signing_key",
                "source",
                "subscription",
                "tag",
                "translation",
                "user",
                "variable",
                "view",
                "webhook",
                "workflow",
            ]
        ],
    ]
    """Filter by resource type.

    Accepts one type or an array of types. `channel` includes channel environment
    settings, and `source` includes source environment settings.
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return entries inserted at or after this RFC 3339 timestamp."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return entries inserted at or before this RFC 3339 timestamp."""

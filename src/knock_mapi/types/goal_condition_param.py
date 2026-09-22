# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = [
    "GoalConditionParam",
    "Event",
    "EventWorkflowWaitForEventIntegrationSourceEvent",
    "EventWorkflowWaitForEventAudienceEvent",
]


class EventWorkflowWaitForEventIntegrationSourceEvent(TypedDict, total=False):
    """An integration source event to wait for."""

    event_key: Required[str]
    """The name of the event to wait for."""

    event_type: Required[Literal["integration_source"]]
    """The type of event to wait for."""

    integration_source_key: Required[str]
    """The key of the integration source that emits the event to wait for."""

    recipient_path: Optional[str]
    """JSON path into the source event that yields the recipient user ID.

    Use userId for Segment events, or a body./headers. path for HTTP events (e.g.
    body.userId).
    """


class EventWorkflowWaitForEventAudienceEvent(TypedDict, total=False):
    """
    An audience membership event to wait for when a recipient enters or exits an audience.
    """

    audience_key: Required[str]
    """The key of the audience to wait for membership changes."""

    event_key: Required[Literal["enter", "exit"]]
    """The audience membership transition to wait for."""

    event_type: Required[Literal["audience"]]
    """The type of event to wait for."""


Event: TypeAlias = Union[EventWorkflowWaitForEventIntegrationSourceEvent, EventWorkflowWaitForEventAudienceEvent]


class GoalConditionParam(TypedDict, total=False):
    """
    A goal condition consisting of a polymorphic event and optional match conditions.
    """

    event: Required[Event]
    """The event to track. Supports integration_source and audience event types."""

    match_conditions: Iterable[ConditionGroupParam]
    """
    Optional list of condition groups; each group uses an operator (and/or) with
    nested conditions.
    """

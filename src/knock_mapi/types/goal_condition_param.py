# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = [
    "GoalConditionParam",
    "Event",
    "EventWorkflowWaitForEventRecipientEvent",
    "EventWorkflowWaitForEventIntegrationSourceEvent",
    "EventWorkflowWaitForEventAudienceEvent",
]


class EventWorkflowWaitForEventRecipientEvent(TypedDict, total=False):
    """A recipient updated event to wait for from the workflow recipient."""

    event_type: Required[Literal["recipient"]]
    """The type of event to wait for."""

    event_key: Literal["updated"]
    """Recipient lifecycle event to wait for. Always "updated" today."""


class EventWorkflowWaitForEventIntegrationSourceEvent(TypedDict, total=False):
    """An integration source event to wait for."""

    event_key: Required[str]
    """The name of the event to wait for."""

    event_type: Required[Literal["integration_source"]]
    """The type of event to wait for."""

    integration_source_key: Required[str]
    """The key of the integration source that emits the event to wait for."""


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


Event: TypeAlias = Union[
    EventWorkflowWaitForEventRecipientEvent,
    EventWorkflowWaitForEventIntegrationSourceEvent,
    EventWorkflowWaitForEventAudienceEvent,
]


class GoalConditionParam(TypedDict, total=False):
    """
    A goal condition consisting of a polymorphic event and optional match conditions.
    """

    event: Required[Event]
    """The event to track.

    Supports recipient, integration_source, and audience event types.
    """

    match_conditions: Iterable[ConditionGroupParam]
    """A list of condition groups.

    Required for recipient events; each group uses an operator (and/or) with nested
    conditions.
    """

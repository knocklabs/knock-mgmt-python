# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = [
    "GoalCondition",
    "Event",
    "EventWorkflowWaitForEventIntegrationSourceEvent",
    "EventWorkflowWaitForEventAudienceEvent",
]


class EventWorkflowWaitForEventIntegrationSourceEvent(BaseModel):
    """An integration source event to wait for."""

    event_key: str
    """The name of the event to wait for."""

    event_type: Literal["integration_source"]
    """The type of event to wait for."""

    integration_source_key: str
    """The key of the integration source that emits the event to wait for."""

    recipient_path: Optional[str] = None
    """JSON path into the source event that yields the recipient user ID.

    Use userId for Segment events, or a body./headers. path for HTTP events (e.g.
    body.userId).
    """


class EventWorkflowWaitForEventAudienceEvent(BaseModel):
    """
    An audience membership event to wait for when a recipient enters or exits an audience.
    """

    audience_key: str
    """The key of the audience to wait for membership changes."""

    event_key: Literal["enter", "exit"]
    """The audience membership transition to wait for."""

    event_type: Literal["audience"]
    """The type of event to wait for."""


Event: TypeAlias = Union[EventWorkflowWaitForEventIntegrationSourceEvent, EventWorkflowWaitForEventAudienceEvent]


class GoalCondition(BaseModel):
    """
    A goal condition consisting of a polymorphic event and optional match conditions.
    """

    event: Event
    """The event to track. Supports integration_source and audience event types."""

    match_conditions: Optional[List[ConditionGroup]] = None
    """
    Optional list of condition groups; each group uses an operator (and/or) with
    nested conditions.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = [
    "GoalCondition",
    "Event",
    "EventWorkflowWaitForEventRecipientEvent",
    "EventWorkflowWaitForEventIntegrationSourceEvent",
    "EventWorkflowWaitForEventAudienceEvent",
]


class EventWorkflowWaitForEventRecipientEvent(BaseModel):
    """A recipient updated event to wait for from the workflow recipient."""

    event_type: Literal["recipient"]
    """The type of event to wait for."""

    event_key: Optional[Literal["updated"]] = None
    """Recipient lifecycle event to wait for. Always "updated" today."""


class EventWorkflowWaitForEventIntegrationSourceEvent(BaseModel):
    """An integration source event to wait for."""

    event_key: str
    """The name of the event to wait for."""

    event_type: Literal["integration_source"]
    """The type of event to wait for."""

    integration_source_key: str
    """The key of the integration source that emits the event to wait for."""


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


Event: TypeAlias = Union[
    EventWorkflowWaitForEventRecipientEvent,
    EventWorkflowWaitForEventIntegrationSourceEvent,
    EventWorkflowWaitForEventAudienceEvent,
]


class GoalCondition(BaseModel):
    """
    A goal condition consisting of a polymorphic event and optional match conditions.
    """

    event: Event
    """The event to track.

    Supports recipient, integration_source, and audience event types.
    """

    match_conditions: Optional[List[ConditionGroup]] = None
    """A list of condition groups.

    Required for recipient events; each group uses an operator (and/or) with nested
    conditions.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["WorkflowTriggerEventsParam", "AudienceTrigger", "SourceEventTrigger", "SourceEventTriggerTriggerParameters"]


class AudienceTrigger(TypedDict, total=False):
    """
    An audience trigger that automatically triggers the workflow when a user enters an audience. Read more in the [docs](https://docs.knock.app/send-notifications/triggering-workflows/audiences).
    """

    audience_action_type: Required[Literal["member_added"]]
    """The action type that triggers the workflow."""

    audience_key: Required[str]
    """The unique key of the audience that triggers the workflow."""

    type: Required[Literal["audience"]]
    """The trigger event type."""


class SourceEventTriggerTriggerParameters(TypedDict, total=False):
    """Optional parameters to customize the triggered workflow run."""

    actor: Optional[str]
    """A liquid template string that will be evaluated to determine the actor."""

    cancellation_key: Optional[str]
    """
    A liquid template string that will be evaluated to determine the cancellation
    key.
    """

    data: Optional[str]
    """A liquid template string that will be evaluated and passed as the data payload."""

    recipients: Optional[str]
    """A liquid template string that will be evaluated to determine recipients."""

    tenant: Optional[str]
    """A liquid template string that will be evaluated to determine the tenant."""


class SourceEventTrigger(TypedDict, total=False):
    """
    A source event trigger that triggers the workflow when an event is received from an integration source. Read more in the [docs](https://docs.knock.app/integrations/sources/overview).
    """

    event_name: Required[str]
    """The name of the event that triggers the workflow."""

    event_type: Required[Literal["track"]]
    """The type of event. Currently only 'track' is supported."""

    integration_source_id: Required[str]
    """The ID of the integration source that emits the event."""

    type: Required[Literal["source_event"]]
    """The trigger event type."""

    trigger_parameters: Optional[SourceEventTriggerTriggerParameters]
    """Optional parameters to customize the triggered workflow run."""


WorkflowTriggerEventsParam: TypeAlias = Union[AudienceTrigger, SourceEventTrigger]

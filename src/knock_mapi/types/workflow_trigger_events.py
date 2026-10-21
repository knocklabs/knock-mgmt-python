# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["WorkflowTriggerEvents", "AudienceTrigger", "SourceEventTrigger", "SourceEventTriggerTriggerParameters"]


class AudienceTrigger(BaseModel):
    """
    An audience trigger that automatically triggers the workflow when a user enters an audience. Read more in the [docs](https://docs.knock.app/send-notifications/triggering-workflows/audiences).
    """

    audience_action_type: Literal["member_added"]
    """The action type that triggers the workflow."""

    audience_key: str
    """The unique key of the audience that triggers the workflow."""

    type: Literal["audience"]
    """The trigger event type."""


class SourceEventTriggerTriggerParameters(BaseModel):
    """Optional parameters to customize the triggered workflow run."""

    actor: Optional[str] = None
    """A liquid template string that will be evaluated to determine the actor."""

    cancellation_key: Optional[str] = None
    """
    A liquid template string that will be evaluated to determine the cancellation
    key.
    """

    data: Optional[str] = None
    """A liquid template string that will be evaluated and passed as the data payload."""

    recipients: Optional[str] = None
    """A liquid template string that will be evaluated to determine recipients."""

    tenant: Optional[str] = None
    """A liquid template string that will be evaluated to determine the tenant."""


class SourceEventTrigger(BaseModel):
    """
    A source event trigger that triggers the workflow when an event is received from an integration source. Read more in the [docs](https://docs.knock.app/integrations/sources/overview).
    """

    event_name: str
    """The name of the event that triggers the workflow."""

    event_type: Literal["track"]
    """The type of event. Currently only 'track' is supported."""

    integration_source_id: str
    """The ID of the integration source that emits the event."""

    type: Literal["source_event"]
    """The trigger event type."""

    trigger_parameters: Optional[SourceEventTriggerTriggerParameters] = None
    """Optional parameters to customize the triggered workflow run."""


WorkflowTriggerEvents: TypeAlias = Annotated[
    Union[AudienceTrigger, SourceEventTrigger], PropertyInfo(discriminator="type")
]

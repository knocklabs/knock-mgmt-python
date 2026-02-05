# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .condition_group import ConditionGroup
from .workflow_sms_step import WorkflowSMSStep
from .workflow_chat_step import WorkflowChatStep
from .workflow_push_step import WorkflowPushStep
from .workflow_batch_step import WorkflowBatchStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_email_step import WorkflowEmailStep
from .workflow_fetch_step import WorkflowFetchStep
from .workflow_webhook_step import WorkflowWebhookStep
from .workflow_throttle_step import WorkflowThrottleStep
from .workflow_in_app_feed_step import WorkflowInAppFeedStep
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep

__all__ = [
    "WorkflowStep",
    "WorkflowUpdateDataStep",
    "WorkflowUpdateDataStepSettings",
    "WorkflowUpdateObjectStep",
    "WorkflowUpdateObjectStepSettings",
    "WorkflowUpdateTenantStep",
    "WorkflowUpdateTenantStepSettings",
    "WorkflowUpdateUserStep",
    "WorkflowUpdateUserStepSettings",
]


class WorkflowUpdateDataStepSettings(BaseModel):
    """The settings for the update data step."""

    data: str
    """
    A JSON string or Liquid template that evaluates to the data to merge into the
    workflow's data scope.
    """


class WorkflowUpdateDataStep(BaseModel):
    """An update data function step.

    Merges data into the workflow's `data` scope for use in subsequent steps.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowUpdateDataStepSettings
    """The settings for the update data step."""

    type: Literal["update_data"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""


class WorkflowUpdateObjectStepSettings(BaseModel):
    """The settings for the update object step."""

    recipient_gid: str
    """The global identifier (GID) of the object to update.

    Format: gid://Object/{collection}/{id}
    """

    update_properties: str
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the object.
    """


class WorkflowUpdateObjectStep(BaseModel):
    """An update object step.

    Updates properties of a specific object referenced in the workflow.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowUpdateObjectStepSettings
    """The settings for the update object step."""

    type: Literal["update_object"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""


class WorkflowUpdateTenantStepSettings(BaseModel):
    """The settings for the update tenant step."""

    recipient_mode: Literal["current", "reference"]
    """The recipient mode determining how the tenant is selected.

    'current' uses the workflow's current tenant. 'reference' uses a specific tenant
    ID.
    """

    update_properties: str
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the tenant.
    """

    recipient_gid: Optional[str] = None
    """The global identifier (GID) of the tenant to update.

    Required when recipient_mode is 'reference'. Format: gid://Object/$tenants/{id}
    """


class WorkflowUpdateTenantStep(BaseModel):
    """An update tenant step.

    Updates properties of a specific tenant referenced in the workflow.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowUpdateTenantStepSettings
    """The settings for the update tenant step."""

    type: Literal["update_tenant"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""


class WorkflowUpdateUserStepSettings(BaseModel):
    """The settings for the update user step."""

    recipient_mode: Literal["current", "reference"]
    """The recipient mode determining how the user is selected.

    'current' uses the workflow's current user. 'reference' uses a specific user ID.
    """

    update_properties: str
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the user.
    """

    recipient_gid: Optional[str] = None
    """The global identifier (GID) of the user to update.

    Required when recipient_mode is 'reference'. Format: gid://Object/$users/{id}
    """


class WorkflowUpdateUserStep(BaseModel):
    """An update user step.

    Updates properties of a specific user referenced in the workflow.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowUpdateUserStepSettings
    """The settings for the update user step."""

    type: Literal["update_user"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""


if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStep = TypeAliasType(
        "WorkflowStep",
        Union[
            WorkflowWebhookStep,
            WorkflowInAppFeedStep,
            WorkflowChatStep,
            WorkflowSMSStep,
            WorkflowPushStep,
            WorkflowEmailStep,
            WorkflowDelayStep,
            WorkflowBatchStep,
            WorkflowFetchStep,
            WorkflowUpdateDataStep,
            WorkflowUpdateObjectStep,
            WorkflowUpdateTenantStep,
            WorkflowUpdateUserStep,
            WorkflowThrottleStep,
            "WorkflowBranchStep",
            WorkflowTriggerWorkflowStep,
        ],
    )
else:
    WorkflowStep: TypeAlias = Union[
        WorkflowWebhookStep,
        WorkflowInAppFeedStep,
        WorkflowChatStep,
        WorkflowSMSStep,
        WorkflowPushStep,
        WorkflowEmailStep,
        WorkflowDelayStep,
        WorkflowBatchStep,
        WorkflowFetchStep,
        WorkflowUpdateDataStep,
        WorkflowUpdateObjectStep,
        WorkflowUpdateTenantStep,
        WorkflowUpdateUserStep,
        WorkflowThrottleStep,
        "WorkflowBranchStep",
        WorkflowTriggerWorkflowStep,
    ]

from .workflow_branch_step import WorkflowBranchStep

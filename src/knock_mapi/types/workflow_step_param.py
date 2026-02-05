# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from .._compat import PYDANTIC_V1
from .condition_group_param import ConditionGroupParam
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .workflow_in_app_feed_step_param import WorkflowInAppFeedStepParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = [
    "WorkflowStepParam",
    "WorkflowUpdateDataStep",
    "WorkflowUpdateDataStepSettings",
    "WorkflowUpdateObjectStep",
    "WorkflowUpdateObjectStepSettings",
    "WorkflowUpdateTenantStep",
    "WorkflowUpdateTenantStepSettings",
    "WorkflowUpdateUserStep",
    "WorkflowUpdateUserStepSettings",
]


class WorkflowUpdateDataStepSettings(TypedDict, total=False):
    """The settings for the update data step."""

    data: Required[str]
    """
    A JSON string or Liquid template that evaluates to the data to merge into the
    workflow's data scope.
    """


class WorkflowUpdateDataStep(TypedDict, total=False):
    """An update data function step.

    Merges data into the workflow's `data` scope for use in subsequent steps.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowUpdateDataStepSettings]
    """The settings for the update data step."""

    type: Required[Literal["update_data"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""


class WorkflowUpdateObjectStepSettings(TypedDict, total=False):
    """The settings for the update object step."""

    recipient_gid: Required[str]
    """The global identifier (GID) of the object to update.

    Format: gid://Object/{collection}/{id}
    """

    update_properties: Required[str]
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the object.
    """


class WorkflowUpdateObjectStep(TypedDict, total=False):
    """An update object step.

    Updates properties of a specific object referenced in the workflow.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowUpdateObjectStepSettings]
    """The settings for the update object step."""

    type: Required[Literal["update_object"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""


class WorkflowUpdateTenantStepSettings(TypedDict, total=False):
    """The settings for the update tenant step."""

    recipient_mode: Required[Literal["current", "reference"]]
    """The recipient mode determining how the tenant is selected.

    'current' uses the workflow's current tenant. 'reference' uses a specific tenant
    ID.
    """

    update_properties: Required[str]
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the tenant.
    """

    recipient_gid: Optional[str]
    """The global identifier (GID) of the tenant to update.

    Required when recipient_mode is 'reference'. Format: gid://Object/$tenants/{id}
    """


class WorkflowUpdateTenantStep(TypedDict, total=False):
    """An update tenant step.

    Updates properties of a specific tenant referenced in the workflow.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowUpdateTenantStepSettings]
    """The settings for the update tenant step."""

    type: Required[Literal["update_tenant"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""


class WorkflowUpdateUserStepSettings(TypedDict, total=False):
    """The settings for the update user step."""

    recipient_mode: Required[Literal["current", "reference"]]
    """The recipient mode determining how the user is selected.

    'current' uses the workflow's current user. 'reference' uses a specific user ID.
    """

    update_properties: Required[str]
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the user.
    """

    recipient_gid: Optional[str]
    """The global identifier (GID) of the user to update.

    Required when recipient_mode is 'reference'. Format: gid://Object/$users/{id}
    """


class WorkflowUpdateUserStep(TypedDict, total=False):
    """An update user step.

    Updates properties of a specific user referenced in the workflow.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowUpdateUserStepSettings]
    """The settings for the update user step."""

    type: Required[Literal["update_user"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""


if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStepParam = TypeAliasType(
        "WorkflowStepParam",
        Union[
            WorkflowWebhookStepParam,
            WorkflowInAppFeedStepParam,
            WorkflowChatStepParam,
            WorkflowSMSStepParam,
            WorkflowPushStepParam,
            WorkflowEmailStepParam,
            WorkflowDelayStepParam,
            WorkflowBatchStepParam,
            WorkflowFetchStepParam,
            WorkflowUpdateDataStep,
            WorkflowUpdateObjectStep,
            WorkflowUpdateTenantStep,
            WorkflowUpdateUserStep,
            WorkflowThrottleStepParam,
            "WorkflowBranchStepParam",
            WorkflowTriggerWorkflowStepParam,
        ],
    )
else:
    WorkflowStepParam: TypeAlias = Union[
        WorkflowWebhookStepParam,
        WorkflowInAppFeedStepParam,
        WorkflowChatStepParam,
        WorkflowSMSStepParam,
        WorkflowPushStepParam,
        WorkflowEmailStepParam,
        WorkflowDelayStepParam,
        WorkflowBatchStepParam,
        WorkflowFetchStepParam,
        WorkflowUpdateDataStep,
        WorkflowUpdateObjectStep,
        WorkflowUpdateTenantStep,
        WorkflowUpdateUserStep,
        WorkflowThrottleStepParam,
        "WorkflowBranchStepParam",
        WorkflowTriggerWorkflowStepParam,
    ]

from .workflow_branch_step_param import WorkflowBranchStepParam

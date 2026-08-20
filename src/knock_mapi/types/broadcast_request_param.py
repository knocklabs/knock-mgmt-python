# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .send_window_param import SendWindowParam
from .condition_group_param import ConditionGroupParam
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_in_app_feed_step_param import WorkflowInAppFeedStepParam
from .workflow_random_cohort_step_param import WorkflowRandomCohortStepParam

__all__ = ["BroadcastRequestParam", "Step", "StepWorkflowInAppGuideStep", "GoalAttachment", "Settings"]


class StepWorkflowInAppGuideStep(TypedDict, total=False):
    """An in-app guide step within a workflow.

    References a guide that will be shown to recipients who execute this step. Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    channel_type: Required[Literal["in_app_guide"]]
    """The type of the channel step. Always `in_app_guide` for in-app guide steps."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    type: Required[Literal["channel"]]
    """The type of the workflow step."""

    channel_group_key: Optional[str]
    """
    The key of the channel group to which the channel step will be sending a
    notification. Either `channel_key` or `channel_group_key` must be provided, but
    not both.
    """

    channel_key: Optional[str]
    """
    The key of a specific configured channel instance (e.g., 'knock-email',
    'postmark', 'sendgrid-marketing') to send the notification through. Either
    `channel_key` or `channel_group_key` must be provided, but not both.
    """

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    guide_key: Optional[str]
    """The key of the guide to reference.

    When a recipient executes this step they are added to the managed audience that
    backs the guide's workflow-derived targeting.
    """

    name: Optional[str]
    """A name for the workflow step."""

    send_windows: Optional[Iterable[SendWindowParam]]
    """A list of send window objects.

    Must include one send window object per day of the week.
    """


Step: TypeAlias = Union[
    WorkflowWebhookStepParam,
    WorkflowInAppFeedStepParam,
    StepWorkflowInAppGuideStep,
    WorkflowChatStepParam,
    WorkflowSMSStepParam,
    WorkflowPushStepParam,
    WorkflowEmailStepParam,
    "WorkflowBranchStepParam",
    WorkflowDelayStepParam,
    WorkflowRandomCohortStepParam,
]


class GoalAttachment(TypedDict, total=False):
    """Attaches a goal to a workflow, guide, or broadcast for attribution tracking."""

    goal_key: Required[str]
    """The key of the goal to attach."""

    attribution_window_days: int
    """The number of days to attribute conversions after the notification is sent.

    Must be between 1 and 30. Defaults to 7.
    """


class Settings(TypedDict, total=False):
    """A map of broadcast settings."""

    is_commercial: bool
    """Whether the broadcast is commercial. Defaults to true."""

    override_preferences: bool
    """Whether to ignore recipient preferences for a given type of notification.

    If true, will send for every channel in the workflow even if the recipient has
    opted out of a certain kind. Defaults to false.
    """


class BroadcastRequestParam(TypedDict, total=False):
    """A broadcast request for upserting a broadcast."""

    name: Required[str]
    """A name for the broadcast. Must be at maximum 255 characters in length."""

    steps: Required[Iterable[Step]]
    """A list of broadcast step objects in the broadcast.

    Broadcasts only support channel, branch, and delay steps.
    """

    categories: SequenceNotStr[str]
    """A list of categories that the broadcast belongs to."""

    description: str
    """An arbitrary string attached to a broadcast object.

    Useful for adding notes about the broadcast for internal purposes. Maximum of
    280 characters allowed.
    """

    goal_attachment: Optional[GoalAttachment]
    """Attaches a goal to a workflow, guide, or broadcast for attribution tracking."""

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp of when the broadcast is scheduled to be sent."""

    settings: Settings
    """A map of broadcast settings."""

    target_audience_key: str
    """The key of the audience to target for this broadcast."""


from .workflow_branch_step_param import WorkflowBranchStepParam

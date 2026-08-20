# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .send_window import SendWindow
from .condition_group import ConditionGroup
from .workflow_sms_step import WorkflowSMSStep
from .workflow_chat_step import WorkflowChatStep
from .workflow_push_step import WorkflowPushStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_email_step import WorkflowEmailStep
from .workflow_webhook_step import WorkflowWebhookStep
from .workflow_in_app_feed_step import WorkflowInAppFeedStep
from .workflow_random_cohort_step import WorkflowRandomCohortStep

__all__ = ["Broadcast", "Step", "StepWorkflowInAppGuideStep", "GoalAttachment", "Settings"]


class StepWorkflowInAppGuideStep(BaseModel):
    """An in-app guide step within a workflow.

    References a guide that will be shown to recipients who execute this step. Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    channel_type: Literal["in_app_guide"]
    """The type of the channel step. Always `in_app_guide` for in-app guide steps."""

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    type: Literal["channel"]
    """The type of the workflow step."""

    channel_group_key: Optional[str] = None
    """
    The key of the channel group to which the channel step will be sending a
    notification. Either `channel_key` or `channel_group_key` must be provided, but
    not both.
    """

    channel_key: Optional[str] = None
    """
    The key of a specific configured channel instance (e.g., 'knock-email',
    'postmark', 'sendgrid-marketing') to send the notification through. Either
    `channel_key` or `channel_group_key` must be provided, but not both.
    """

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    guide_key: Optional[str] = None
    """The key of the guide to reference.

    When a recipient executes this step they are added to the managed audience that
    backs the guide's workflow-derived targeting.
    """

    name: Optional[str] = None
    """A name for the workflow step."""

    send_windows: Optional[List[SendWindow]] = None
    """A list of send window objects.

    Must include one send window object per day of the week.
    """


Step: TypeAlias = Union[
    WorkflowWebhookStep,
    WorkflowInAppFeedStep,
    StepWorkflowInAppGuideStep,
    WorkflowChatStep,
    WorkflowSMSStep,
    WorkflowPushStep,
    WorkflowEmailStep,
    "WorkflowBranchStep",
    WorkflowDelayStep,
    WorkflowRandomCohortStep,
]


class GoalAttachment(BaseModel):
    """Attaches a goal to a workflow, guide, or broadcast for attribution tracking."""

    goal_key: str
    """The key of the goal to attach."""

    attribution_window_days: Optional[int] = None
    """The number of days to attribute conversions after the notification is sent.

    Must be between 1 and 30. Defaults to 7.
    """


class Settings(BaseModel):
    """A map of broadcast settings."""

    is_commercial: Optional[bool] = None
    """Whether the broadcast is commercial. Defaults to true."""

    override_preferences: Optional[bool] = None
    """Whether to ignore recipient preferences for a given type of notification.

    If true, will send for every channel in the workflow even if the recipient has
    opted out of a certain kind. Defaults to false.
    """


class Broadcast(BaseModel):
    """A broadcast object."""

    created_at: datetime
    """The timestamp of when the broadcast was created. (read-only)."""

    environment: str
    """The slug of the environment in which the broadcast exists. (read-only)."""

    key: str
    """The unique key string for the broadcast object.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the broadcast. Must be at maximum 255 characters in length."""

    sha: str
    """The SHA hash of the workflow data. (read-only)."""

    status: Literal["draft", "scheduled", "sent"]
    """The current status of the broadcast. One of: `draft`, `scheduled`, `sent`."""

    steps: List[Step]
    """A list of broadcast step objects in the broadcast.

    Broadcasts only support channel, branch, and delay steps.
    """

    updated_at: datetime
    """The timestamp of when the broadcast was last updated. (read-only)."""

    valid: bool
    """Whether the broadcast and its steps are in a valid state. (read-only)."""

    archived_at: Optional[datetime] = None
    """The timestamp of when the broadcast was archived."""

    categories: Optional[List[str]] = None
    """A list of categories that the broadcast belongs to."""

    description: Optional[str] = None
    """An arbitrary string attached to a broadcast object.

    Useful for adding notes about the broadcast for internal purposes. Maximum of
    280 characters allowed.
    """

    goal_attachment: Optional[GoalAttachment] = None
    """Attaches a goal to a workflow, guide, or broadcast for attribution tracking."""

    scheduled_at: Optional[datetime] = None
    """The timestamp of when the broadcast is scheduled to be sent."""

    sent_at: Optional[datetime] = None
    """The timestamp of when the broadcast was sent. (read-only)."""

    settings: Optional[Settings] = None
    """A map of broadcast settings."""

    target_audience_key: Optional[str] = None
    """The key of the audience to target for this broadcast."""


from .workflow_branch_step import WorkflowBranchStep

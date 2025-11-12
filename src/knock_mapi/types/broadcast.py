# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .workflow_sms_step import WorkflowSMSStep
from .workflow_chat_step import WorkflowChatStep
from .workflow_push_step import WorkflowPushStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_email_step import WorkflowEmailStep
from .workflow_webhook_step import WorkflowWebhookStep
from .workflow_in_app_feed_step import WorkflowInAppFeedStep

__all__ = ["Broadcast", "Step", "Settings"]

Step: TypeAlias = Union[
    WorkflowWebhookStep,
    WorkflowInAppFeedStep,
    WorkflowChatStep,
    WorkflowSMSStep,
    WorkflowPushStep,
    WorkflowEmailStep,
    "WorkflowBranchStep",
    WorkflowDelayStep,
]


class Settings(BaseModel):
    is_commercial: Optional[bool] = None
    """Whether the broadcast is commercial. Defaults to true."""

    override_preferences: Optional[bool] = None
    """Whether to ignore recipient preferences for a given type of notification.

    If true, will send for every channel in the workflow even if the recipient has
    opted out of a certain kind. Defaults to false.
    """


class Broadcast(BaseModel):
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

    scheduled_at: Optional[datetime] = None
    """The timestamp of when the broadcast is scheduled to be sent."""

    sent_at: Optional[datetime] = None
    """The timestamp of when the broadcast was sent. (read-only)."""

    settings: Optional[Settings] = None
    """A map of broadcast settings."""

    target_audience_key: Optional[str] = None
    """The key of the audience to target for this broadcast."""


from .workflow_branch_step import WorkflowBranchStep

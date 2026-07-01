# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_in_app_feed_step_param import WorkflowInAppFeedStepParam
from .workflow_random_cohort_step_param import WorkflowRandomCohortStepParam

__all__ = ["BroadcastRequestParam", "Step", "Settings"]

Step: TypeAlias = Union[
    WorkflowWebhookStepParam,
    WorkflowInAppFeedStepParam,
    WorkflowChatStepParam,
    WorkflowSMSStepParam,
    WorkflowPushStepParam,
    WorkflowEmailStepParam,
    "WorkflowBranchStepParam",
    WorkflowDelayStepParam,
    WorkflowRandomCohortStepParam,
]


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

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp of when the broadcast is scheduled to be sent."""

    settings: Settings
    """A map of broadcast settings."""

    target_audience_key: str
    """The key of the audience to target for this broadcast."""


from .workflow_branch_step_param import WorkflowBranchStepParam

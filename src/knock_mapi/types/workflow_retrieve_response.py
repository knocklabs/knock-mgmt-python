# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .member_user import MemberUser
from .condition_group import ConditionGroup

__all__ = ["WorkflowRetrieveResponse", "Settings"]


class Settings(BaseModel):
    """A map of workflow settings."""

    is_commercial: Optional[bool] = None
    """Whether the workflow is commercial. Defaults to false."""

    override_preferences: Optional[bool] = None
    """Whether to ignore recipient preferences for a given type of notification.

    If true, will send for every channel in the workflow even if the recipient has
    opted out of a certain kind. Defaults to false.
    """


class WorkflowRetrieveResponse(BaseModel):
    """A workflow object."""

    active: bool
    """
    Whether the workflow is
    [active](https://docs.knock.app/concepts/workflows#workflow-status) in the
    current environment. (read-only).
    """

    created_at: datetime
    """The timestamp of when the workflow was created. (read-only)."""

    environment: str
    """The slug of the environment in which the workflow exists. (read-only)."""

    key: str
    """The unique key string for the workflow object.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the workflow. Must be at maximum 255 characters in length."""

    sha: str
    """The SHA hash of the workflow data. (read-only)."""

    steps: List["WorkflowStep"]
    """A list of workflow step objects in the workflow."""

    updated_at: datetime
    """The timestamp of when the workflow was last updated. (read-only)."""

    valid: bool
    """Whether the workflow and its steps are in a valid state. (read-only)."""

    categories: Optional[List[str]] = None
    """
    A list of
    [categories](https://docs.knock.app/concepts/workflows#workflow-categories) that
    the workflow belongs to.
    """

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    created_by: Optional[MemberUser] = None
    """Information about a user within the Knock dashboard.

    Not to be confused with an external user (recipient) of a workflow.
    """

    deleted_at: Optional[datetime] = None
    """The timestamp of when the workflow was deleted. (read-only)."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow object.

    Useful for adding notes about the workflow for internal purposes. Maximum of 280
    characters allowed.
    """

    settings: Optional[Settings] = None
    """A map of workflow settings."""

    tags: Optional[List[str]] = None
    """Use tags to organize resources internally within your account.

    For example, by team or product area.
    """

    trigger_data_json_schema: Optional[Dict[str, object]] = None
    """
    A JSON schema for the expected structure of the workflow trigger's `data`
    payload (available in templates as `{{ data.field_name }}`). Used to validate
    trigger requests. Read more in the
    [docs](https://docs.knock.app/developer-tools/validating-trigger-data).
    """

    trigger_frequency: Optional[Literal["every_trigger", "once_per_recipient", "once_per_recipient_per_tenant"]] = None
    """The frequency at which the workflow should be triggered.

    One of: `once_per_recipient`, `once_per_recipient_per_tenant`, `every_trigger`.
    Defaults to `every_trigger`. Read more in
    [docs](https://docs.knock.app/send-notifications/triggering-workflows/overview#controlling-workflow-trigger-frequency).
    """

    updated_by: Optional[MemberUser] = None
    """Information about a user within the Knock dashboard.

    Not to be confused with an external user (recipient) of a workflow.
    """


from .workflow_step import WorkflowStep

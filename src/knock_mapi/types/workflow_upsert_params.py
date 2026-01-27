# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowUpsertParams", "Workflow", "WorkflowSettings"]


class WorkflowUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    workflow: Required[Workflow]
    """A workflow request for upserting a workflow."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""


class WorkflowSettings(TypedDict, total=False):
    """A map of workflow settings."""

    is_commercial: bool
    """Whether the workflow is commercial. Defaults to false."""

    override_preferences: bool
    """Whether to ignore recipient preferences for a given type of notification.

    If true, will send for every channel in the workflow even if the recipient has
    opted out of a certain kind. Defaults to false.
    """


class Workflow(TypedDict, total=False):
    """A workflow request for upserting a workflow."""

    name: Required[str]
    """A name for the workflow. Must be at maximum 255 characters in length."""

    steps: Required[Iterable["WorkflowStepParam"]]
    """A list of workflow step objects in the workflow."""

    categories: SequenceNotStr[str]
    """
    A list of
    [categories](https://docs.knock.app/concepts/workflows#workflow-categories) that
    the workflow belongs to.
    """

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: str
    """An arbitrary string attached to a workflow object.

    Useful for adding notes about the workflow for internal purposes. Maximum of 280
    characters allowed.
    """

    settings: WorkflowSettings
    """A map of workflow settings."""

    trigger_data_json_schema: Dict[str, object]
    """
    A JSON schema for the expected structure of the workflow trigger's `data`
    payload (available in templates as `{{ data.field_name }}`). Used to validate
    trigger requests. Read more in the
    [docs](https://docs.knock.app/developer-tools/validating-trigger-data).
    """

    trigger_frequency: Literal["every_trigger", "once_per_recipient", "once_per_recipient_per_tenant"]
    """The frequency at which the workflow should be triggered.

    One of: `once_per_recipient`, `once_per_recipient_per_tenant`, `every_trigger`.
    Defaults to `every_trigger`. Read more in
    [docs](https://docs.knock.app/send-notifications/triggering-workflows/overview#controlling-workflow-trigger-frequency).
    """


from .workflow_step_param import WorkflowStepParam

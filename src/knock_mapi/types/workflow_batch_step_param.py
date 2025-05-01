# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .duration_param import DurationParam

__all__ = ["WorkflowBatchStepParam", "Settings"]


class Settings(TypedDict, total=False):
    batch_execution_mode: Optional[Literal["accumulate", "flush_leading"]]
    """The execution mode of the batch step.

    One of: `accumulate` or `flush_leading`. When set to `flush_leading`, the first
    item in the batch will be executed immediately, and the rest will be batched.
    See
    [these docs](https://docs.knock.app/designing-workflows/batch-function#immediately-flushing-the-first-item-in-a-batch)
    for more information.
    """

    batch_items_max_limit: Optional[int]
    """The maximum number of batch items allowed in a batch. Between: 2 and 1000."""

    batch_items_render_limit: Optional[int]
    """The maximum number of batch items allowed to be rendered into a template.

    Between: 1 and 100. Defaults to 10.
    """

    batch_key: Optional[str]
    """The data property to use to batch notifications per recipient."""

    batch_order: Optional[Literal["asc", "desc"]]
    """
    The order describing whether to return the first or last ten batch items in the
    activities variable. One of: `asc` or `desc`.
    """

    batch_until_field_path: Optional[str]
    """The data path to resolve the batch window.

    The resolved value must be an ISO-8601 timestamp.
    """

    batch_window: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    batch_window_extension_limit: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    batch_window_type: Optional[Literal["fixed", "sliding"]]
    """The type of the batch window used. One of: `fixed` or `sliding`."""


class WorkflowBatchStepParam(TypedDict, total=False):
    description: Required[Optional[str]]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Required[str]
    """A name for the workflow step."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the batch step."""

    type: Required[Literal["batch"]]
    """The type of the workflow step."""

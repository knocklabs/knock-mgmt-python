# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup
from .request_template import RequestTemplate

__all__ = ["WorkflowFetchStep"]


class WorkflowFetchStep(BaseModel):
    """A fetch function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/fetch-function).
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: RequestTemplate
    """A request template for a fetch function step."""

    type: Literal["http_fetch"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""

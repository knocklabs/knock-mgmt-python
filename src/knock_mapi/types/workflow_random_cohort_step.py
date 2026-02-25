# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkflowRandomCohortStep"]


class WorkflowRandomCohortStep(BaseModel):
    """An experiment step.

    Deterministically assigns recipients to percentage-based cohorts for A/B testing and experimentation.
    """

    cohort_branches: List[object]
    """A list of cohort branches.

    Must have between 2 and 10 branches, and percentages must sum to 100.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    type: Literal["random_cohort"]
    """The type of step."""

    cohort_key: Optional[str] = None
    """The key used to deterministically assign recipients to cohorts.

    Defaults to the recipient ID if not provided.
    """

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""

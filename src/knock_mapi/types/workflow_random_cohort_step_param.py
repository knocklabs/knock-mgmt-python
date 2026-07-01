# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkflowRandomCohortStepParam"]


class WorkflowRandomCohortStepParam(TypedDict, total=False):
    """An experiment step.

    Deterministically assigns recipients to percentage-based cohorts for A/B testing and experimentation.
    """

    cohort_branches: Required[Iterable[object]]
    """A list of cohort branches.

    Must have between 2 and 10 branches, and percentages must sum to 100.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    type: Required[Literal["random_cohort"]]
    """The type of step."""

    cohort_key: Optional[str]
    """The key used to deterministically assign recipients to cohorts.

    Defaults to the recipient ID if not provided.
    """

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""

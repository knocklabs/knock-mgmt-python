# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WorkflowRandomCohortStepBranch"]


class WorkflowRandomCohortStepBranch(BaseModel):
    """A cohort branch in an experiment step."""

    percentage: str
    """The percentage of recipients to assign to this cohort.

    Must be between 0 and 100 with at most 1 decimal place. All branch percentages
    must sum to 100. Sent as a number in requests; returned as a decimal string in
    responses (e.g. "50", "33.3").
    """

    name: Optional[str] = None
    """The name of the cohort branch."""

    steps: Optional[List["WorkflowStep"]] = None
    """A list of steps that will be executed for recipients assigned to this cohort."""

    terminates: Optional[bool] = None
    """If the workflow should halt at the end of the branch.

    Defaults to false if not provided.
    """


from .workflow_step import WorkflowStep

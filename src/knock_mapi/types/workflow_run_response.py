# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowRunResponse"]


class WorkflowRunResponse(BaseModel):
    """A response to a run workflow request."""

    workflow_run_id: str
    """The ID of the workflow run."""

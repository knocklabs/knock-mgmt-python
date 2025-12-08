# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["WorkflowActivateResponse"]


class WorkflowActivateResponse(BaseModel):
    """Wraps the Workflow response under the `workflow` key."""

    workflow: "Workflow"
    """A workflow object."""


from .workflow import Workflow

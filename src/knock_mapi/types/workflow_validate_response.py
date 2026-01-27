# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["WorkflowValidateResponse"]


class WorkflowValidateResponse(BaseModel):
    """Wraps the Workflow response under the `workflow` key."""

    workflow: "Workflow"
    """A workflow object.

    Read more in the [docs](https://docs.knock.app/concepts/workflows).
    """


from .workflow import Workflow

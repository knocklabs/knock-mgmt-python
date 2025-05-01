# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["WorkflowActivateResponse"]


class WorkflowActivateResponse(BaseModel):
    workflow: "Workflow"
    """A workflow object."""


from .workflow import Workflow

if PYDANTIC_V2:
    WorkflowActivateResponse.model_rebuild()
else:
    WorkflowActivateResponse.update_forward_refs()  # type: ignore

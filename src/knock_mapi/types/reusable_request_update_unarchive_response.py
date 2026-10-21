# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .reusable_request import ReusableRequest

__all__ = ["ReusableRequestUpdateUnarchiveResponse"]


class ReusableRequestUpdateUnarchiveResponse(BaseModel):
    """Wraps the ReusableRequest response under the `reusable_request` key."""

    reusable_request: ReusableRequest
    """A reusable HTTP request that workflows can link to."""

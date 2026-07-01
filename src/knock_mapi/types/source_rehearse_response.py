# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourceRehearseResponse", "Error"]


class Error(BaseModel):
    field: str

    message: str


class SourceRehearseResponse(BaseModel):
    """The result of a simulated source event rehearsal."""

    action_logs_count: int
    """The total number of action logs produced by the rehearsal."""

    failed_action_logs_count: int
    """The number of failed action logs produced by the rehearsal."""

    log_id: Optional[str] = None
    """The ID of the source event log created by the rehearsal."""

    status: Literal["ok", "error"]
    """Whether the rehearsal completed without action errors."""

    successful_action_logs_count: int
    """The number of successful action logs produced by the rehearsal."""

    errors: Optional[List[Error]] = None
    """Errors returned while rehearsing the source event."""

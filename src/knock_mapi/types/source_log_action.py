# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SourceLogAction"]


class SourceLogAction(BaseModel):
    """An action executed after receiving a source event."""

    id: str
    """The action log ID."""

    action_parameters: Optional[Dict[str, object]] = None
    """The configured mapping parameters used to derive the action payload."""

    action_payload: Optional[Dict[str, object]] = None
    """The parsed values generated from the mapping parameters for this action."""

    action_result: Optional[Dict[str, object]] = None
    """The result returned by the action."""

    action_status: Optional[str] = None
    """The status of the action."""

    action_type: Optional[str] = None
    """The type of action that was executed."""

    inserted_at: Optional[datetime] = None
    """The timestamp of when the action log was created."""

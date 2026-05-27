# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourceStatusResponse", "MappingsRequiringCommit"]


class MappingsRequiringCommit(BaseModel):
    action_type: Literal["workflows_trigger"]
    """The action that is performed when this mapping matches a source event."""

    event_type: str
    """The decoded event type that triggers the action."""

    is_deleted: bool
    """Whether the mapping is pending deletion."""

    resource_key: str
    """The key of the workflow resource referenced by the mapping."""

    status: Literal["deleted", "updated"]
    """Whether the mapping is pending deletion or update."""

    inactive_at: Optional[datetime] = None
    """The timestamp of when the mapping was deactivated."""


class SourceStatusResponse(BaseModel):
    """Status information for a source in an environment."""

    events_count: int
    """The number of source events received in the last 30 days."""

    last_event_received: Optional[str] = None
    """The timestamp of the most recently received source event."""

    mappings_count: int
    """The total number of event action mappings for the source environment."""

    mappings_requiring_commit: List[MappingsRequiringCommit]
    """
    Workflow trigger event action mappings that need a workflow commit before their
    changes are applied.
    """

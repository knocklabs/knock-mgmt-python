# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourceEventActionMapping"]


class SourceEventActionMapping(BaseModel):
    """An action mapping attached to a source event."""

    action_type: Literal[
        "workflows_trigger",
        "users_identify",
        "users_delete",
        "objects_set",
        "objects_delete",
        "objects_subscribe",
        "objects_unsubscribe",
        "tenants_set",
        "tenants_delete",
        "audiences_add_member",
        "audiences_remove_member",
    ]
    """The action that is performed when this mapping matches a source event."""

    active: bool
    """Whether the mapping is active. Inactive mappings are skipped during execution."""

    created_at: datetime
    """The timestamp of when the mapping was created."""

    event_type: str
    """The decoded event type that triggers the action."""

    is_deleted: bool
    """Whether the mapping has been deleted.

    When true, this indicates the trigger is present in the workflow's published
    version and may be active until the workflow is committed and published.
    """

    updated_at: datetime
    """The timestamp of when the mapping was last updated."""

    action_parameters: Optional[Dict[str, object]] = None
    """The action-specific parameters for the mapping."""

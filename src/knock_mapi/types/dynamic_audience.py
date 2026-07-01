# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .audience_condition import AudienceCondition

__all__ = ["DynamicAudience", "Segment"]


class Segment(BaseModel):
    conditions: List[AudienceCondition]
    """A list of conditions within this segment, joined by AND."""


class DynamicAudience(BaseModel):
    """
    A dynamic audience where membership is determined by segment conditions evaluated at runtime.
    """

    created_at: datetime
    """The timestamp of when the audience was created."""

    environment: str
    """The slug of the environment in which the audience exists."""

    key: str
    """The unique key of the audience."""

    name: str
    """The name of the audience."""

    segments: List[Segment]
    """A list of segments that define the dynamic audience membership criteria.

    Each segment contains one or more conditions joined by AND. Multiple segments
    are joined by OR.
    """

    type: Literal["dynamic"]
    """The type of audience. Always `dynamic` for dynamic audiences."""

    updated_at: datetime
    """The timestamp of when the audience was last updated."""

    description: Optional[str] = None
    """A description of the audience."""

    sha: Optional[str] = None
    """The SHA hash of the audience data."""

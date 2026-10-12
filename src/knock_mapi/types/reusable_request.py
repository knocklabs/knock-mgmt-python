# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup
from .reusable_request_settings import ReusableRequestSettings

__all__ = ["ReusableRequest"]


class ReusableRequest(BaseModel):
    """A reusable HTTP request that workflows can link to."""

    created_at: datetime
    """The timestamp of when the reusable request was created."""

    environment: str
    """The slug of the environment in which the reusable request exists."""

    key: str
    """The unique key for the reusable request.

    Must be 3 to 255 characters and match ^[a-z0-9_-]+$.
    """

    settings: ReusableRequestSettings
    """The HTTP request a reusable request runs."""

    type: Literal["http_fetch"]
    """The reusable request type. Only http_fetch is supported."""

    updated_at: datetime
    """The timestamp of when the reusable request was last updated."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An internal note about the reusable request."""

    name: Optional[str] = None
    """A name for the reusable request."""

    sha: Optional[str] = None
    """The SHA hash of the reusable request."""

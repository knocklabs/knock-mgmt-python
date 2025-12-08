# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Environment"]


class Environment(BaseModel):
    """An environment object."""

    created_at: datetime
    """The timestamp of when the environment was created."""

    name: str
    """A human-readable name for the environment. Cannot exceed 255 characters."""

    order: int
    """The order of the environment.

    The lowest number is the first environment, the highest number is the last
    environment. The order will not always be sequential.
    """

    owner: Literal["system", "user"]
    """The owner of the environment."""

    slug: str
    """A unique slug for the environment. Cannot exceed 255 characters."""

    updated_at: datetime
    """The timestamp of when the environment was last updated."""

    deleted_at: Optional[datetime] = None
    """The timestamp of when the environment was deleted."""

    hide_pii_data: Optional[bool] = None
    """Whether PII data is hidden from the environment.

    Read more in the
    [data obfuscation docs](https://docs.knock.app/manage-your-account/data-obfuscation).
    """

    label_color: Optional[str] = None
    """The color of the environment label to display in the dashboard."""

    last_commit_at: Optional[datetime] = None
    """The timestamp of the most-recent commit in the environment."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .guide_step import GuideStep
from .condition_group import ConditionGroup

__all__ = ["Guide", "ActivationLocationRule"]


class ActivationLocationRule(BaseModel):
    directive: Literal["allow", "block"]
    """Whether to allow or block the guide at the specified pathname."""

    pathname: str
    """The URL pathname pattern to match against. Must be a valid URI path."""


class Guide(BaseModel):
    active: bool
    """Whether the guide is active."""

    created_at: datetime
    """The timestamp of when the guide was created."""

    environment: str
    """The slug of the environment in which the guide exists."""

    key: str
    """The unique key string for the guide object.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the guide. Must be at maximum 255 characters in length."""

    sha: str
    """The SHA hash of the guide."""

    updated_at: datetime
    """The timestamp of when the guide was last updated."""

    activation_location_rules: Optional[List[ActivationLocationRule]] = None
    """
    A list of activation location rules that describe when the guide should be
    shown.
    """

    archived_at: Optional[datetime] = None
    """The timestamp of when the guide was archived."""

    channel_key: Optional[str] = None
    """The key of the channel in which the guide exists."""

    deleted_at: Optional[datetime] = None
    """The timestamp of when the guide was deleted."""

    description: Optional[str] = None
    """An arbitrary string attached to a guide object.

    Useful for adding notes about the guide for internal purposes. Maximum of 280
    characters allowed.
    """

    semver: Optional[str] = None
    """The semver of the guide."""

    steps: Optional[List[GuideStep]] = None
    """A list of guide step objects in the guide."""

    target_audience_id: Optional[str] = None
    """The ID of the target audience for the guide."""

    target_property_conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    type: Optional[str] = None
    """The type of the guide."""

    valid: Optional[bool] = None
    """Whether the guide is valid."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .guide_step_param import GuideStepParam
from .condition_group_param import ConditionGroupParam

__all__ = ["GuideValidateParams", "Guide", "GuideActivationURLPattern"]


class GuideValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    guide: Required[Guide]
    """A request to create or update a guide."""


class GuideActivationURLPattern(TypedDict, total=False):
    directive: Required[Literal["allow", "block"]]
    """Whether to allow or block the guide at the specified pathname."""

    pathname: Required[str]
    """The URL pathname pattern to match against. Must be a valid URI path."""


class Guide(TypedDict, total=False):
    channel_key: Required[str]
    """The key of the channel in which the guide exists."""

    name: Required[str]
    """A name for the guide. Must be at maximum 255 characters in length."""

    steps: Required[Iterable[GuideStepParam]]
    """A list of guide step objects in the guide."""

    activation_url_patterns: Iterable[GuideActivationURLPattern]
    """A list of activation url patterns that describe when the guide should be shown."""

    archived_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp of when the guide was archived."""

    deleted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp of when the guide was deleted."""

    description: Optional[str]
    """An arbitrary string attached to a guide object.

    Useful for adding notes about the guide for internal purposes. Maximum of 280
    characters allowed.
    """

    target_audience_id: Optional[str]
    """The ID of the target audience for the guide.

    When not set, will default to targeting all users.
    """

    target_property_conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

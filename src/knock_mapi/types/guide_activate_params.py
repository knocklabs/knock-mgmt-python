# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["GuideActivateParams", "GuideBooleanActivationParams", "GuideScheduledActivationParams"]


class GuideBooleanActivationParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    status: Required[bool]
    """Whether to activate or deactivate the guide."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """


class GuideScheduledActivationParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """When to activate the guide.

    If provided, the guide will be scheduled to activate at this time. Must be in
    ISO 8601 UTC format.
    """

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When to deactivate the guide.

    If provided, the guide will be scheduled to deactivate at this time. Must be in
    ISO 8601 UTC format.
    """


GuideActivateParams: TypeAlias = Union[GuideBooleanActivationParams, GuideScheduledActivationParams]

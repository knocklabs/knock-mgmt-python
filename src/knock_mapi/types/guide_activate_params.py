# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["GuideActivateParams", "GuideBooleanActivationParams", "GuideScheduledActivationParams"]


class GuideBooleanActivationParams(TypedDict, total=False):
    status: Required[bool]
    """Whether to activate or deactivate the guide."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""


class GuideScheduledActivationParams(TypedDict, total=False):
    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

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

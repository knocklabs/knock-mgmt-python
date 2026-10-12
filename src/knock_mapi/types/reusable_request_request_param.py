# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam
from .reusable_request_settings_param import ReusableRequestSettingsParam

__all__ = ["ReusableRequestRequestParam"]


class ReusableRequestRequestParam(TypedDict, total=False):
    """
    A reusable request object with attributes to update or create a reusable request.
    """

    settings: Required[ReusableRequestSettingsParam]
    """The HTTP request a reusable request runs."""

    type: Required[Literal["http_fetch"]]
    """The reusable request type. Only http_fetch is supported."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An internal note about the reusable request."""

    name: Optional[str]
    """A name for the reusable request."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .audience_condition_param import AudienceConditionParam

__all__ = ["AudienceRequestParam", "StaticAudienceRequest", "DynamicAudienceRequest", "DynamicAudienceRequestSegment"]


class StaticAudienceRequest(TypedDict, total=False):
    """Request body for creating/updating a static audience."""

    name: Required[str]
    """The name of the audience."""

    type: Required[Literal["static"]]
    """The type of audience. Set to `static` for static audiences."""

    description: Optional[str]
    """A description of the audience."""


class DynamicAudienceRequestSegment(TypedDict, total=False):
    conditions: Required[Iterable[AudienceConditionParam]]
    """A list of conditions within this segment, joined by AND."""


class DynamicAudienceRequest(TypedDict, total=False):
    """Request body for creating/updating a dynamic audience."""

    name: Required[str]
    """The name of the audience."""

    type: Required[Literal["dynamic"]]
    """The type of audience. Set to `dynamic` for dynamic audiences."""

    description: Optional[str]
    """A description of the audience."""

    segments: Iterable[DynamicAudienceRequestSegment]
    """A list of segments that define the dynamic audience membership criteria.

    Each segment contains one or more conditions joined by AND. Multiple segments
    are joined by OR.
    """


AudienceRequestParam: TypeAlias = Union[StaticAudienceRequest, DynamicAudienceRequest]

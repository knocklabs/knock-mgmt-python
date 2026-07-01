# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .audience_condition_param import AudienceConditionParam

__all__ = [
    "AudienceUpsertParams",
    "Audience",
    "AudienceStaticAudienceRequest",
    "AudienceDynamicAudienceRequest",
    "AudienceDynamicAudienceRequestSegment",
]


class AudienceUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    audience: Required[Audience]
    """An audience object with attributes to create or update an audience.

    Use `type: static` for audiences with explicitly managed members, or
    `type: dynamic` for audiences with segment-based membership.
    """

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""

    force: bool
    """
    When set to true, forces the upsert to override existing content regardless of
    environment restrictions. This bypasses the development-only environment check
    and origin environment checks.
    """


class AudienceStaticAudienceRequest(TypedDict, total=False):
    """Request body for creating/updating a static audience."""

    name: Required[str]
    """The name of the audience."""

    type: Required[Literal["static"]]
    """The type of audience. Set to `static` for static audiences."""

    description: Optional[str]
    """A description of the audience."""


class AudienceDynamicAudienceRequestSegment(TypedDict, total=False):
    conditions: Required[Iterable[AudienceConditionParam]]
    """A list of conditions within this segment, joined by AND."""


class AudienceDynamicAudienceRequest(TypedDict, total=False):
    """Request body for creating/updating a dynamic audience."""

    name: Required[str]
    """The name of the audience."""

    type: Required[Literal["dynamic"]]
    """The type of audience. Set to `dynamic` for dynamic audiences."""

    description: Optional[str]
    """A description of the audience."""

    segments: Iterable[AudienceDynamicAudienceRequestSegment]
    """A list of segments that define the dynamic audience membership criteria.

    Each segment contains one or more conditions joined by AND. Multiple segments
    are joined by OR.
    """


Audience: TypeAlias = Union[AudienceStaticAudienceRequest, AudienceDynamicAudienceRequest]

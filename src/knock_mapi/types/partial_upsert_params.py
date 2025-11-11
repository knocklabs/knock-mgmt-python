# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PartialUpsertParams", "Partial"]


class PartialUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    partial: Required[Partial]
    """A partial object with attributes to update or create a partial."""

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


class Partial(TypedDict, total=False):
    content: Required[str]
    """The content of the partial."""

    name: Required[str]
    """The name of the partial."""

    type: Required[Literal["html", "text", "json", "markdown"]]
    """The type of the partial."""

    description: Optional[str]
    """The description of the partial."""

    icon_name: Optional[str]
    """The name of the icon to be used in the visual editor.

    Only relevant when `visual_block_enabled` is `true`.
    """

    visual_block_enabled: Optional[bool]
    """Indicates whether the partial can be used in the visual editor.

    Only applies to HTML partials.
    """

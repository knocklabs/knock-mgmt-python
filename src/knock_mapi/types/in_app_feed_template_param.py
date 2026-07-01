# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["InAppFeedTemplateParam", "ActionButton"]


class ActionButton(TypedDict, total=False):
    """A single-action button to be rendered in an in-app feed cell."""

    action: Required[str]
    """The URI for this action."""

    label: Required[str]
    """The label of the action button."""


class InAppFeedTemplateParam(TypedDict, total=False):
    """An in-app feed template."""

    markdown_body: Required[str]
    """The markdown body of the in-app feed."""

    action_buttons: Iterable[ActionButton]
    """The action buttons of the in-app feed message."""

    action_url: Optional[str]
    """The URL to navigate to when the in-app feed is tapped.

    Can be omitted for multi-action templates, where the action buttons will be used
    instead.
    """

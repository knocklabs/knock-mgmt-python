# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["InAppFeedTemplate", "ActionButton"]


class ActionButton(BaseModel):
    action: str
    """The URI for this action."""

    label: str
    """The label of the action button."""


class InAppFeedTemplate(BaseModel):
    markdown_body: str
    """The markdown body of the in-app feed."""

    action_buttons: Optional[List[ActionButton]] = None
    """The action buttons of the in-app feed message."""

    action_url: Optional[str] = None
    """The URL to navigate to when the in-app feed is tapped.

    Can be omitted for multi-action templates, where the action buttons will be used
    instead.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatTemplateParam"]


class ChatTemplateParam(TypedDict, total=False):
    """A chat template."""

    markdown_body: Required[str]
    """The markdown body of the chat template."""

    json_body: Optional[str]
    """A JSON template for the chat notification message payload.

    Only present if not using the markdown body.
    """

    summary: str
    """The summary of the chat template.

    Used by some chat apps in their push notifications.
    """

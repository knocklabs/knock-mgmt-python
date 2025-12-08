# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatTemplate"]


class ChatTemplate(BaseModel):
    """A chat template."""

    markdown_body: str
    """The markdown body of the chat template."""

    json_body: Optional[str] = None
    """A JSON template for the chat notification message payload.

    Only present if not using the markdown body.
    """

    summary: Optional[str] = None
    """The summary of the chat template.

    Used by some chat apps in their push notifications.
    """

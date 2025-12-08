# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EmailLayout", "FooterLink"]


class FooterLink(BaseModel):
    text: str
    """The text to display as the link."""

    url: str
    """The URL to link to."""


class EmailLayout(BaseModel):
    """A versioned email layout used within an environment."""

    created_at: datetime
    """The timestamp of when the email layout was created."""

    html_layout: str
    """The complete HTML content of the email layout."""

    key: str
    """The unique key for this email layout."""

    name: str
    """The human-readable name of this email layout."""

    sha: str
    """The SHA of the email layout."""

    text_layout: str
    """The complete plaintext content of the email layout."""

    environment: Optional[str] = None
    """The environment of the email layout."""

    footer_links: Optional[List[FooterLink]] = None
    """A list of one or more items to show in the footer of the email layout."""

    updated_at: Optional[datetime] = None
    """The timestamp of when the email layout was last updated."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EmailLayout", "BrandingOverrides", "FooterLink"]


class BrandingOverrides(BaseModel):
    """
    Overrides to apply against account branding variables in an email layout, including dark mode-specific values.
    """

    dark_icon_url: Optional[str] = None
    """A URL for a dark mode icon override."""

    dark_logo_url: Optional[str] = None
    """A URL for a dark mode logo override."""

    dark_primary_color: Optional[str] = None
    """The dark mode primary brand color in hex format."""

    dark_primary_color_contrast: Optional[str] = None
    """The dark mode contrast color for the primary brand color in hex format."""

    icon_url: Optional[str] = None
    """A URL for a light mode icon override."""

    logo_url: Optional[str] = None
    """A URL for a light mode logo override."""

    primary_color: Optional[str] = None
    """The light mode primary brand color in hex format."""

    primary_color_contrast: Optional[str] = None
    """The light mode contrast color for the primary brand color in hex format."""

    primary_text_color: Optional[str] = None
    """The light mode primary text color in hex format."""

    secondary_text_color: Optional[str] = None
    """The light mode secondary text color in hex format."""


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
    """The complete HTML or MJML content of the email layout."""

    key: str
    """The unique key for this email layout."""

    name: str
    """The human-readable name of this email layout."""

    sha: str
    """The SHA of the email layout."""

    text_layout: str
    """The complete plaintext content of the email layout."""

    branding_overrides: Optional[BrandingOverrides] = None
    """
    Overrides to apply against account branding variables in an email layout,
    including dark mode-specific values.
    """

    environment: Optional[str] = None
    """The environment of the email layout."""

    footer_links: Optional[List[FooterLink]] = None
    """A list of one or more items to show in the footer of the email layout."""

    is_mjml: Optional[bool] = None
    """Whether this layout uses MJML format.

    When true, html_layout must contain <mjml> tags.
    """

    updated_at: Optional[datetime] = None
    """The timestamp of when the email layout was last updated."""

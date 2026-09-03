# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrandingOverrides"]


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

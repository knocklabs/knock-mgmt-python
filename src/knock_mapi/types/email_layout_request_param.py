# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .branding_overrides_param import BrandingOverridesParam

__all__ = ["EmailLayoutRequestParam", "FooterLink"]


class FooterLink(TypedDict, total=False):
    text: Required[str]
    """The text to display as the link."""

    url: Required[str]
    """The URL to link to."""


class EmailLayoutRequestParam(TypedDict, total=False):
    """A request to update or create an email layout."""

    html_layout: Required[str]
    """The complete HTML or MJML content of the email layout."""

    name: Required[str]
    """The friendly name of this email layout."""

    text_layout: Required[str]
    """The complete plain text content of the email layout."""

    branding_overrides: Optional[BrandingOverridesParam]
    """
    Overrides to apply against account branding variables in an email layout,
    including dark mode-specific values.
    """

    footer_links: Iterable[FooterLink]
    """A list of one or more items to show in the footer of the email layout."""

    is_mjml: Optional[bool]
    """Whether this layout uses MJML format.

    When true, html_layout must contain <mjml> tags.
    """

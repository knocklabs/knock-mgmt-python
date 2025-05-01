# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["EmailLayoutValidateParams", "EmailLayout", "EmailLayoutFooterLink"]


class EmailLayoutValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    email_layout: Required[EmailLayout]
    """A request to update or create an email layout."""


class EmailLayoutFooterLink(TypedDict, total=False):
    text: Required[str]
    """The text to display as the link."""

    url: Required[str]
    """The URL to link to."""


class EmailLayout(TypedDict, total=False):
    html_layout: Required[str]
    """The complete HTML content of the email layout."""

    name: Required[str]
    """The friendly name of this email layout."""

    text_layout: Required[str]
    """The complete plain text content of the email layout."""

    footer_links: Iterable[EmailLayoutFooterLink]
    """A list of one or more items to show in the footer of the email layout."""

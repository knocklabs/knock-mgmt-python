# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmailLayoutValidateParams", "EmailLayout", "EmailLayoutFooterLink"]


class EmailLayoutValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    email_layout: Required[EmailLayout]
    """A request to update or create an email layout."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """


class EmailLayoutFooterLink(TypedDict, total=False):
    text: Required[str]
    """The text to display as the link."""

    url: Required[str]
    """The URL to link to."""


class EmailLayout(TypedDict, total=False):
    """A request to update or create an email layout."""

    html_layout: Required[str]
    """The complete HTML or MJML content of the email layout."""

    name: Required[str]
    """The friendly name of this email layout."""

    text_layout: Required[str]
    """The complete plain text content of the email layout."""

    footer_links: Iterable[EmailLayoutFooterLink]
    """A list of one or more items to show in the footer of the email layout."""

    is_mjml: Optional[bool]
    """Whether this layout uses MJML format.

    When true, html_layout must contain <mjml> tags.
    """

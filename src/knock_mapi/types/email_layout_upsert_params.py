# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["EmailLayoutUpsertParams", "EmailLayout", "EmailLayoutFooterLink"]


class EmailLayoutUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    email_layout: Required[EmailLayout]
    """A request to update or create an email layout."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""


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

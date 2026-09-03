# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .email_layout_request_param import EmailLayoutRequestParam

__all__ = ["EmailLayoutUpsertParams"]


class EmailLayoutUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    email_layout: Required[EmailLayoutRequestParam]
    """A request to update or create an email layout."""

    allow_empty: bool
    """
    When used with commit, creates a new version with identical content and commits
    it if there are no unpublished changes.
    """

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""

    force: bool
    """
    When set to true, forces the upsert to override existing content regardless of
    environment restrictions. This bypasses the development-only environment check
    and origin environment checks.
    """

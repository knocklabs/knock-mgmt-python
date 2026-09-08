# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .audience_request_param import AudienceRequestParam

__all__ = ["AudienceUpsertParams"]


class AudienceUpsertParams(TypedDict, total=False):
    audience: Required[AudienceRequestParam]
    """An audience object with attributes to create or update an audience.

    Use `type: static` for audiences with explicitly managed members, or
    `type: dynamic` for audiences with segment-based membership.
    """

    allow_empty: bool
    """
    When used with commit, creates a new version with identical content and commits
    it if there are no unpublished changes.
    """

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    force: bool
    """
    When set to true, forces the upsert to override existing content regardless of
    environment restrictions. This bypasses the development-only environment check
    and origin environment checks.
    """

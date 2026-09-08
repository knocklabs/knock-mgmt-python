# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .translation_request_param import TranslationRequestParam

__all__ = ["TranslationUpsertParams"]


class TranslationUpsertParams(TypedDict, total=False):
    namespace: Required[str]
    """An optional namespace that identifies the translation."""

    translation: Required[TranslationRequestParam]
    """
    A translation object with a content attribute used to update or create a
    translation.
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

    format: Literal["json", "po"]
    """Optionally specify the returned content format.

    Supports 'json' and 'po'. Defaults to 'json'.
    """

    tenant: str
    """An optional tenant to scope the translation to."""

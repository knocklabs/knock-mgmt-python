# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranslationListParams"]


class TranslationListParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    after: str
    """The cursor to fetch entries after."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    before: str
    """The cursor to fetch entries before."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    format: Literal["json", "po"]
    """Optionally specify the returned content format.

    Supports 'json' and 'po'. Defaults to 'json'.
    """

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """

    limit: int
    """The number of entries to fetch per-page."""

    locale_code: str
    """A specific locale code to filter translations for."""

    namespace: str
    """A specific namespace to filter translations for."""

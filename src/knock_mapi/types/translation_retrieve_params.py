# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranslationRetrieveParams"]


class TranslationRetrieveParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    format: Literal["json", "po"]
    """Optionally specify the returned content format.

    Supports 'json' and 'po'. Defaults to 'json'.
    """

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """

    namespace: str
    """A specific namespace to filter translations for."""

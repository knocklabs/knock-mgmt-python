# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranslationRetrieveParams"]


class TranslationRetrieveParams(TypedDict, total=False):
    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

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

    tenant: str
    """A specific tenant to scope the translation to."""

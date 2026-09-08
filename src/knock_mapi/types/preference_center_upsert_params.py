# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PreferenceCenterUpsertParams"]


class PreferenceCenterUpsertParams(TypedDict, total=False):
    config: Required[object]
    """The preference center configuration document."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    enabled: bool
    """Whether the preference center is enabled for recipients."""

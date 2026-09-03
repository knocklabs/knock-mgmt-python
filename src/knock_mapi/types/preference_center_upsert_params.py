# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PreferenceCenterUpsertParams"]


class PreferenceCenterUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    config: Required[object]
    """The preference center configuration document."""

    enabled: bool
    """Whether the preference center is enabled for recipients."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WarehouseSyncUpdateSettingsParams"]


class WarehouseSyncUpdateSettingsParams(TypedDict, total=False):
    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    enabled: bool
    """Whether the sync runs on its schedule."""

    frequency_minutes: Literal[10, 15, 60, 360, 720, 1440]
    """How often the sync runs, in minutes."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GoalCloneParams", "Clone"]


class GoalCloneParams(TypedDict, total=False):
    clone: Required[Clone]
    """The destination key, name, and environment for the cloned goal."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""


class Clone(TypedDict, total=False):
    """The destination key, name, and environment for the cloned goal."""

    environment: Required[str]
    """The destination environment slug."""

    key: Required[str]
    """The key for the cloned goal."""

    name: Required[str]
    """The name for the cloned goal."""

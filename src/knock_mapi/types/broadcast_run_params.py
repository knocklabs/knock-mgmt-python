# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BroadcastRunParams", "Recipient", "Settings"]


class BroadcastRunParams(TypedDict, total=False):
    recipient: Required[Recipient]
    """The user to run the broadcast for."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    settings: Settings
    """Settings that control how the broadcast run executes."""

    tenant: Optional[str]
    """The tenant to associate the broadcast run with. Must not contain whitespace."""


class Recipient(TypedDict, total=False):
    """The user to run the broadcast for."""

    id: Required[str]
    """The ID of the user."""


class Settings(TypedDict, total=False):
    """Settings that control how the broadcast run executes."""

    sandbox_mode: bool
    """Whether to generate messages without sending them to downstream providers."""

    skip_delay: bool
    """Whether to skip delay steps during the run."""

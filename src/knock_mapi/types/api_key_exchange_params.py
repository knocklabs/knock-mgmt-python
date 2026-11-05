# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["APIKeyExchangeParams"]


class APIKeyExchangeParams(TypedDict, total=False):
    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    type: Literal["secret", "public"]
    """The type of API key to return: `secret` or `public`."""

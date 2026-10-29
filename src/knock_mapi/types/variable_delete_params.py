# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VariableDeleteParams"]


class VariableDeleteParams(TypedDict, total=False):
    environment: str
    """The environment slug.

    When provided, only the variable's override for this environment is cleared.
    When omitted, the whole variable is deleted, which requires `variables:manage`
    in the account's default environment and in every environment with an override.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AttachmentDeleteParams"]


class AttachmentDeleteParams(TypedDict, total=False):
    goal_key: Required[str]

    resource_type: Required[Literal["workflow", "guide", "broadcast"]]

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

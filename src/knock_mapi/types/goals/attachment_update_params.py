# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AttachmentUpdateParams", "Attachment"]


class AttachmentUpdateParams(TypedDict, total=False):
    goal_key: Required[str]

    resource_type: Required[Literal["workflow", "guide", "broadcast"]]

    attachment: Required[Attachment]
    """Settings for the goal attachment."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""


class Attachment(TypedDict, total=False):
    """Settings for the goal attachment."""

    attribution_window_days: int
    """
    The number of days after a message is sent in which a goal completion is
    attributed to it. Must be between 1 and 30. When omitted, re-saving the attached
    goal keeps its window; otherwise 7.
    """

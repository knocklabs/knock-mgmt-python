# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .goal_request_param import GoalRequestParam

__all__ = ["GoalUpsertParams"]


class GoalUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    goal: Required[GoalRequestParam]
    """A goal payload for upsert or validate."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

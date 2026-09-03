# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .goal_request_param import GoalRequestParam

__all__ = ["GoalValidateParams"]


class GoalValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    goal: Required[GoalRequestParam]
    """A goal payload for upsert or validate."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

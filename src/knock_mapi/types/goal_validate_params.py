# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .goal_request_param import GoalRequestParam

__all__ = ["GoalValidateParams"]


class GoalValidateParams(TypedDict, total=False):
    goal: Required[GoalRequestParam]
    """A goal payload for upsert or validate."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

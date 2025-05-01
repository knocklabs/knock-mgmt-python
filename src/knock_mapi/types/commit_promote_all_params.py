# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommitPromoteAllParams"]


class CommitPromoteAllParams(TypedDict, total=False):
    to_environment: Required[str]
    """
    A slug of the target environment to which you want to promote all changes from
    its directly preceding environment.

    For example, if you have three environments “development”, “staging”, and
    “production” (in that order), setting this param to “production” will promote
    all commits not currently in production from staging.

    Note: This must be a non-development environment.
    """

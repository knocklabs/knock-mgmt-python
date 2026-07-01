# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommitPromoteAllParams"]


class CommitPromoteAllParams(TypedDict, total=False):
    to_environment: Required[str]
    """
    A slug of the target environment to which you want to promote all changes from
    its directly preceding environment.

    For example, if you have three environments “development”, “staging”, and
    “production” (in that order), setting this param to “production” will promote
    all commits not currently in production from staging.

    When this param is set to `"development"`, the `"branch"` param must be
    provided.
    """

    branch: str
    """The slug of the branch to promote all changes from."""

    resource_id: str
    """Filter commits to promote by resource identifier.

    Must be used together with resource_type.
    """

    resource_type: Union[
        Literal["audience", "email_layout", "guide", "message_type", "partial", "translation", "workflow"],
        List[Literal["audience", "email_layout", "guide", "message_type", "partial", "translation", "workflow"]],
    ]
    """Filter commits to promote by resource type(s).

    Accepts a single type or array of types. Can be combined with resource_id to
    filter for specific resources.
    """

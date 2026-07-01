# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowActivateParams"]


class WorkflowActivateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    status: Required[bool]
    """Whether to activate or deactivate the workflow.

    Set to `true` by default, which will activate the workflow.
    """

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

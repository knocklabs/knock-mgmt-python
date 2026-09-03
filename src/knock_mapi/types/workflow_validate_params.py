# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowValidateParams"]


class WorkflowValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    workflow: Required["WorkflowRequestParam"]
    """A workflow request for upserting a workflow."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """


from .workflow_request_param import WorkflowRequestParam

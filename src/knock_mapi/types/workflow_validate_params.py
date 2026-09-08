# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowValidateParams"]


class WorkflowValidateParams(TypedDict, total=False):
    workflow: Required["WorkflowRequestParam"]
    """A workflow request for upserting a workflow."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""


from .workflow_request_param import WorkflowRequestParam

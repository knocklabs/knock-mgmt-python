# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkflowRetrieveParams"]


class WorkflowRetrieveParams(TypedDict, total=False):
    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .email_layout_request_param import EmailLayoutRequestParam

__all__ = ["EmailLayoutValidateParams"]


class EmailLayoutValidateParams(TypedDict, total=False):
    email_layout: Required[EmailLayoutRequestParam]
    """A request to update or create an email layout."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .email_layout_request_param import EmailLayoutRequestParam

__all__ = ["EmailLayoutValidateParams"]


class EmailLayoutValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    email_layout: Required[EmailLayoutRequestParam]
    """A request to update or create an email layout."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

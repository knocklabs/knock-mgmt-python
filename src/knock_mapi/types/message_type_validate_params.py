# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .message_type_request_param import MessageTypeRequestParam

__all__ = ["MessageTypeValidateParams"]


class MessageTypeValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    message_type: Required[MessageTypeRequestParam]
    """A request to create a message type."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

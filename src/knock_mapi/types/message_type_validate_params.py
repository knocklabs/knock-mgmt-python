# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .message_type_variant_param import MessageTypeVariantParam

__all__ = ["MessageTypeValidateParams", "MessageType"]


class MessageTypeValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    message_type: Required[MessageType]
    """A request to create a message type."""


class MessageType(TypedDict, total=False):
    description: Required[Optional[str]]
    """An arbitrary string attached to a message type object.

    Useful for adding notes about the message type for internal purposes. Maximum of
    280 characters allowed.
    """

    name: Required[str]
    """A name for the message type. Must be at maximum 255 characters in length."""

    preview: Required[str]
    """An HTML/liquid template for the message type preview."""

    icon_name: str
    """The icon name of the message type."""

    semver: str
    """The semantic version of the message type."""

    variants: Iterable[MessageTypeVariantParam]
    """The variants of the message type."""

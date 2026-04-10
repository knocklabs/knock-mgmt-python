# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .sms_template_param import SMSTemplateParam
from .chat_template_param import ChatTemplateParam
from .push_template_param import PushTemplateParam
from .email_template_param import EmailTemplateParam
from .in_app_feed_template_param import InAppFeedTemplateParam

__all__ = [
    "TemplatePreviewParams",
    "Recipient",
    "RecipientObjectRecipientReference",
    "Template",
    "Actor",
    "ActorObjectRecipientReference",
    "Layout",
]


class TemplatePreviewParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    channel_type: Required[Literal["email", "sms", "push", "chat", "in_app_feed"]]
    """The channel type of the template to preview."""

    recipient: Required[Recipient]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    template: Required[Template]
    """The template content to preview. Structure depends on channel_type."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    actor: Optional[Actor]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    data: Dict[str, object]
    """The data to pass to the template for rendering."""

    layout: Optional[Layout]
    """Email layout configuration.

    Only applicable for email channel type. Falls back to environment default if not
    provided.
    """

    tenant: Optional[str]
    """The tenant to associate with the preview. Must not contain whitespace."""


class RecipientObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


Recipient: TypeAlias = Union[str, RecipientObjectRecipientReference]

Template: TypeAlias = Union[
    EmailTemplateParam, SMSTemplateParam, PushTemplateParam, ChatTemplateParam, InAppFeedTemplateParam
]


class ActorObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


Actor: TypeAlias = Union[str, ActorObjectRecipientReference]


class Layout(TypedDict, total=False):
    """Email layout configuration.

    Only applicable for email channel type. Falls back to environment default if not provided.
    """

    html_content: Optional[str]
    """Inline HTML content for the layout. Must include `{{ content }}` placeholder."""

    key: Optional[str]
    """The key of an existing email layout to use."""

    text_content: Optional[str]
    """Inline text content for the layout."""

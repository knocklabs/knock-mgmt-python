# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .sms_template_param import SMSTemplateParam
from .chat_template_param import ChatTemplateParam
from .push_template_param import PushTemplateParam
from .email_template_param import EmailTemplateParam
from .in_app_feed_template_param import InAppFeedTemplateParam
from .shared_params.recipient_reference import RecipientReference

__all__ = ["TemplatePreviewParams", "Template", "Layout", "Workflow"]


class TemplatePreviewParams(TypedDict, total=False):
    channel_type: Required[Literal["email", "sms", "push", "chat", "in_app_feed"]]
    """The channel type of the template to preview."""

    recipient: Required[RecipientReference]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    template: Required[Template]
    """The template content to preview. Structure depends on channel_type."""

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    actor: Optional[RecipientReference]
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

    workflow: Optional[Workflow]
    """Optional workflow context for variable hydration.

    When provided, recipient/actor/tenant are resolved via Knock.
    """


Template: TypeAlias = Union[
    EmailTemplateParam, SMSTemplateParam, PushTemplateParam, ChatTemplateParam, InAppFeedTemplateParam
]


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


class Workflow(TypedDict, total=False):
    """Optional workflow context for variable hydration.

    When provided, recipient/actor/tenant are resolved via Knock.
    """

    key: Required[str]
    """The workflow key."""

    categories: Optional[SequenceNotStr[str]]
    """Workflow categories."""

    commercial: Optional[bool]
    """Whether the workflow is marked as commercial messaging."""

    override_preferences: Optional[bool]
    """Whether to ignore recipient preferences for a given type of notification.

    If true, will send for every channel in the workflow even if the recipient has
    opted out of a certain kind. Defaults to false.
    """

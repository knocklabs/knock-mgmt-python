# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .sms_template import SMSTemplate
from .chat_template import ChatTemplate
from .push_template import PushTemplate
from .email_template import EmailTemplate
from .in_app_feed_template import InAppFeedTemplate

__all__ = ["TemplatePreviewResponse", "Error", "Template"]


class Error(BaseModel):
    """A rendering error with optional location information."""

    message: str
    """A human-readable description of the error."""

    field: Optional[str] = None
    """The template field that caused the error, if available."""

    line: Optional[int] = None
    """The line number where the error occurred, if available."""


Template: TypeAlias = Union[EmailTemplate, InAppFeedTemplate, PushTemplate, ChatTemplate, SMSTemplate]


class TemplatePreviewResponse(BaseModel):
    """A response to a template preview request."""

    content_type: Literal["email", "in_app_feed", "push", "chat", "sms"]
    """The content type of the preview."""

    result: Literal["success", "error"]
    """The result of the preview."""

    errors: Optional[List[Error]] = None
    """A list of errors encountered during rendering. Present when result is "error"."""

    template: Optional[Template] = None
    """The rendered template, ready to be previewed."""

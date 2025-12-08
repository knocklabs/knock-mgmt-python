# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..sms_template import SMSTemplate
from ..chat_template import ChatTemplate
from ..push_template import PushTemplate
from ..email_template import EmailTemplate
from ..request_template import RequestTemplate
from ..in_app_feed_template import InAppFeedTemplate

__all__ = ["StepPreviewTemplateResponse", "Template"]

Template: TypeAlias = Union[EmailTemplate, InAppFeedTemplate, PushTemplate, ChatTemplate, SMSTemplate, RequestTemplate]


class StepPreviewTemplateResponse(BaseModel):
    """A response to a preview workflow template request."""

    content_type: Literal["email", "in_app_feed", "push", "chat", "sms", "http"]
    """The content type of the preview."""

    result: Literal["success", "error"]
    """The result of the preview."""

    template: Template
    """The rendered template, ready to be previewed."""

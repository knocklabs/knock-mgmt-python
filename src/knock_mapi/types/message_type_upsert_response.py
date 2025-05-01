# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .message_type import MessageType

__all__ = ["MessageTypeUpsertResponse"]


class MessageTypeUpsertResponse(BaseModel):
    message_type: MessageType
    """
    A message type is a schema for a message that maps to a UI component or element
    within your application.
    """

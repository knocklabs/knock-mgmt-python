# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AttachmentDeleteResponse"]


class AttachmentDeleteResponse(BaseModel):
    """The response from detaching a goal."""

    result: str
    """The result of the detach operation."""

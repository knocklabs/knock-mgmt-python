# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .goal_resource_attachment import GoalResourceAttachment

__all__ = ["AttachmentListResponse"]


class AttachmentListResponse(BaseModel):
    """The goal's attachments in the environment."""

    attachments: List[GoalResourceAttachment]
    """The goal's attachments in the environment."""

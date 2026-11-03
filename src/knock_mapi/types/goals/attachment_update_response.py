# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .goal_resource_attachment import GoalResourceAttachment

__all__ = ["AttachmentUpdateResponse"]


class AttachmentUpdateResponse(BaseModel):
    """Wraps the GoalResourceAttachment response under the `attachment` key."""

    attachment: GoalResourceAttachment
    """A goal attached to a workflow, guide, or broadcast in one environment.

    An attachment goes live without a commit.
    """

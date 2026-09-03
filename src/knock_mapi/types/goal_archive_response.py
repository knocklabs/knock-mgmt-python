# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GoalArchiveResponse"]


class GoalArchiveResponse(BaseModel):
    """The response from archiving a goal."""

    result: str
    """The result of the archive operation."""

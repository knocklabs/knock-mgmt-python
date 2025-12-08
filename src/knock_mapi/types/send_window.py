# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SendWindow"]


class SendWindow(BaseModel):
    """A send window time for a notification. Describes a single day."""

    day: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    """The day of the week."""

    type: Literal["send", "do_not_send"]
    """The type of send window."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The start time of the send window."""

    until: Optional[str] = None
    """The end time of the send window."""

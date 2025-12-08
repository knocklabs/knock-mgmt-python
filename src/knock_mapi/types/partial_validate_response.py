# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .partial import Partial
from .._models import BaseModel

__all__ = ["PartialValidateResponse"]


class PartialValidateResponse(BaseModel):
    """Wraps the Partial response under the `partial` key."""

    partial: Partial
    """A partial is a reusable piece of content that can be used in a template."""

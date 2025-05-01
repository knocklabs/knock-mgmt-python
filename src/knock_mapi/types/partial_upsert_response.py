# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .partial import Partial
from .._models import BaseModel

__all__ = ["PartialUpsertResponse"]


class PartialUpsertResponse(BaseModel):
    partial: Partial
    """A partial is a reusable piece of content that can be used in a template."""

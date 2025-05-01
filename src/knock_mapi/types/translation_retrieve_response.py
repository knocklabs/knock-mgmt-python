# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .translation import Translation

__all__ = ["TranslationRetrieveResponse"]


class TranslationRetrieveResponse(BaseModel):
    translation: Translation
    """A translation object."""

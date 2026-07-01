# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .translation import Translation

__all__ = ["TranslationUpsertResponse"]


class TranslationUpsertResponse(BaseModel):
    """Wraps the Translation response under the `translation` key."""

    translation: Translation
    """A translation object."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .preference_category import PreferenceCategory

__all__ = ["PreferenceCategoryListResponse"]


class PreferenceCategoryListResponse(BaseModel):
    """A list of preference categories in the project's catalog."""

    entries: List[PreferenceCategory]
    """Preference categories, ordered by name."""

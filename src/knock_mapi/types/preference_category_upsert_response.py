# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .preference_category import PreferenceCategory

__all__ = ["PreferenceCategoryUpsertResponse"]


class PreferenceCategoryUpsertResponse(BaseModel):
    """Wraps the PreferenceCategory response under the `preference_category` key."""

    preference_category: PreferenceCategory
    """A named preference category in a project's catalog."""

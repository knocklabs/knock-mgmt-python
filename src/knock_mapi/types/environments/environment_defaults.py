# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .environment_defaults_preference_set import EnvironmentDefaultsPreferenceSet

__all__ = ["EnvironmentDefaults"]


class EnvironmentDefaults(BaseModel):
    """The default settings for an environment."""

    created_at: Optional[datetime] = None
    """The timestamp of when the defaults were first set.

    Null when no defaults have been set.
    """

    preference_set: Optional[EnvironmentDefaultsPreferenceSet] = None
    """
    A preference set applied to every recipient in the environment unless the
    recipient overrides it. The `__persistence_strategy__` and `__strategy__` keys
    are not supported, because defaults are always replaced in full.
    """

    updated_at: Optional[datetime] = None
    """The timestamp of when the defaults were last updated.

    Null when no defaults have been set.
    """

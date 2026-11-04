# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .environment_defaults_preference_set_param import EnvironmentDefaultsPreferenceSetParam

__all__ = ["DefaultUpdateParams"]


class DefaultUpdateParams(TypedDict, total=False):
    preference_set: Required[Optional[EnvironmentDefaultsPreferenceSetParam]]
    """
    A preference set applied to every recipient in the environment unless the
    recipient overrides it. The `__persistence_strategy__` and `__strategy__` keys
    are not supported, because defaults are always replaced in full.
    """

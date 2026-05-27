# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .source_preprocess_script import SourcePreprocessScript
from .source_event_action_mapping import SourceEventActionMapping

__all__ = ["SourceEnvironmentSettings", "Settings"]


class Settings(BaseModel):
    """
    Source settings for this environment, including endpoint, verification behavior, and preprocess script.
    """

    endpoint: Optional[str] = None
    """The public endpoint that receives source events for this environment."""

    enforce_idempotency: Optional[bool] = None

    enforce_verification: Optional[bool] = None

    event_type_path: Optional[str] = None

    handle_identifies: Optional[bool] = None

    idempotency_key_path: Optional[str] = None

    preprocess_script: Optional[SourcePreprocessScript] = None
    """A script that runs before source events are mapped."""

    timestamp_path: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class SourceEnvironmentSettings(BaseModel):
    """Environment-specific settings for a source."""

    created_at: datetime
    """The timestamp of when these environment settings were created."""

    mappings: List[SourceEventActionMapping]
    """Event action mappings configured for this source in the environment."""

    settings: Settings
    """
    Source settings for this environment, including endpoint, verification behavior,
    and preprocess script.
    """

    updated_at: datetime
    """The timestamp of when these environment settings were last updated."""

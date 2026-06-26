# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .source_preprocess_script_param import SourcePreprocessScriptParam

__all__ = ["SourceRequestParam", "EnvironmentSettings", "EnvironmentSettingsMapping", "EnvironmentSettingsSettings"]


class EnvironmentSettingsMapping(TypedDict, total=False):
    """An action mapping to configure for a source event."""

    action_type: Required[
        Literal[
            "workflows_trigger",
            "users_identify",
            "users_delete",
            "objects_set",
            "objects_delete",
            "objects_subscribe",
            "objects_unsubscribe",
            "tenants_set",
            "tenants_delete",
            "audiences_add_member",
            "audiences_remove_member",
        ]
    ]
    """The action that is performed when this mapping matches a source event."""

    event_type: Required[str]
    """The decoded event type that triggers the action."""

    action_parameters: Optional[Dict[str, object]]
    """The action-specific parameters for the mapping."""

    active: bool
    """Whether the mapping is active.

    Set to false to deactivate the mapping without deleting it. Defaults to true.
    """

    is_deleted: bool
    """Whether to delete the mapping.

    Workflow trigger mappings must be marked deleted before they can be removed.
    """


class EnvironmentSettingsSettings(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Writable source settings for this environment."""

    enforce_verification: bool

    event_type_path: Optional[str]

    idempotency_key_path: Optional[str]

    preprocess_script: Optional[SourcePreprocessScriptParam]
    """A script that runs before source events are mapped."""

    timestamp_path: Optional[str]


class EnvironmentSettings(TypedDict, total=False):
    """Environment-specific source settings to configure."""

    mappings: Iterable[EnvironmentSettingsMapping]
    """Event action mappings to configure for this source in the environment."""

    settings: EnvironmentSettingsSettings
    """Writable source settings for this environment."""


class SourceRequestParam(TypedDict, total=False):
    """
    A source request for setting a source and its environment-specific configuration.
    """

    name: Required[str]
    """The human-readable name of the source."""

    custom_image_url: Optional[str]
    """An optional URL for a custom image representing the source."""

    description: Optional[str]
    """An optional description of the source."""

    environment_settings: Dict[str, EnvironmentSettings]
    """Per-environment settings keyed by environment slug."""

    preconfigured_provider: str
    """
    When creating a source, bootstraps configuration from a preconfigured provider
    template. Ignored when updating an existing source.
    """

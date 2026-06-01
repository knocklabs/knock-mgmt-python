# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SourceProviderResponse",
    "DefaultSettings",
    "DefaultSettingsPreprocessingScript",
    "Provider",
    "ProviderBranding",
    "ProviderBrandingWordmarkImages",
    "ProviderBrandingColors",
    "DefaultActionMapping",
    "ExamplePayload",
]


class DefaultSettingsPreprocessingScript(BaseModel):
    """Verification script source code.

    Only present when `include` contains `preprocessing_script`.
    """

    language: Literal["javascript"]
    """Script language."""

    source: str
    """Verification script source code."""


class DefaultSettings(BaseModel):
    """Default source settings for this provider."""

    enforce_verification: bool
    """Whether the source should enforce webhook verification."""

    event_type_path: str
    """Path to find the event type from the data."""

    idempotency_key_path: Optional[str] = None
    """Path to find the idempotency key from the data."""

    preprocessing_script: Optional[DefaultSettingsPreprocessingScript] = None
    """Verification script source code.

    Only present when `include` contains `preprocessing_script`.
    """

    timestamp_path: Optional[str] = None
    """Path to find the timestamp from the data."""


class ProviderBrandingWordmarkImages(BaseModel):
    dark: str
    """Wordmark image URL or path for dark backgrounds."""

    light: str
    """Wordmark image URL or path for light backgrounds."""


class ProviderBrandingColors(BaseModel):
    primary: str
    """Primary brand color."""

    secondary: str
    """Secondary brand color."""


class ProviderBranding(BaseModel):
    """Provider branding assets. Only present when `include` contains `branding`."""

    icon_image: str
    """Provider icon image URL or path."""

    wordmark_images: ProviderBrandingWordmarkImages

    colors: Optional[ProviderBrandingColors] = None


class Provider(BaseModel):
    """Provider display metadata."""

    categories: List[
        Literal["Billing", "Infrastructure", "Analytics", "CRM", "Ecommerce", "Communications", "Identity"]
    ]
    """Provider categories for filtering and grouping."""

    description: str
    """Provider display description."""

    name: str
    """Provider display name."""

    webhook_docs_url: str
    """Provider webhook documentation URL."""

    website_url: Optional[str] = None
    """Provider website URL."""

    branding: Optional[ProviderBranding] = None
    """Provider branding assets. Only present when `include` contains `branding`."""

    knock_tutorial_url: Optional[str] = None
    """Knock tutorial URL for setting up the provider."""

    webhook_config_deep_link: Optional[str] = None
    """Provider webhook configuration URL."""


class DefaultActionMapping(BaseModel):
    action_parameters: Dict[str, object]
    """Action-specific data paths and options."""

    action_type: Literal[
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
    """The action performed when the mapping matches a source event."""

    event_type: str
    """Event type to match."""


class ExamplePayload(BaseModel):
    body: Optional[Dict[str, object]] = None
    """Example payload body."""

    headers: Optional[Dict[str, object]] = None
    """Example payload headers."""


class SourceProviderResponse(BaseModel):
    """A source provider available for creating sources."""

    default_settings: DefaultSettings
    """Default source settings for this provider."""

    key: str
    """Provider key."""

    provider: Provider
    """Provider display metadata."""

    version: str
    """Provider version."""

    default_action_mappings: Optional[List[DefaultActionMapping]] = None
    """Default event action mappings for the provider.

    Only present when `include` contains `default_action_mappings`.
    """

    example_payloads: Optional[Dict[str, List[ExamplePayload]]] = None
    """Example payloads keyed by event type."""

    static_fields: Optional[Dict[str, object]] = None
    """JSON Schema fields needed to configure the source.

    Only present when `include` contains `static_fields`.
    """

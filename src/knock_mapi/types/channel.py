# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Channel", "EnvironmentSettings"]


class EnvironmentSettings(BaseModel):
    """Environment-specific settings for a channel."""

    id: str
    """The unique identifier for these environment settings."""

    is_sandbox: bool
    """Whether the channel is in sandbox mode for this environment.

    Sandbox mode may prevent actual message delivery.
    """

    is_valid: bool
    """
    Whether the channel configuration is valid and ready to send messages in this
    environment.
    """

    channel_settings: Optional[Dict[str, object]] = None
    """Channel-type-specific settings (e.g., from_address for email).

    Structure varies by channel type.
    """

    provider_settings: Optional[Dict[str, object]] = None
    """Provider-specific settings (e.g., API keys, credentials).

    Structure varies by provider. Secret values are obfuscated unless they are
    Liquid templates.
    """


class Channel(BaseModel):
    """A configured channel, which is a way to route messages to a provider."""

    id: str
    """The unique identifier for the channel."""

    created_at: datetime
    """The timestamp of when the channel was created."""

    key: str
    """Unique identifier for the channel within a project (immutable once created)."""

    name: str
    """The human-readable name of the channel."""

    provider: str
    """The ID of the provider that this channel uses to deliver messages.

    Learn more about the providers available
    [in our documentation](https://docs.knock.app/integrations/overview).
    """

    type: Literal["email", "in_app", "in_app_feed", "in_app_guide", "sms", "push", "chat", "http"]
    """The type of channel, determining what kind of messages it can send."""

    updated_at: datetime
    """The timestamp of when the channel was last updated."""

    archived_at: Optional[datetime] = None
    """The timestamp of when the channel was deleted."""

    custom_icon_url: Optional[str] = None
    """Optional URL to a custom icon for the channel.

    Only used for display purposes in the dashboard.
    """

    description: Optional[str] = None
    """Optional description of the channel's purpose or usage."""

    environment_settings: Optional[Dict[str, EnvironmentSettings]] = None
    """
    Per-environment settings for this channel, keyed by environment slug (e.g.,
    'development', 'production'). Only included when requested via the `include`
    parameter or when retrieving a single channel.
    """

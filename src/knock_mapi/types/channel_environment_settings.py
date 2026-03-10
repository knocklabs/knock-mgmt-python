# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ChannelEnvironmentSettings"]


class ChannelEnvironmentSettings(BaseModel):
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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from ..._models import BaseModel

__all__ = ["EnvironmentDefaultsPreferenceSet"]


class EnvironmentDefaultsPreferenceSet(BaseModel):
    """
    A preference set applied to every recipient in the environment unless the recipient overrides it. The `__persistence_strategy__` and `__strategy__` keys are not supported, because defaults are always replaced in full.
    """

    categories: Optional[object] = None
    """
    A map of category key to a boolean or an object containing `channel_types`,
    `channels`, and `conditions`.
    """

    channel_types: Optional[object] = None
    """A map of channel type to a boolean or an object containing `conditions`.

    Valid channel types are `email`, `sms`, `push`, `chat`, `in_app_feed`, and
    `http`.
    """

    channels: Optional[object] = None
    """A map of channel ID to a boolean or an object containing `conditions`."""

    commercial_subscribed: Union[bool, object, None] = None
    """
    Whether the recipient is subscribed to commercial messages, as a boolean or a
    settings object.
    """

    workflows: Optional[object] = None
    """
    A map of workflow key to a boolean or an object containing `channel_types`,
    `channels`, and `conditions`.
    """

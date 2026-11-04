# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["EnvironmentDefaultsPreferenceSetParam"]


class EnvironmentDefaultsPreferenceSetParam(TypedDict, total=False):
    """
    A preference set applied to every recipient in the environment unless the recipient overrides it. The `__persistence_strategy__` and `__strategy__` keys are not supported, because defaults are always replaced in full.
    """

    categories: object
    """
    A map of category key to a boolean or an object containing `channel_types`,
    `channels`, and `conditions`.
    """

    channel_types: object
    """A map of channel type to a boolean or an object containing `conditions`.

    Valid channel types are `email`, `sms`, `push`, `chat`, `in_app_feed`, and
    `http`.
    """

    channels: object
    """A map of channel ID to a boolean or an object containing `conditions`."""

    commercial_subscribed: Union[bool, object]
    """
    Whether the recipient is subscribed to commercial messages, as a boolean or a
    settings object.
    """

    workflows: object
    """
    A map of workflow key to a boolean or an object containing `channel_types`,
    `channels`, and `conditions`.
    """

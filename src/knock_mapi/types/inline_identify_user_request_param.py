# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["InlineIdentifyUserRequestParam"]


class InlineIdentifyUserRequestParam(TypedDict, total=False):
    """A user recipient with optional identify properties.

    When email or name are provided, the user is created or updated as part of the workflow run. The collection is always `$users` and should not be sent.
    """

    id: Required[str]
    """The ID of the user."""

    email: Optional[str]
    """The email address to set on the user."""

    name: Optional[str]
    """The display name to set on the user."""

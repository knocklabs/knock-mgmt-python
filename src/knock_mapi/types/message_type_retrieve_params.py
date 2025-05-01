# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageTypeRetrieveParams"]


class MessageTypeRetrieveParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """

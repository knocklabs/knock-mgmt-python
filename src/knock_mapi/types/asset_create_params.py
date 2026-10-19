# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    filename: Required[str]
    """The display name for this asset."""

    key: Required[str]
    """The storage key from the upload request. The file must already be uploaded."""

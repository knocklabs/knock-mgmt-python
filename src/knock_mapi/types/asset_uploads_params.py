# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AssetUploadsParams"]


class AssetUploadsParams(TypedDict, total=False):
    content_length: Required[int]
    """The file size in bytes.

    Maximum is 5 MB. The upload URL is signed for this length.
    """

    mime_type: Required[str]
    """The MIME type of the file. One of image/jpeg, image/png, or image/gif."""

    filename: Optional[str]
    """The display name to echo back.

    The upload request does not store it. Send it again when creating the asset.
    """

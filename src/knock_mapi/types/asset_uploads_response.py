# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AssetUploadsResponse"]


class AssetUploadsResponse(BaseModel):
    """A time-limited permission to upload an asset file directly to storage."""

    content_length: int
    """The byte length the PUT must send as Content-Length."""

    expires_in: int
    """Seconds until the upload URL expires."""

    key: str
    """The storage key to send when creating the asset."""

    mime_type: str
    """The MIME type the PUT must send as Content-Type."""

    upload_url: str
    """The URL to PUT the file bytes to.

    The signature covers Content-Type and Content-Length, and the PUT must send
    both.
    """

    filename: Optional[str] = None
    """The filename from the request, when one was sent."""

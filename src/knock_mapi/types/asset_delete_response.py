# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssetDeleteResponse"]


class AssetDeleteResponse(BaseModel):
    """The response from archiving an asset."""

    result: str
    """The result of the archive operation."""

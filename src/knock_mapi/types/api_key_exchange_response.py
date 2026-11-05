# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["APIKeyExchangeResponse"]


class APIKeyExchangeResponse(BaseModel):
    """Returns an API key that can be used to make requests to the public API."""

    api_key: str
    """The API key exchanged from the service token, of the requested `type`."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["APIKeyExchangeResponse"]


class APIKeyExchangeResponse(BaseModel):
    api_key: str
    """The secret API key exchanged from the service token."""

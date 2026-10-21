# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookDeleteResponse"]


class WebhookDeleteResponse(BaseModel):
    """The response from archiving a webhook."""

    result: str
    """The result of the archive operation."""

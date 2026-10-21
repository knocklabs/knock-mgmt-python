# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    """Wraps the Webhook response under the `webhook` key."""

    webhook: Webhook
    """An outbound webhook that receives event notifications."""

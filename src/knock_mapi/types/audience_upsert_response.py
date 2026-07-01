# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .audience import Audience

__all__ = ["AudienceUpsertResponse"]


class AudienceUpsertResponse(BaseModel):
    """Wraps the Audience response under the `audience` key."""

    audience: Audience
    """An audience defines a set of users that can be targeted for notifications.

    Can be either a `StaticAudience` (members explicitly added/removed) or a
    `DynamicAudience` (members determined by segment conditions).
    """

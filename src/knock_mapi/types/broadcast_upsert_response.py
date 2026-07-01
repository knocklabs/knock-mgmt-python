# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["BroadcastUpsertResponse"]


class BroadcastUpsertResponse(BaseModel):
    """Wraps the Broadcast response under the `broadcast` key."""

    broadcast: "Broadcast"
    """A broadcast object."""


from .broadcast import Broadcast

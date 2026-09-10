# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BroadcastRunResponse"]


class BroadcastRunResponse(BaseModel):
    """A response to a broadcast run request."""

    broadcast_run_id: str
    """The ID of the broadcast run."""

    request_id: str
    """The ID of the run request."""

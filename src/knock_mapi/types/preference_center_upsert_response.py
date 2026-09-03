# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PreferenceCenterUpsertResponse"]


class PreferenceCenterUpsertResponse(BaseModel):
    """The preference center configuration for a single environment."""

    config: Optional[object] = None
    """The preference center configuration document."""

    enabled: Optional[bool] = None
    """Whether the preference center is enabled for recipients."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GuideActivationLocationRule"]


class GuideActivationLocationRule(BaseModel):
    directive: Literal["allow", "block"]
    """Whether to allow or block the guide at the specified pathname."""

    pathname: str
    """The URL pathname pattern to match against. Must be a valid URI path."""

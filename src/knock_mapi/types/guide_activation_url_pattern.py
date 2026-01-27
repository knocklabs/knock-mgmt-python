# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GuideActivationURLPattern"]


class GuideActivationURLPattern(BaseModel):
    """
    A rule that controls when a guide should be shown based on the user's location in the application. At least one of `pathname` or `search` must be provided.
    """

    directive: Literal["allow", "block"]
    """Whether to allow or block the guide at the specified location."""

    pathname: Optional[str] = None
    """The URL pathname pattern to match against. Must be a valid URI path."""

    search: Optional[str] = None
    """The URL query string pattern to match against (without the leading '?').

    Supports URLPattern API syntax.
    """

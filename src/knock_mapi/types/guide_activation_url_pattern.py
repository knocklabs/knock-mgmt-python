# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GuideActivationURLPattern"]


class GuideActivationURLPattern(BaseModel):
    """
    A rule that controls when a guide should be shown based on the user's location in the application.
    """

    directive: Literal["allow", "block"]
    """Whether to allow or block the guide at the specified pathname."""

    pathname: str
    """The URL pathname pattern to match against. Must be a valid URI path."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GuideActivationURLPatternParam"]


class GuideActivationURLPatternParam(TypedDict, total=False):
    """
    A rule that controls when a guide should be shown based on the user's location in the application.
    """

    directive: Required[Literal["allow", "block"]]
    """Whether to allow or block the guide at the specified pathname."""

    pathname: Required[str]
    """The URL pathname pattern to match against. Must be a valid URI path."""

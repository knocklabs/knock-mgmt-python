# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .partial_request_param import PartialRequestParam

__all__ = ["PartialPreviewParams", "Layout"]


class PartialPreviewParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    partial: Required[PartialRequestParam]
    """A partial object with attributes to update or create a partial."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    data: Dict[str, object]
    """The data to pass to the partial when rendering.

    Top-level keys are exposed as variables in the partial template.
    """

    layout: Optional[Layout]
    """Email layout configuration.

    Only applicable for `html` partials. When omitted, the rendered partial is
    returned unwrapped.
    """


class Layout(TypedDict, total=False):
    """Email layout configuration.

    Only applicable for `html` partials. When omitted, the rendered partial is returned unwrapped.
    """

    key: Optional[str]
    """The key of an existing email layout to use."""

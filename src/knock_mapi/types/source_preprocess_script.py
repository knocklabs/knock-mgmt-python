# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SourcePreprocessScript"]


class SourcePreprocessScript(BaseModel):
    """A script that runs before source events are mapped."""

    language: Literal["javascript"]
    """The programming language used by the preprocess script."""

    source: str
    """The source code for the preprocess script."""

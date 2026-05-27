# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SourcePreprocessScriptParam"]


class SourcePreprocessScriptParam(TypedDict, total=False):
    """A script that runs before source events are mapped."""

    language: Required[Literal["javascript"]]
    """The programming language used by the preprocess script."""

    source: Required[str]
    """The source code for the preprocess script."""

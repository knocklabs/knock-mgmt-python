# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranslationValidateParams", "Translation"]


class TranslationValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    translation: Required[Translation]
    """
    A translation object with a content attribute used to update or create a
    translation.
    """


class Translation(TypedDict, total=False):
    content: Required[str]
    """
    A JSON encoded string containing the key-value pairs of translation references
    and translation strings.
    """

    format: Required[Literal["json", "po"]]
    """
    Indicates whether content is a JSON encoded object string or a string in the PO
    format.
    """

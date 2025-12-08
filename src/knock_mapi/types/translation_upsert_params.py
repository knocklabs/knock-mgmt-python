# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranslationUpsertParams", "Translation"]


class TranslationUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    namespace: Required[str]
    """An optional namespace that identifies the translation."""

    translation: Required[Translation]
    """
    A translation object with a content attribute used to update or create a
    translation.
    """

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""

    format: Literal["json", "po"]
    """Optionally specify the returned content format.

    Supports 'json' and 'po'. Defaults to 'json'.
    """


class Translation(TypedDict, total=False):
    """
    A translation object with a content attribute used to update or create a translation.
    """

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

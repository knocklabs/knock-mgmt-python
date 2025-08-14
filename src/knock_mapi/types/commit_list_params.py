# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommitListParams"]


class CommitListParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    limit: int
    """The number of entries to fetch per-page."""

    promoted: bool
    """
    Whether to show commits in the given environment that have not been promoted to
    the subsequent environment (false) or commits which have been promoted (true).
    """

    resource_id: str
    """Filter commits by resource identifier.

    Must be used together with resource_type. For most resources, this will be the
    resource key. In the case of translations, this will be the locale code and
    namespace, separated by a `/`. For example, `en/courses` or `en`.
    """

    resource_type: Literal["email_layout", "guide", "message_type", "partial", "translation", "workflow"]
    """Filter commits by resource type. Must be used together with resource_id."""

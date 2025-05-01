# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookTemplateParam", "Header", "QueryParam"]


class Header(TypedDict, total=False):
    key: Required[str]
    """The key of the header."""

    value: Required[str]
    """The value of the header."""


class QueryParam(TypedDict, total=False):
    key: Required[str]
    """The key of the query param."""

    value: Required[str]
    """The value of the query param."""


class WebhookTemplateParam(TypedDict, total=False):
    method: Required[Literal["get", "post", "put", "delete", "patch"]]
    """The HTTP method of the webhook."""

    url: Required[str]
    """The URL of the webhook."""

    body: Optional[str]
    """The body of the request. Only used for POST or PUT requests."""

    headers: Iterable[Header]
    """A list of key-value pairs for the request headers.

    Each object should contain key and value fields with string values.
    """

    query_params: Iterable[QueryParam]
    """A list of key-value pairs for the request query params.

    Each object should contain key and value fields with string values.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RequestTemplateParam", "HeadersRequestTemplateHeadersArray", "QueryParamsRequestTemplateQueryParamsArray"]


class HeadersRequestTemplateHeadersArray(TypedDict, total=False):
    key: Required[str]
    """The key of the header."""

    value: Required[str]
    """The value of the header."""


class QueryParamsRequestTemplateQueryParamsArray(TypedDict, total=False):
    key: Required[str]
    """The key of the query param."""

    value: Required[str]
    """The value of the query param."""


class RequestTemplateParam(TypedDict, total=False):
    """A request template for a fetch function step."""

    method: Required[Literal["get", "post", "put", "delete", "patch"]]
    """The HTTP method of the request."""

    url: Required[str]
    """The URL of the request."""

    body: Optional[str]
    """The body of the request. Only used for POST or PUT requests."""

    headers: Union[str, Iterable[HeadersRequestTemplateHeadersArray]]
    """The headers of the request.

    Can be a template string or a list of key-value pairs.
    """

    query_params: Union[str, Iterable[QueryParamsRequestTemplateQueryParamsArray]]
    """The query params of the request.

    Can be a template string or a list of key-value pairs.
    """

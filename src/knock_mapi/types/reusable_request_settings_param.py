# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ReusableRequestSettingsParam",
    "HeadersRequestTemplateHeadersArray",
    "QueryParamsRequestTemplateQueryParamsArray",
]


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


class ReusableRequestSettingsParam(TypedDict, total=False):
    """The HTTP request a reusable request runs."""

    method: Required[Literal["get", "post", "put", "delete", "patch"]]
    """The HTTP method of the request."""

    body: Optional[str]
    """The body of the request. Only used for POST or PUT requests."""

    data_input_schema: Optional[Dict[str, object]]
    """A JSON schema for inputs the request accepts."""

    data_input_values_str: Optional[str]
    """A JSON string of input values for the request."""

    headers: Union[str, Iterable[HeadersRequestTemplateHeadersArray]]
    """The headers of the request.

    Can be a template string or a list of key-value pairs.
    """

    query_params: Union[str, Iterable[QueryParamsRequestTemplateQueryParamsArray]]
    """The query params of the request.

    Can be a template string or a list of key-value pairs.
    """

    response_path: Optional[str]
    """A JSON path into the response that is merged into the workflow data."""

    signing_key: Optional[str]
    """The signing key used to sign the request."""

    url: str
    """The URL of the request."""

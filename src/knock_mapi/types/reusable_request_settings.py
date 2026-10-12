# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ReusableRequestSettings",
    "HeadersRequestTemplateHeadersArray",
    "QueryParamsRequestTemplateQueryParamsArray",
]


class HeadersRequestTemplateHeadersArray(BaseModel):
    key: str
    """The key of the header."""

    value: str
    """The value of the header."""


class QueryParamsRequestTemplateQueryParamsArray(BaseModel):
    key: str
    """The key of the query param."""

    value: str
    """The value of the query param."""


class ReusableRequestSettings(BaseModel):
    """The HTTP request a reusable request runs."""

    method: Literal["get", "post", "put", "delete", "patch"]
    """The HTTP method of the request."""

    body: Optional[str] = None
    """The body of the request. Only used for POST or PUT requests."""

    data_input_schema: Optional[Dict[str, object]] = None
    """A JSON schema for inputs the request accepts."""

    data_input_values_str: Optional[str] = None
    """A JSON string of input values for the request."""

    headers: Union[str, List[HeadersRequestTemplateHeadersArray], None] = None
    """The headers of the request.

    Can be a template string or a list of key-value pairs.
    """

    query_params: Union[str, List[QueryParamsRequestTemplateQueryParamsArray], None] = None
    """The query params of the request.

    Can be a template string or a list of key-value pairs.
    """

    response_path: Optional[str] = None
    """A JSON path into the response that is merged into the workflow data."""

    signing_key: Optional[str] = None
    """The signing key used to sign the request."""

    url: Optional[str] = None
    """The URL of the request."""

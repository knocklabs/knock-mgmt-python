# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequestTemplate", "HeadersRequestTemplateHeadersArray", "QueryParamsRequestTemplateQueryParamsArray"]


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


class RequestTemplate(BaseModel):
    """A request template for a fetch function step."""

    method: Literal["get", "post", "put", "delete", "patch"]
    """The HTTP method of the request."""

    url: str
    """The URL of the request."""

    body: Optional[str] = None
    """The body of the request. Only used for POST or PUT requests."""

    headers: Union[str, List[HeadersRequestTemplateHeadersArray], None] = None
    """The headers of the request.

    Can be a template string or a list of key-value pairs.
    """

    query_params: Union[str, List[QueryParamsRequestTemplateQueryParamsArray], None] = None
    """The query params of the request.

    Can be a template string or a list of key-value pairs.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequestTemplate", "HeadersUnionMember1", "QueryParamsUnionMember1"]


class HeadersUnionMember1(BaseModel):
    key: str
    """The key of the header."""

    value: str
    """The value of the header."""


class QueryParamsUnionMember1(BaseModel):
    key: str
    """The key of the query param."""

    value: str
    """The value of the query param."""


class RequestTemplate(BaseModel):
    method: Literal["get", "post", "put", "delete", "patch"]
    """The HTTP method of the request."""

    url: str
    """The URL of the request."""

    body: Optional[str] = None
    """The body of the request. Only used for POST or PUT requests."""

    headers: Union[str, List[HeadersUnionMember1], None] = None
    """The headers of the request.

    Can be a template string or a list of key-value pairs.
    """

    query_params: Union[str, List[QueryParamsUnionMember1], None] = None
    """The query params of the request.

    Can be a template string or a list of key-value pairs.
    """

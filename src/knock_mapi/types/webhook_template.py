# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookTemplate", "Header", "QueryParam"]


class Header(BaseModel):
    key: str
    """The key of the header."""

    value: str
    """The value of the header."""


class QueryParam(BaseModel):
    key: str
    """The key of the query param."""

    value: str
    """The value of the query param."""


class WebhookTemplate(BaseModel):
    """A webhook template.

    By default, a webhook step will use the request settings you configured in your webhook channel. You can override this as you see fit on a per-step basis.
    """

    method: Literal["get", "post", "put", "delete", "patch"]
    """The HTTP method of the webhook."""

    url: str
    """The URL of the webhook."""

    body: Optional[str] = None
    """The body of the request. Only used for POST or PUT requests."""

    headers: Optional[List[Header]] = None
    """A list of key-value pairs for the request headers.

    Each object should contain key and value fields with string values.
    """

    query_params: Optional[List[QueryParam]] = None
    """A list of key-value pairs for the request query params.

    Each object should contain key and value fields with string values.
    """

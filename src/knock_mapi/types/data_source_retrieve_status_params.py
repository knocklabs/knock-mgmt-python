# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DataSourceRetrieveStatusParams"]


class DataSourceRetrieveStatusParams(TypedDict, total=False):
    environment: str
    """The environment slug."""

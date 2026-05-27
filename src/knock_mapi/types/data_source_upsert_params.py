# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .source_request_param import SourceRequestParam

__all__ = ["DataSourceUpsertParams"]


class DataSourceUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    source: Required[SourceRequestParam]
    """
    A source request for setting a source and its environment-specific
    configuration.
    """

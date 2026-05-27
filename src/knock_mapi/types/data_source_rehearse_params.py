# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DataSourceRehearseParams"]


class DataSourceRehearseParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    payload: Required[Dict[str, object]]
    """
    An arbitrary payload to send through the source's parse, preprocess, and mapping
    pipeline.
    """

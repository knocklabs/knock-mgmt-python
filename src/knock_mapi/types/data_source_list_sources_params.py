# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DataSourceListSourcesParams"]


class DataSourceListSourcesParams(TypedDict, total=False):
    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    environment: str
    """The environment slug."""

    include: List[Literal["environment_settings"]]
    """Associated resources to include in each source. Accepts `environment_settings`."""

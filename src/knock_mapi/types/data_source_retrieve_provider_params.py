# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DataSourceRetrieveProviderParams"]


class DataSourceRetrieveProviderParams(TypedDict, total=False):
    include: List[
        Literal["branding", "default_action_mappings", "example_payloads", "preprocessing_script", "static_fields"]
    ]
    """Associated resources to include in the response.

    Accepts `branding`, `default_action_mappings`, `example_payloads`,
    `preprocessing_script`, `static_fields`.
    """

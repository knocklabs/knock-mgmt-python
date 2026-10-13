# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VariableUpsertParams"]


class VariableUpsertParams(TypedDict, total=False):
    type: Required[Literal["public", "secret"]]
    """The type of the variable.

    Required, and it cannot be changed after the variable is created.
    """

    description: Optional[str]
    """The description of the variable.

    When omitted or null on an update, the existing description is kept. An empty
    string clears it.
    """

    environment_values: Dict[str, Optional[str]]
    """A map of root environment slugs to override values.

    An environment that is omitted or null is left unchanged. An empty string clears
    the override, so the default value applies.
    """

    value: Optional[str]
    """The default value of the variable.

    Required when creating a variable. When omitted or null on an update, the
    existing value is kept. An empty string clears the default value.
    """

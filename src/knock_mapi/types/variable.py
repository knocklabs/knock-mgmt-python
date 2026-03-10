# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Variable"]


class Variable(BaseModel):
    """An environment variable object."""

    inserted_at: datetime
    """The timestamp of when the variable was created."""

    key: str
    """The key of the variable."""

    type: Literal["public", "secret"]
    """The type of the variable."""

    updated_at: datetime
    """The timestamp of when the variable was last updated."""

    description: Optional[str] = None
    """The description of the variable."""

    environment_values: Optional[Dict[str, Optional[str]]] = None
    """A map of environment slugs to their override values.

    Only present for project-scoped responses.
    """

    value: Optional[str] = None
    """The default value of the variable. For secret variables, this is obfuscated."""

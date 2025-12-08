# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["GuideStep"]


class GuideStep(BaseModel):
    """A step in a guide that corresponds to a piece of UI and its content."""

    ref: str
    """The unique reference string for the step.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    schema_key: str
    """The key of the template schema to use for this step."""

    schema_semver: str
    """The semantic version of the template schema to use."""

    schema_variant_key: str
    """The key of the template schema variant to use."""

    name: Optional[str] = None
    """A name for the step."""

    values: Optional[Dict[str, object]] = None
    """A map of values that make up the step's content.

    Each value must conform to its respective template schema field settings.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["GuideStepParam"]


class GuideStepParam(TypedDict, total=False):
    """A step in a guide that corresponds to a piece of UI and its content."""

    ref: Required[str]
    """The unique reference string for the step.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    schema_key: Required[str]
    """The key of the template schema to use for this step."""

    schema_semver: Required[str]
    """The semantic version of the template schema to use."""

    schema_variant_key: Required[str]
    """The key of the template schema variant to use."""

    name: str
    """A name for the step."""

    values: Dict[str, object]
    """A map of values that make up the step's content.

    Each value must conform to its respective template schema field settings.
    """

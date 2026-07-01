# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .email_layout import EmailLayout

__all__ = ["EmailLayoutUpsertResponse"]


class EmailLayoutUpsertResponse(BaseModel):
    """Wraps the EmailLayout response under the `email_layout` key."""

    email_layout: EmailLayout
    """A versioned email layout used within an environment."""

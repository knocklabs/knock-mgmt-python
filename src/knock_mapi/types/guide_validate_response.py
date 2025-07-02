# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .guide import Guide
from .._models import BaseModel

__all__ = ["GuideValidateResponse"]


class GuideValidateResponse(BaseModel):
    guide: Guide
    """
    A guide defines an in-app guide that can be displayed to users based on priority
    and other conditions.
    """

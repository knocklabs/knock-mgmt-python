# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthVerifyResponse"]


class AuthVerifyResponse(BaseModel):
    account_name: str

    account_slug: str

    type: Literal["service_token", "oauth_context"]

    service_token_name: Optional[str] = None

    user_id: Optional[str] = None

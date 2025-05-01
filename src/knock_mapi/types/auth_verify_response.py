# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AuthVerifyResponse"]


class AuthVerifyResponse(BaseModel):
    account_name: str

    account_slug: str

    service_token_name: str

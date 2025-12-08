# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthVerifyResponse", "AccountFeatures"]


class AccountFeatures(BaseModel):
    """Account plan features and limits."""

    batch_items_render_limit_allowed: Optional[bool] = None
    """Whether batch rendering limits can be configured."""

    custom_branding_allowed: Optional[bool] = None
    """Whether custom branding can be applied to notifications."""

    data_retention_days: Optional[int] = None
    """Number of days data is retained, null for unlimited retention."""

    data_warehouse_extension_allowed: Optional[bool] = None
    """Whether data warehouse integration extensions are available."""

    datadog_extension_allowed: Optional[bool] = None
    """Whether Datadog integration extension is available."""

    dsync_allowed: Optional[bool] = None
    """Whether directory sync functionality is available."""

    guides_monthly_notified_recipients_limit: Optional[int] = None
    """Monthly limit for guide notification recipients, null for unlimited."""

    guides_per_tenant_scope_allowed: Optional[bool] = None
    """Whether per-tenant scope for guide messages is allowed."""

    heap_extension_allowed: Optional[bool] = None
    """Whether Heap integration extension is available."""

    knock_branding_required: Optional[bool] = None
    """Whether Knock branding is required to be displayed."""

    litmus_email_preview_allowed: Optional[bool] = None
    """Whether Litmus email preview integration is available."""

    message_sent_limit: Optional[int] = None
    """Monthly limit for messages sent, null for unlimited."""

    new_relic_extension_allowed: Optional[bool] = None
    """Whether New Relic integration extension is available."""

    segment_extension_allowed: Optional[bool] = None
    """Whether Segment integration extension is available."""

    self_serve_allowed: Optional[bool] = None
    """Whether self-service account management features are available."""

    sso_allowed: Optional[bool] = None
    """Whether single sign-on (SSO) is enabled for the account."""

    tenant_preferences_allowed: Optional[bool] = None
    """Whether tenant-level preferences are supported."""

    translations_allowed: Optional[bool] = None
    """Whether multi-language translations are supported."""


class AuthVerifyResponse(BaseModel):
    """Information about the current calling scope."""

    account_features: AccountFeatures
    """Account plan features and limits."""

    account_name: str
    """The display name of the account."""

    account_slug: str
    """The unique slug identifier for the account."""

    type: Literal["service_token", "oauth_context"]
    """
    The type of authentication context - either a service token or OAuth user
    context.
    """

    service_token_name: Optional[str] = None
    """
    The name of the service token if authenticated via service token, null for OAuth
    contexts.
    """

    user_id: Optional[str] = None
    """
    The ID of the authenticated user if in OAuth context, null for service token
    contexts.
    """

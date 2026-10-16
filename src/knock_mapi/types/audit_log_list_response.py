# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuditLogListResponse", "Actor", "Location", "Resource"]


class Actor(BaseModel):
    """The Knock user who performed the action."""

    id: str
    """The unique identifier for the user."""

    email: str
    """The email address of the user."""

    name: Optional[str] = None
    """The name of the user."""


class Location(BaseModel):
    """The location derived from the request IP address."""

    city: Optional[str] = None
    """The city."""

    country_code: Optional[str] = None
    """The country code."""

    region_code: Optional[str] = None
    """The region code."""


class Resource(BaseModel):
    """The resource the action changed.

    `type` and `identifier` follow the commit resource for promotable resources, including `reusable_request`. `identifier` is null when the resource has no public handle or the row no longer exists.
    """

    id: str
    """The stored id of the resource. External user and object ids are not UUIDs."""

    type: Literal[
        "account",
        "account_user",
        "api_key",
        "asset",
        "audience",
        "broadcast",
        "channel",
        "channel_group",
        "email_layout",
        "environment",
        "environment_defaults",
        "event_action_mapping",
        "external_audience",
        "goal",
        "guide",
        "guide_group",
        "invite",
        "member",
        "message_type",
        "object",
        "partial",
        "permission_group",
        "preference_category",
        "preference_center",
        "preference_center_domain",
        "reusable_request",
        "service_token",
        "signing_key",
        "source",
        "subscription",
        "tag",
        "translation",
        "user",
        "variable",
        "view",
        "webhook",
        "workflow",
        "unknown",
    ]
    """The type of the resource."""

    identifier: Optional[str] = None
    """
    The public handle for the resource, such as a key, slug, email, or
    `locale/namespace` for a translation.
    """


class AuditLogListResponse(BaseModel):
    """An account audit log entry.

    Commit rows are returned by the commits endpoint. The entry does not include the stored change diff.
    """

    id: str
    """The unique identifier for the audit log entry."""

    action: str
    """The action that was performed, such as `workflow.updated` or `seat.removed`."""

    actor: Optional[Actor] = None
    """The Knock user who performed the action."""

    agent_session_id: Optional[str] = None
    """The agent session that performed the action, when the source is an agent."""

    environment: Optional[str] = None
    """The slug of the environment or branch where the action happened.

    Null for account-level actions.
    """

    inserted_at: datetime
    """The timestamp of when the action happened."""

    ip_address: Optional[str] = None
    """The IP address of the request that performed the action."""

    location: Optional[Location] = None
    """The location derived from the request IP address."""

    project_id: Optional[str] = None
    """The project the action belongs to. Null for account-level actions."""

    request_id: Optional[str] = None
    """The id of the request that performed the action."""

    request_source: Optional[Literal["dashboard", "mapi", "agent"]] = None
    """Where the action originated."""

    resource: Resource
    """The resource the action changed.

    `type` and `identifier` follow the commit resource for promotable resources,
    including `reusable_request`. `identifier` is null when the resource has no
    public handle or the row no longer exists.
    """

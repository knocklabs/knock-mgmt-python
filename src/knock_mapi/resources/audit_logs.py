# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import audit_log_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncEntriesCursor, AsyncEntriesCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.audit_log_list_response import AuditLogListResponse

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action: Union[str, SequenceNotStr[str]] | Omit = omit,
        actor_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        environment: str | Omit = omit,
        limit: int | Omit = omit,
        resource_type: Union[
            Literal[
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
            ],
            List[
                Literal[
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
                ]
            ],
        ]
        | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[AuditLogListResponse]:
        """
        Returns a paginated list of audit log entries for the current account, across
        every environment and branch, including account-level entries that have no
        environment. Entries are ordered from most recent first.

        The list includes user-visible changes and environment merges. Commits are
        returned by the commits endpoint. Entries outside the account's data retention
        window are omitted.

        Args:
          action: Filter by action. Accepts one action or an array of actions, matched exactly.

          actor_id: Filter by the id of the user who performed the action. Accepts one id or an
              array of ids.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          environment: The environment slug. When omitted, the list is account-wide and does not use
              the account's default environment. When set, limits entries to that environment
              or branch and omits account-level entries.

          limit: The number of entries to fetch per-page.

          resource_type: Filter by resource type. Accepts one type or an array of types. `channel`
              includes channel environment settings, and `source` includes source environment
              settings.

          since: Only return entries inserted at or after this RFC 3339 timestamp.

          until: Only return entries inserted at or before this RFC 3339 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/audit_logs",
            page=SyncEntriesCursor[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "actor_id": actor_id,
                        "after": after,
                        "before": before,
                        "environment": environment,
                        "limit": limit,
                        "resource_type": resource_type,
                        "since": since,
                        "until": until,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action: Union[str, SequenceNotStr[str]] | Omit = omit,
        actor_id: Union[str, SequenceNotStr[str]] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        environment: str | Omit = omit,
        limit: int | Omit = omit,
        resource_type: Union[
            Literal[
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
            ],
            List[
                Literal[
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
                ]
            ],
        ]
        | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogListResponse, AsyncEntriesCursor[AuditLogListResponse]]:
        """
        Returns a paginated list of audit log entries for the current account, across
        every environment and branch, including account-level entries that have no
        environment. Entries are ordered from most recent first.

        The list includes user-visible changes and environment merges. Commits are
        returned by the commits endpoint. Entries outside the account's data retention
        window are omitted.

        Args:
          action: Filter by action. Accepts one action or an array of actions, matched exactly.

          actor_id: Filter by the id of the user who performed the action. Accepts one id or an
              array of ids.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          environment: The environment slug. When omitted, the list is account-wide and does not use
              the account's default environment. When set, limits entries to that environment
              or branch and omits account-level entries.

          limit: The number of entries to fetch per-page.

          resource_type: Filter by resource type. Accepts one type or an array of types. `channel`
              includes channel environment settings, and `source` includes source environment
              settings.

          since: Only return entries inserted at or after this RFC 3339 timestamp.

          until: Only return entries inserted at or before this RFC 3339 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/audit_logs",
            page=AsyncEntriesCursor[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "actor_id": actor_id,
                        "after": after,
                        "before": before,
                        "environment": environment,
                        "limit": limit,
                        "resource_type": resource_type,
                        "since": since,
                        "until": until,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )

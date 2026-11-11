# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    warehouse_sync_list_params,
    warehouse_sync_update_params,
    warehouse_sync_retrieve_params,
    warehouse_sync_update_run_params,
    warehouse_sync_retrieve_runs_params,
    warehouse_sync_update_settings_params,
    warehouse_sync_update_validate_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.warehouse_sync import WarehouseSync
from ..types.warehouse_sync_request_param import WarehouseSyncRequestParam
from ..types.warehouse_sync_update_response import WarehouseSyncUpdateResponse
from ..types.warehouse_sync_update_run_response import WarehouseSyncUpdateRunResponse
from ..types.warehouse_sync_retrieve_runs_response import WarehouseSyncRetrieveRunsResponse
from ..types.warehouse_sync_update_settings_response import WarehouseSyncUpdateSettingsResponse
from ..types.warehouse_sync_update_validate_response import WarehouseSyncUpdateValidateResponse

__all__ = ["WarehouseSyncsResource", "AsyncWarehouseSyncsResource"]


class WarehouseSyncsResource(SyncAPIResource):
    """
    Warehouse syncs read rows from a warehouse on a schedule and write them to Knock.
    """

    @cached_property
    def with_raw_response(self) -> WarehouseSyncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return WarehouseSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WarehouseSyncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return WarehouseSyncsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSync:
        """
        Retrieve a warehouse sync by its key in a given environment.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return self._get(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}", warehouse_sync_key=warehouse_sync_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    warehouse_sync_retrieve_params.WarehouseSyncRetrieveParams,
                ),
            ),
            cast_to=WarehouseSync,
        )

    def update(
        self,
        warehouse_sync_key: str,
        *,
        warehouse_sync: WarehouseSyncRequestParam,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateResponse:
        """Creates a warehouse sync, or saves a new draft of it if it exists.

        Fields left
        out keep their current values. Pass `commit=true` to publish the draft. A draft
        that fails to publish stays saved.

        Args:
          warehouse_sync: A warehouse sync payload for upsert or validate. Fields left out keep their
              current values. `warehouse_key`, `target_type`, and `target` are required to
              create a sync and can't change after. Change `enabled` and `frequency_minutes`
              with the settings endpoint.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}", warehouse_sync_key=warehouse_sync_key),
            body=maybe_transform(
                {"warehouse_sync": warehouse_sync}, warehouse_sync_update_params.WarehouseSyncUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "commit": commit,
                        "commit_message": commit_message,
                        "environment": environment,
                    },
                    warehouse_sync_update_params.WarehouseSyncUpdateParams,
                ),
            ),
            cast_to=WarehouseSyncUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[WarehouseSync]:
        """
        Returns a paginated list of warehouse syncs for the given environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/warehouse_syncs",
            page=SyncEntriesCursor[WarehouseSync],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    warehouse_sync_list_params.WarehouseSyncListParams,
                ),
            ),
            model=WarehouseSync,
        )

    def retrieve_runs(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncRetrieveRunsResponse:
        """
        Returns the most recent runs of a warehouse sync, newest first.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return self._get(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/runs", warehouse_sync_key=warehouse_sync_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, warehouse_sync_retrieve_runs_params.WarehouseSyncRetrieveRunsParams
                ),
            ),
            cast_to=WarehouseSyncRetrieveRunsResponse,
        )

    def update_run(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateRunResponse:
        """
        Starts a run of the published warehouse sync now, instead of waiting for its
        schedule. Refused while a run is in progress.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/run", warehouse_sync_key=warehouse_sync_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, warehouse_sync_update_run_params.WarehouseSyncUpdateRunParams
                ),
            ),
            cast_to=WarehouseSyncUpdateRunResponse,
        )

    def update_settings(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        enabled: bool | Omit = omit,
        frequency_minutes: Literal[10, 15, 60, 360, 720, 1440] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateSettingsResponse:
        """Pauses or resumes a warehouse sync, or changes how often it runs.

        Settings take
        effect right away and don't need a publish.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          enabled: Whether the sync runs on its schedule.

          frequency_minutes: How often the sync runs, in minutes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/settings", warehouse_sync_key=warehouse_sync_key),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "frequency_minutes": frequency_minutes,
                },
                warehouse_sync_update_settings_params.WarehouseSyncUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment},
                    warehouse_sync_update_settings_params.WarehouseSyncUpdateSettingsParams,
                ),
            ),
            cast_to=WarehouseSyncUpdateSettingsResponse,
        )

    def update_validate(
        self,
        warehouse_sync_key: str,
        *,
        warehouse_sync: WarehouseSyncRequestParam,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateValidateResponse:
        """
        Checks a warehouse sync payload the way an upsert would, without saving it.
        Returns the payload as sent.

        Args:
          warehouse_sync: A warehouse sync payload for upsert or validate. Fields left out keep their
              current values. `warehouse_key`, `target_type`, and `target` are required to
              create a sync and can't change after. Change `enabled` and `frequency_minutes`
              with the settings endpoint.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/validate", warehouse_sync_key=warehouse_sync_key),
            body=maybe_transform(
                {"warehouse_sync": warehouse_sync},
                warehouse_sync_update_validate_params.WarehouseSyncUpdateValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment},
                    warehouse_sync_update_validate_params.WarehouseSyncUpdateValidateParams,
                ),
            ),
            cast_to=WarehouseSyncUpdateValidateResponse,
        )


class AsyncWarehouseSyncsResource(AsyncAPIResource):
    """
    Warehouse syncs read rows from a warehouse on a schedule and write them to Knock.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWarehouseSyncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWarehouseSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWarehouseSyncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncWarehouseSyncsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSync:
        """
        Retrieve a warehouse sync by its key in a given environment.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return await self._get(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}", warehouse_sync_key=warehouse_sync_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    warehouse_sync_retrieve_params.WarehouseSyncRetrieveParams,
                ),
            ),
            cast_to=WarehouseSync,
        )

    async def update(
        self,
        warehouse_sync_key: str,
        *,
        warehouse_sync: WarehouseSyncRequestParam,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateResponse:
        """Creates a warehouse sync, or saves a new draft of it if it exists.

        Fields left
        out keep their current values. Pass `commit=true` to publish the draft. A draft
        that fails to publish stays saved.

        Args:
          warehouse_sync: A warehouse sync payload for upsert or validate. Fields left out keep their
              current values. `warehouse_key`, `target_type`, and `target` are required to
              create a sync and can't change after. Change `enabled` and `frequency_minutes`
              with the settings endpoint.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return await self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}", warehouse_sync_key=warehouse_sync_key),
            body=await async_maybe_transform(
                {"warehouse_sync": warehouse_sync}, warehouse_sync_update_params.WarehouseSyncUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "commit": commit,
                        "commit_message": commit_message,
                        "environment": environment,
                    },
                    warehouse_sync_update_params.WarehouseSyncUpdateParams,
                ),
            ),
            cast_to=WarehouseSyncUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WarehouseSync, AsyncEntriesCursor[WarehouseSync]]:
        """
        Returns a paginated list of warehouse syncs for the given environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/warehouse_syncs",
            page=AsyncEntriesCursor[WarehouseSync],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    warehouse_sync_list_params.WarehouseSyncListParams,
                ),
            ),
            model=WarehouseSync,
        )

    async def retrieve_runs(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncRetrieveRunsResponse:
        """
        Returns the most recent runs of a warehouse sync, newest first.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return await self._get(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/runs", warehouse_sync_key=warehouse_sync_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, warehouse_sync_retrieve_runs_params.WarehouseSyncRetrieveRunsParams
                ),
            ),
            cast_to=WarehouseSyncRetrieveRunsResponse,
        )

    async def update_run(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateRunResponse:
        """
        Starts a run of the published warehouse sync now, instead of waiting for its
        schedule. Refused while a run is in progress.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return await self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/run", warehouse_sync_key=warehouse_sync_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, warehouse_sync_update_run_params.WarehouseSyncUpdateRunParams
                ),
            ),
            cast_to=WarehouseSyncUpdateRunResponse,
        )

    async def update_settings(
        self,
        warehouse_sync_key: str,
        *,
        environment: str | Omit = omit,
        enabled: bool | Omit = omit,
        frequency_minutes: Literal[10, 15, 60, 360, 720, 1440] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateSettingsResponse:
        """Pauses or resumes a warehouse sync, or changes how often it runs.

        Settings take
        effect right away and don't need a publish.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          enabled: Whether the sync runs on its schedule.

          frequency_minutes: How often the sync runs, in minutes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return await self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/settings", warehouse_sync_key=warehouse_sync_key),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "frequency_minutes": frequency_minutes,
                },
                warehouse_sync_update_settings_params.WarehouseSyncUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment},
                    warehouse_sync_update_settings_params.WarehouseSyncUpdateSettingsParams,
                ),
            ),
            cast_to=WarehouseSyncUpdateSettingsResponse,
        )

    async def update_validate(
        self,
        warehouse_sync_key: str,
        *,
        warehouse_sync: WarehouseSyncRequestParam,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WarehouseSyncUpdateValidateResponse:
        """
        Checks a warehouse sync payload the way an upsert would, without saving it.
        Returns the payload as sent.

        Args:
          warehouse_sync: A warehouse sync payload for upsert or validate. Fields left out keep their
              current values. `warehouse_key`, `target_type`, and `target` are required to
              create a sync and can't change after. Change `enabled` and `frequency_minutes`
              with the settings endpoint.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_sync_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_sync_key` but received {warehouse_sync_key!r}")
        return await self._put(
            path_template("/v1/warehouse_syncs/{warehouse_sync_key}/validate", warehouse_sync_key=warehouse_sync_key),
            body=await async_maybe_transform(
                {"warehouse_sync": warehouse_sync},
                warehouse_sync_update_validate_params.WarehouseSyncUpdateValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment},
                    warehouse_sync_update_validate_params.WarehouseSyncUpdateValidateParams,
                ),
            ),
            cast_to=WarehouseSyncUpdateValidateResponse,
        )


class WarehouseSyncsResourceWithRawResponse:
    def __init__(self, warehouse_syncs: WarehouseSyncsResource) -> None:
        self._warehouse_syncs = warehouse_syncs

        self.retrieve = to_raw_response_wrapper(
            warehouse_syncs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            warehouse_syncs.update,
        )
        self.list = to_raw_response_wrapper(
            warehouse_syncs.list,
        )
        self.retrieve_runs = to_raw_response_wrapper(
            warehouse_syncs.retrieve_runs,
        )
        self.update_run = to_raw_response_wrapper(
            warehouse_syncs.update_run,
        )
        self.update_settings = to_raw_response_wrapper(
            warehouse_syncs.update_settings,
        )
        self.update_validate = to_raw_response_wrapper(
            warehouse_syncs.update_validate,
        )


class AsyncWarehouseSyncsResourceWithRawResponse:
    def __init__(self, warehouse_syncs: AsyncWarehouseSyncsResource) -> None:
        self._warehouse_syncs = warehouse_syncs

        self.retrieve = async_to_raw_response_wrapper(
            warehouse_syncs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            warehouse_syncs.update,
        )
        self.list = async_to_raw_response_wrapper(
            warehouse_syncs.list,
        )
        self.retrieve_runs = async_to_raw_response_wrapper(
            warehouse_syncs.retrieve_runs,
        )
        self.update_run = async_to_raw_response_wrapper(
            warehouse_syncs.update_run,
        )
        self.update_settings = async_to_raw_response_wrapper(
            warehouse_syncs.update_settings,
        )
        self.update_validate = async_to_raw_response_wrapper(
            warehouse_syncs.update_validate,
        )


class WarehouseSyncsResourceWithStreamingResponse:
    def __init__(self, warehouse_syncs: WarehouseSyncsResource) -> None:
        self._warehouse_syncs = warehouse_syncs

        self.retrieve = to_streamed_response_wrapper(
            warehouse_syncs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            warehouse_syncs.update,
        )
        self.list = to_streamed_response_wrapper(
            warehouse_syncs.list,
        )
        self.retrieve_runs = to_streamed_response_wrapper(
            warehouse_syncs.retrieve_runs,
        )
        self.update_run = to_streamed_response_wrapper(
            warehouse_syncs.update_run,
        )
        self.update_settings = to_streamed_response_wrapper(
            warehouse_syncs.update_settings,
        )
        self.update_validate = to_streamed_response_wrapper(
            warehouse_syncs.update_validate,
        )


class AsyncWarehouseSyncsResourceWithStreamingResponse:
    def __init__(self, warehouse_syncs: AsyncWarehouseSyncsResource) -> None:
        self._warehouse_syncs = warehouse_syncs

        self.retrieve = async_to_streamed_response_wrapper(
            warehouse_syncs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            warehouse_syncs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            warehouse_syncs.list,
        )
        self.retrieve_runs = async_to_streamed_response_wrapper(
            warehouse_syncs.retrieve_runs,
        )
        self.update_run = async_to_streamed_response_wrapper(
            warehouse_syncs.update_run,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            warehouse_syncs.update_settings,
        )
        self.update_validate = async_to_streamed_response_wrapper(
            warehouse_syncs.update_validate,
        )

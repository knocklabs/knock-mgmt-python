# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    data_source_upsert_params,
    data_source_rehearse_params,
    data_source_retrieve_params,
    data_source_list_logs_params,
    data_source_list_events_params,
    data_source_list_sources_params,
    data_source_retrieve_status_params,
    data_source_retrieve_provider_params,
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
from ..types.source import Source
from ..types.source_log import SourceLog
from ..types.sources_response import SourcesResponse
from ..types.source_request_param import SourceRequestParam
from ..types.source_events_response import SourceEventsResponse
from ..types.source_status_response import SourceStatusResponse
from ..types.source_provider_response import SourceProviderResponse
from ..types.source_rehearse_response import SourceRehearseResponse
from ..types.source_providers_response import SourceProvidersResponse
from ..types.data_source_upsert_response import DataSourceUpsertResponse

__all__ = ["DataSourcesResource", "AsyncDataSourcesResource"]


class DataSourcesResource(SyncAPIResource):
    """Sources receive external events that can trigger Knock actions."""

    @cached_property
    def with_raw_response(self) -> DataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return DataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return DataSourcesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """
        Returns a source with environment-specific settings, preprocess scripts, and
        event mappings.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/v1/sources/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                    },
                    data_source_retrieve_params.DataSourceRetrieveParams,
                ),
            ),
            cast_to=Source,
        )

    def list_events(
        self,
        key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceEventsResponse:
        """
        Returns known unique events received by a source in the requested environment.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/v1/sources/{key}/events", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, data_source_list_events_params.DataSourceListEventsParams
                ),
            ),
            cast_to=SourceEventsResponse,
        )

    def list_logs(
        self,
        key: str,
        *,
        environment: str,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        date: str | Omit = omit,
        ending_at: Union[str, datetime] | Omit = omit,
        event: str | Omit = omit,
        include: List[Literal["actions"]] | Omit = omit,
        limit: int | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[SourceLog]:
        """Returns event logs received by a source in the requested environment.

        Supports
        filtering by date/time, event, and log ID.

        Args:
          environment: The environment slug.

          id: The log ID to filter by.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          date: Returns event logs that were produced on this date.

          ending_at: Only return source logs at or before this timestamp.

          event: The event name to filter by.

          include: Associated resources to include in the response. Accepts `actions` to include
              the actions executed after receiving each source event.

          limit: The number of entries to fetch per-page.

          starting_at: Only return source logs at or after this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get_api_list(
            path_template("/v1/sources/{key}/logs", key=key),
            page=SyncEntriesCursor[SourceLog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "id": id,
                        "after": after,
                        "before": before,
                        "date": date,
                        "ending_at": ending_at,
                        "event": event,
                        "include": include,
                        "limit": limit,
                        "starting_at": starting_at,
                    },
                    data_source_list_logs_params.DataSourceListLogsParams,
                ),
            ),
            model=SourceLog,
        )

    def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceProvidersResponse:
        """Returns the source provider templates available for creating sources."""
        return self._get(
            "/v1/source_providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceProvidersResponse,
        )

    def list_sources(
        self,
        *,
        annotate: bool | Omit = omit,
        environment: str | Omit = omit,
        include: List[Literal["environment_settings"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourcesResponse:
        """
        Returns connected sources for the project.

        Args:
          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          environment: The environment slug.

          include: Associated resources to include in each source. Accepts `environment_settings`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annotate": annotate,
                        "environment": environment,
                        "include": include,
                    },
                    data_source_list_sources_params.DataSourceListSourcesParams,
                ),
            ),
            cast_to=SourcesResponse,
        )

    def rehearse(
        self,
        key: str,
        *,
        environment: str,
        payload: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRehearseResponse:
        """
        Sends an arbitrary payload through the source's parse, preprocess, and mapping
        pipeline in the requested environment. This endpoint cannot be run in production
        environments.

        Args:
          environment: The environment slug.

          payload: An arbitrary payload to send through the source's parse, preprocess, and mapping
              pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._post(
            path_template("/v1/sources/{key}/rehearse", key=key),
            body=maybe_transform({"payload": payload}, data_source_rehearse_params.DataSourceRehearseParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, data_source_rehearse_params.DataSourceRehearseParams
                ),
            ),
            cast_to=SourceRehearseResponse,
        )

    def retrieve_provider(
        self,
        key: str,
        *,
        include: List[
            Literal["branding", "default_action_mappings", "example_payloads", "preprocessing_script", "static_fields"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceProviderResponse:
        """
        Returns a source provider template available for creating sources.

        Args:
          include: Associated resources to include in the response. Accepts `branding`,
              `default_action_mappings`, `example_payloads`, `preprocessing_script`,
              `static_fields`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/v1/source_providers/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include}, data_source_retrieve_provider_params.DataSourceRetrieveProviderParams
                ),
            ),
            cast_to=SourceProviderResponse,
        )

    def retrieve_status(
        self,
        key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceStatusResponse:
        """
        Returns source activity and workflow-trigger mappings that need action in the
        requested environment.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/v1/sources/{key}/status", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, data_source_retrieve_status_params.DataSourceRetrieveStatusParams
                ),
            ),
            cast_to=SourceStatusResponse,
        )

    def upsert(
        self,
        key: str,
        *,
        environment: str,
        source: SourceRequestParam,
        annotate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceUpsertResponse:
        """
        Creates or updates a source with environment-specific settings, preprocess
        scripts, and event mappings.

        Args:
          environment: The environment slug.

          source: A source request for setting a source and its environment-specific
              configuration.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._put(
            path_template("/v1/sources/{key}", key=key),
            body=maybe_transform({"source": source}, data_source_upsert_params.DataSourceUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                    },
                    data_source_upsert_params.DataSourceUpsertParams,
                ),
            ),
            cast_to=DataSourceUpsertResponse,
        )


class AsyncDataSourcesResource(AsyncAPIResource):
    """Sources receive external events that can trigger Knock actions."""

    @cached_property
    def with_raw_response(self) -> AsyncDataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncDataSourcesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """
        Returns a source with environment-specific settings, preprocess scripts, and
        event mappings.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/v1/sources/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                    },
                    data_source_retrieve_params.DataSourceRetrieveParams,
                ),
            ),
            cast_to=Source,
        )

    async def list_events(
        self,
        key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceEventsResponse:
        """
        Returns known unique events received by a source in the requested environment.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/v1/sources/{key}/events", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, data_source_list_events_params.DataSourceListEventsParams
                ),
            ),
            cast_to=SourceEventsResponse,
        )

    def list_logs(
        self,
        key: str,
        *,
        environment: str,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        date: str | Omit = omit,
        ending_at: Union[str, datetime] | Omit = omit,
        event: str | Omit = omit,
        include: List[Literal["actions"]] | Omit = omit,
        limit: int | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SourceLog, AsyncEntriesCursor[SourceLog]]:
        """Returns event logs received by a source in the requested environment.

        Supports
        filtering by date/time, event, and log ID.

        Args:
          environment: The environment slug.

          id: The log ID to filter by.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          date: Returns event logs that were produced on this date.

          ending_at: Only return source logs at or before this timestamp.

          event: The event name to filter by.

          include: Associated resources to include in the response. Accepts `actions` to include
              the actions executed after receiving each source event.

          limit: The number of entries to fetch per-page.

          starting_at: Only return source logs at or after this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get_api_list(
            path_template("/v1/sources/{key}/logs", key=key),
            page=AsyncEntriesCursor[SourceLog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "id": id,
                        "after": after,
                        "before": before,
                        "date": date,
                        "ending_at": ending_at,
                        "event": event,
                        "include": include,
                        "limit": limit,
                        "starting_at": starting_at,
                    },
                    data_source_list_logs_params.DataSourceListLogsParams,
                ),
            ),
            model=SourceLog,
        )

    async def list_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceProvidersResponse:
        """Returns the source provider templates available for creating sources."""
        return await self._get(
            "/v1/source_providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceProvidersResponse,
        )

    async def list_sources(
        self,
        *,
        annotate: bool | Omit = omit,
        environment: str | Omit = omit,
        include: List[Literal["environment_settings"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourcesResponse:
        """
        Returns connected sources for the project.

        Args:
          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          environment: The environment slug.

          include: Associated resources to include in each source. Accepts `environment_settings`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "annotate": annotate,
                        "environment": environment,
                        "include": include,
                    },
                    data_source_list_sources_params.DataSourceListSourcesParams,
                ),
            ),
            cast_to=SourcesResponse,
        )

    async def rehearse(
        self,
        key: str,
        *,
        environment: str,
        payload: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRehearseResponse:
        """
        Sends an arbitrary payload through the source's parse, preprocess, and mapping
        pipeline in the requested environment. This endpoint cannot be run in production
        environments.

        Args:
          environment: The environment slug.

          payload: An arbitrary payload to send through the source's parse, preprocess, and mapping
              pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._post(
            path_template("/v1/sources/{key}/rehearse", key=key),
            body=await async_maybe_transform(
                {"payload": payload}, data_source_rehearse_params.DataSourceRehearseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, data_source_rehearse_params.DataSourceRehearseParams
                ),
            ),
            cast_to=SourceRehearseResponse,
        )

    async def retrieve_provider(
        self,
        key: str,
        *,
        include: List[
            Literal["branding", "default_action_mappings", "example_payloads", "preprocessing_script", "static_fields"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceProviderResponse:
        """
        Returns a source provider template available for creating sources.

        Args:
          include: Associated resources to include in the response. Accepts `branding`,
              `default_action_mappings`, `example_payloads`, `preprocessing_script`,
              `static_fields`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/v1/source_providers/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include": include}, data_source_retrieve_provider_params.DataSourceRetrieveProviderParams
                ),
            ),
            cast_to=SourceProviderResponse,
        )

    async def retrieve_status(
        self,
        key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceStatusResponse:
        """
        Returns source activity and workflow-trigger mappings that need action in the
        requested environment.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/v1/sources/{key}/status", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, data_source_retrieve_status_params.DataSourceRetrieveStatusParams
                ),
            ),
            cast_to=SourceStatusResponse,
        )

    async def upsert(
        self,
        key: str,
        *,
        environment: str,
        source: SourceRequestParam,
        annotate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceUpsertResponse:
        """
        Creates or updates a source with environment-specific settings, preprocess
        scripts, and event mappings.

        Args:
          environment: The environment slug.

          source: A source request for setting a source and its environment-specific
              configuration.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._put(
            path_template("/v1/sources/{key}", key=key),
            body=await async_maybe_transform({"source": source}, data_source_upsert_params.DataSourceUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                    },
                    data_source_upsert_params.DataSourceUpsertParams,
                ),
            ),
            cast_to=DataSourceUpsertResponse,
        )


class DataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.retrieve = to_raw_response_wrapper(
            data_sources.retrieve,
        )
        self.list_events = to_raw_response_wrapper(
            data_sources.list_events,
        )
        self.list_logs = to_raw_response_wrapper(
            data_sources.list_logs,
        )
        self.list_providers = to_raw_response_wrapper(
            data_sources.list_providers,
        )
        self.list_sources = to_raw_response_wrapper(
            data_sources.list_sources,
        )
        self.rehearse = to_raw_response_wrapper(
            data_sources.rehearse,
        )
        self.retrieve_provider = to_raw_response_wrapper(
            data_sources.retrieve_provider,
        )
        self.retrieve_status = to_raw_response_wrapper(
            data_sources.retrieve_status,
        )
        self.upsert = to_raw_response_wrapper(
            data_sources.upsert,
        )


class AsyncDataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.retrieve = async_to_raw_response_wrapper(
            data_sources.retrieve,
        )
        self.list_events = async_to_raw_response_wrapper(
            data_sources.list_events,
        )
        self.list_logs = async_to_raw_response_wrapper(
            data_sources.list_logs,
        )
        self.list_providers = async_to_raw_response_wrapper(
            data_sources.list_providers,
        )
        self.list_sources = async_to_raw_response_wrapper(
            data_sources.list_sources,
        )
        self.rehearse = async_to_raw_response_wrapper(
            data_sources.rehearse,
        )
        self.retrieve_provider = async_to_raw_response_wrapper(
            data_sources.retrieve_provider,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            data_sources.retrieve_status,
        )
        self.upsert = async_to_raw_response_wrapper(
            data_sources.upsert,
        )


class DataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.retrieve = to_streamed_response_wrapper(
            data_sources.retrieve,
        )
        self.list_events = to_streamed_response_wrapper(
            data_sources.list_events,
        )
        self.list_logs = to_streamed_response_wrapper(
            data_sources.list_logs,
        )
        self.list_providers = to_streamed_response_wrapper(
            data_sources.list_providers,
        )
        self.list_sources = to_streamed_response_wrapper(
            data_sources.list_sources,
        )
        self.rehearse = to_streamed_response_wrapper(
            data_sources.rehearse,
        )
        self.retrieve_provider = to_streamed_response_wrapper(
            data_sources.retrieve_provider,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            data_sources.retrieve_status,
        )
        self.upsert = to_streamed_response_wrapper(
            data_sources.upsert,
        )


class AsyncDataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.retrieve = async_to_streamed_response_wrapper(
            data_sources.retrieve,
        )
        self.list_events = async_to_streamed_response_wrapper(
            data_sources.list_events,
        )
        self.list_logs = async_to_streamed_response_wrapper(
            data_sources.list_logs,
        )
        self.list_providers = async_to_streamed_response_wrapper(
            data_sources.list_providers,
        )
        self.list_sources = async_to_streamed_response_wrapper(
            data_sources.list_sources,
        )
        self.rehearse = async_to_streamed_response_wrapper(
            data_sources.rehearse,
        )
        self.retrieve_provider = async_to_streamed_response_wrapper(
            data_sources.retrieve_provider,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            data_sources.retrieve_status,
        )
        self.upsert = async_to_streamed_response_wrapper(
            data_sources.upsert,
        )

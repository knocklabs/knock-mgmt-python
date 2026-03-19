# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import channel_group_list_params, channel_group_upsert_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.channel_group import ChannelGroup
from ..types.channel_group_upsert_response import ChannelGroupUpsertResponse

__all__ = ["ChannelGroupsResource", "AsyncChannelGroupsResource"]


class ChannelGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return ChannelGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return ChannelGroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        channel_group_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelGroup:
        """
        Get a channel group by its key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_group_key:
            raise ValueError(f"Expected a non-empty value for `channel_group_key` but received {channel_group_key!r}")
        return self._get(
            path_template("/v1/channel_groups/{channel_group_key}", channel_group_key=channel_group_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGroup,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[ChannelGroup]:
        """Returns a paginated list of channel groups.

        Note: the list of channel groups is
        across the entire account, not scoped to an environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/channel_groups",
            page=SyncEntriesCursor[ChannelGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_group_list_params.ChannelGroupListParams,
                ),
            ),
            model=ChannelGroup,
        )

    def delete(
        self,
        channel_group_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archives (soft deletes) a channel group by key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_group_key:
            raise ValueError(f"Expected a non-empty value for `channel_group_key` but received {channel_group_key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/channel_groups/{channel_group_key}", channel_group_key=channel_group_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upsert(
        self,
        channel_group_key: str,
        *,
        channel_group: channel_group_upsert_params.ChannelGroup,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelGroupUpsertResponse:
        """
        Creates or updates a channel group by key.

        Args:
          channel_group: A request to create or update a channel group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_group_key:
            raise ValueError(f"Expected a non-empty value for `channel_group_key` but received {channel_group_key!r}")
        return self._put(
            path_template("/v1/channel_groups/{channel_group_key}", channel_group_key=channel_group_key),
            body=maybe_transform(
                {"channel_group": channel_group}, channel_group_upsert_params.ChannelGroupUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGroupUpsertResponse,
        )


class AsyncChannelGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncChannelGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        channel_group_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelGroup:
        """
        Get a channel group by its key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_group_key:
            raise ValueError(f"Expected a non-empty value for `channel_group_key` but received {channel_group_key!r}")
        return await self._get(
            path_template("/v1/channel_groups/{channel_group_key}", channel_group_key=channel_group_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGroup,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChannelGroup, AsyncEntriesCursor[ChannelGroup]]:
        """Returns a paginated list of channel groups.

        Note: the list of channel groups is
        across the entire account, not scoped to an environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/channel_groups",
            page=AsyncEntriesCursor[ChannelGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_group_list_params.ChannelGroupListParams,
                ),
            ),
            model=ChannelGroup,
        )

    async def delete(
        self,
        channel_group_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archives (soft deletes) a channel group by key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_group_key:
            raise ValueError(f"Expected a non-empty value for `channel_group_key` but received {channel_group_key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/channel_groups/{channel_group_key}", channel_group_key=channel_group_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upsert(
        self,
        channel_group_key: str,
        *,
        channel_group: channel_group_upsert_params.ChannelGroup,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelGroupUpsertResponse:
        """
        Creates or updates a channel group by key.

        Args:
          channel_group: A request to create or update a channel group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_group_key:
            raise ValueError(f"Expected a non-empty value for `channel_group_key` but received {channel_group_key!r}")
        return await self._put(
            path_template("/v1/channel_groups/{channel_group_key}", channel_group_key=channel_group_key),
            body=await async_maybe_transform(
                {"channel_group": channel_group}, channel_group_upsert_params.ChannelGroupUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGroupUpsertResponse,
        )


class ChannelGroupsResourceWithRawResponse:
    def __init__(self, channel_groups: ChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.retrieve = to_raw_response_wrapper(
            channel_groups.retrieve,
        )
        self.list = to_raw_response_wrapper(
            channel_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            channel_groups.delete,
        )
        self.upsert = to_raw_response_wrapper(
            channel_groups.upsert,
        )


class AsyncChannelGroupsResourceWithRawResponse:
    def __init__(self, channel_groups: AsyncChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.retrieve = async_to_raw_response_wrapper(
            channel_groups.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            channel_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            channel_groups.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            channel_groups.upsert,
        )


class ChannelGroupsResourceWithStreamingResponse:
    def __init__(self, channel_groups: ChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.retrieve = to_streamed_response_wrapper(
            channel_groups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            channel_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            channel_groups.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            channel_groups.upsert,
        )


class AsyncChannelGroupsResourceWithStreamingResponse:
    def __init__(self, channel_groups: AsyncChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.retrieve = async_to_streamed_response_wrapper(
            channel_groups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            channel_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            channel_groups.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            channel_groups.upsert,
        )

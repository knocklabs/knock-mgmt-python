# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import channel_group_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.channel_group import ChannelGroup

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


class ChannelGroupsResourceWithRawResponse:
    def __init__(self, channel_groups: ChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.list = to_raw_response_wrapper(
            channel_groups.list,
        )


class AsyncChannelGroupsResourceWithRawResponse:
    def __init__(self, channel_groups: AsyncChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.list = async_to_raw_response_wrapper(
            channel_groups.list,
        )


class ChannelGroupsResourceWithStreamingResponse:
    def __init__(self, channel_groups: ChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.list = to_streamed_response_wrapper(
            channel_groups.list,
        )


class AsyncChannelGroupsResourceWithStreamingResponse:
    def __init__(self, channel_groups: AsyncChannelGroupsResource) -> None:
        self._channel_groups = channel_groups

        self.list = async_to_streamed_response_wrapper(
            channel_groups.list,
        )

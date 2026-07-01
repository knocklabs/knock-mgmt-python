# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import (
    broadcast_list_params,
    broadcast_send_params,
    broadcast_cancel_params,
    broadcast_upsert_params,
    broadcast_retrieve_params,
    broadcast_validate_params,
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
from ..types.broadcast import Broadcast
from ..types.broadcast_request_param import BroadcastRequestParam
from ..types.broadcast_send_response import BroadcastSendResponse
from ..types.broadcast_cancel_response import BroadcastCancelResponse
from ..types.broadcast_upsert_response import BroadcastUpsertResponse
from ..types.broadcast_validate_response import BroadcastValidateResponse

__all__ = ["BroadcastsResource", "AsyncBroadcastsResource"]


class BroadcastsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return BroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return BroadcastsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        broadcast_key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Get a broadcast by its key in a given environment.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return self._get(
            path_template("/v1/broadcasts/{broadcast_key}", broadcast_key=broadcast_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "branch": branch,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    broadcast_retrieve_params.BroadcastRetrieveParams,
                ),
            ),
            cast_to=Broadcast,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Broadcast]:
        """Returns a paginated list of broadcasts available in a given environment.

        The
        broadcasts are returned ordered by creation time (newest first).

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/broadcasts",
            page=SyncEntriesCursor[Broadcast],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "after": after,
                        "annotate": annotate,
                        "before": before,
                        "branch": branch,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    broadcast_list_params.BroadcastListParams,
                ),
            ),
            model=Broadcast,
        )

    def cancel(
        self,
        broadcast_key: str,
        *,
        environment: str,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCancelResponse:
        """Cancels sending a scheduled broadcast.

        The broadcast will return to draft
        status.

        Args:
          environment: The environment slug.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return self._put(
            path_template("/v1/broadcasts/{broadcast_key}/cancel", broadcast_key=broadcast_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "branch": branch,
                    },
                    broadcast_cancel_params.BroadcastCancelParams,
                ),
            ),
            cast_to=BroadcastCancelResponse,
        )

    def send(
        self,
        broadcast_key: str,
        *,
        environment: str,
        branch: str | Omit = omit,
        send_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSendResponse:
        """
        Sends a broadcast immediately or schedules it to send at a future time.

        Args:
          environment: The environment slug.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          send_at: When to send the broadcast. If provided, the broadcast will be scheduled to send
              at this time. Must be in ISO 8601 UTC format. If not provided, the broadcast
              will be sent immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return self._put(
            path_template("/v1/broadcasts/{broadcast_key}/send", broadcast_key=broadcast_key),
            body=maybe_transform({"send_at": send_at}, broadcast_send_params.BroadcastSendParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "branch": branch,
                    },
                    broadcast_send_params.BroadcastSendParams,
                ),
            ),
            cast_to=BroadcastSendResponse,
        )

    def upsert(
        self,
        broadcast_key: str,
        *,
        environment: str,
        broadcast: BroadcastRequestParam,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastUpsertResponse:
        """
        Updates a broadcast of a given key, or creates a new one if it does not yet
        exist.

        Args:
          environment: The environment slug.

          broadcast: A broadcast request for upserting a broadcast.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return self._put(
            path_template("/v1/broadcasts/{broadcast_key}", broadcast_key=broadcast_key),
            body=maybe_transform({"broadcast": broadcast}, broadcast_upsert_params.BroadcastUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "branch": branch,
                    },
                    broadcast_upsert_params.BroadcastUpsertParams,
                ),
            ),
            cast_to=BroadcastUpsertResponse,
        )

    def validate(
        self,
        broadcast_key: str,
        *,
        environment: str,
        broadcast: BroadcastRequestParam,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastValidateResponse:
        """
        Validates a broadcast payload without persisting it.

        Args:
          environment: The environment slug.

          broadcast: A broadcast request for upserting a broadcast.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return self._put(
            path_template("/v1/broadcasts/{broadcast_key}/validate", broadcast_key=broadcast_key),
            body=maybe_transform({"broadcast": broadcast}, broadcast_validate_params.BroadcastValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "branch": branch,
                    },
                    broadcast_validate_params.BroadcastValidateParams,
                ),
            ),
            cast_to=BroadcastValidateResponse,
        )


class AsyncBroadcastsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncBroadcastsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        broadcast_key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Get a broadcast by its key in a given environment.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return await self._get(
            path_template("/v1/broadcasts/{broadcast_key}", broadcast_key=broadcast_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "branch": branch,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    broadcast_retrieve_params.BroadcastRetrieveParams,
                ),
            ),
            cast_to=Broadcast,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Broadcast, AsyncEntriesCursor[Broadcast]]:
        """Returns a paginated list of broadcasts available in a given environment.

        The
        broadcasts are returned ordered by creation time (newest first).

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/broadcasts",
            page=AsyncEntriesCursor[Broadcast],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "after": after,
                        "annotate": annotate,
                        "before": before,
                        "branch": branch,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    broadcast_list_params.BroadcastListParams,
                ),
            ),
            model=Broadcast,
        )

    async def cancel(
        self,
        broadcast_key: str,
        *,
        environment: str,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastCancelResponse:
        """Cancels sending a scheduled broadcast.

        The broadcast will return to draft
        status.

        Args:
          environment: The environment slug.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return await self._put(
            path_template("/v1/broadcasts/{broadcast_key}/cancel", broadcast_key=broadcast_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "branch": branch,
                    },
                    broadcast_cancel_params.BroadcastCancelParams,
                ),
            ),
            cast_to=BroadcastCancelResponse,
        )

    async def send(
        self,
        broadcast_key: str,
        *,
        environment: str,
        branch: str | Omit = omit,
        send_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastSendResponse:
        """
        Sends a broadcast immediately or schedules it to send at a future time.

        Args:
          environment: The environment slug.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          send_at: When to send the broadcast. If provided, the broadcast will be scheduled to send
              at this time. Must be in ISO 8601 UTC format. If not provided, the broadcast
              will be sent immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return await self._put(
            path_template("/v1/broadcasts/{broadcast_key}/send", broadcast_key=broadcast_key),
            body=await async_maybe_transform({"send_at": send_at}, broadcast_send_params.BroadcastSendParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "branch": branch,
                    },
                    broadcast_send_params.BroadcastSendParams,
                ),
            ),
            cast_to=BroadcastSendResponse,
        )

    async def upsert(
        self,
        broadcast_key: str,
        *,
        environment: str,
        broadcast: BroadcastRequestParam,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastUpsertResponse:
        """
        Updates a broadcast of a given key, or creates a new one if it does not yet
        exist.

        Args:
          environment: The environment slug.

          broadcast: A broadcast request for upserting a broadcast.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return await self._put(
            path_template("/v1/broadcasts/{broadcast_key}", broadcast_key=broadcast_key),
            body=await async_maybe_transform({"broadcast": broadcast}, broadcast_upsert_params.BroadcastUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "branch": branch,
                    },
                    broadcast_upsert_params.BroadcastUpsertParams,
                ),
            ),
            cast_to=BroadcastUpsertResponse,
        )

    async def validate(
        self,
        broadcast_key: str,
        *,
        environment: str,
        broadcast: BroadcastRequestParam,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastValidateResponse:
        """
        Validates a broadcast payload without persisting it.

        Args:
          environment: The environment slug.

          broadcast: A broadcast request for upserting a broadcast.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_key:
            raise ValueError(f"Expected a non-empty value for `broadcast_key` but received {broadcast_key!r}")
        return await self._put(
            path_template("/v1/broadcasts/{broadcast_key}/validate", broadcast_key=broadcast_key),
            body=await async_maybe_transform(
                {"broadcast": broadcast}, broadcast_validate_params.BroadcastValidateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "branch": branch,
                    },
                    broadcast_validate_params.BroadcastValidateParams,
                ),
            ),
            cast_to=BroadcastValidateResponse,
        )


class BroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            broadcasts.list,
        )
        self.cancel = to_raw_response_wrapper(
            broadcasts.cancel,
        )
        self.send = to_raw_response_wrapper(
            broadcasts.send,
        )
        self.upsert = to_raw_response_wrapper(
            broadcasts.upsert,
        )
        self.validate = to_raw_response_wrapper(
            broadcasts.validate,
        )


class AsyncBroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = async_to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            broadcasts.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            broadcasts.cancel,
        )
        self.send = async_to_raw_response_wrapper(
            broadcasts.send,
        )
        self.upsert = async_to_raw_response_wrapper(
            broadcasts.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            broadcasts.validate,
        )


class BroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.cancel = to_streamed_response_wrapper(
            broadcasts.cancel,
        )
        self.send = to_streamed_response_wrapper(
            broadcasts.send,
        )
        self.upsert = to_streamed_response_wrapper(
            broadcasts.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            broadcasts.validate,
        )


class AsyncBroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = async_to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            broadcasts.cancel,
        )
        self.send = async_to_streamed_response_wrapper(
            broadcasts.send,
        )
        self.upsert = async_to_streamed_response_wrapper(
            broadcasts.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            broadcasts.validate,
        )

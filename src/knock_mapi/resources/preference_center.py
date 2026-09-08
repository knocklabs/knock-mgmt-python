# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import preference_center_reset_params, preference_center_upsert_params, preference_center_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.preference_center_reset_response import PreferenceCenterResetResponse
from ..types.preference_center_upsert_response import PreferenceCenterUpsertResponse
from ..types.preference_center_retrieve_response import PreferenceCenterRetrieveResponse

__all__ = ["PreferenceCenterResource", "AsyncPreferenceCenterResource"]


class PreferenceCenterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreferenceCenterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return PreferenceCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferenceCenterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return PreferenceCenterResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterRetrieveResponse:
        """
        Returns the preference center configuration for the given environment.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/preference_center",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, preference_center_retrieve_params.PreferenceCenterRetrieveParams
                ),
            ),
            cast_to=PreferenceCenterRetrieveResponse,
        )

    def reset(
        self,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterResetResponse:
        """
        Resets the preference center configuration for the given environment to the
        built-in default content. The `enabled` flag is preserved.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/preference_center/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, preference_center_reset_params.PreferenceCenterResetParams
                ),
            ),
            cast_to=PreferenceCenterResetResponse,
        )

    def upsert(
        self,
        *,
        config: object,
        environment: str | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterUpsertResponse:
        """
        Creates or updates the preference center configuration for the given
        environment.

        Args:
          config: The preference center configuration document.

          environment: The environment slug. When omitted, the account's default environment is used.

          enabled: Whether the preference center is enabled for recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/preference_center",
            body=maybe_transform(
                {
                    "config": config,
                    "enabled": enabled,
                },
                preference_center_upsert_params.PreferenceCenterUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, preference_center_upsert_params.PreferenceCenterUpsertParams
                ),
            ),
            cast_to=PreferenceCenterUpsertResponse,
        )


class AsyncPreferenceCenterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreferenceCenterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferenceCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferenceCenterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncPreferenceCenterResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterRetrieveResponse:
        """
        Returns the preference center configuration for the given environment.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/preference_center",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, preference_center_retrieve_params.PreferenceCenterRetrieveParams
                ),
            ),
            cast_to=PreferenceCenterRetrieveResponse,
        )

    async def reset(
        self,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterResetResponse:
        """
        Resets the preference center configuration for the given environment to the
        built-in default content. The `enabled` flag is preserved.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/preference_center/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, preference_center_reset_params.PreferenceCenterResetParams
                ),
            ),
            cast_to=PreferenceCenterResetResponse,
        )

    async def upsert(
        self,
        *,
        config: object,
        environment: str | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterUpsertResponse:
        """
        Creates or updates the preference center configuration for the given
        environment.

        Args:
          config: The preference center configuration document.

          environment: The environment slug. When omitted, the account's default environment is used.

          enabled: Whether the preference center is enabled for recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/preference_center",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "enabled": enabled,
                },
                preference_center_upsert_params.PreferenceCenterUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, preference_center_upsert_params.PreferenceCenterUpsertParams
                ),
            ),
            cast_to=PreferenceCenterUpsertResponse,
        )


class PreferenceCenterResourceWithRawResponse:
    def __init__(self, preference_center: PreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.retrieve = to_raw_response_wrapper(
            preference_center.retrieve,
        )
        self.reset = to_raw_response_wrapper(
            preference_center.reset,
        )
        self.upsert = to_raw_response_wrapper(
            preference_center.upsert,
        )


class AsyncPreferenceCenterResourceWithRawResponse:
    def __init__(self, preference_center: AsyncPreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.retrieve = async_to_raw_response_wrapper(
            preference_center.retrieve,
        )
        self.reset = async_to_raw_response_wrapper(
            preference_center.reset,
        )
        self.upsert = async_to_raw_response_wrapper(
            preference_center.upsert,
        )


class PreferenceCenterResourceWithStreamingResponse:
    def __init__(self, preference_center: PreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.retrieve = to_streamed_response_wrapper(
            preference_center.retrieve,
        )
        self.reset = to_streamed_response_wrapper(
            preference_center.reset,
        )
        self.upsert = to_streamed_response_wrapper(
            preference_center.upsert,
        )


class AsyncPreferenceCenterResourceWithStreamingResponse:
    def __init__(self, preference_center: AsyncPreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.retrieve = async_to_streamed_response_wrapper(
            preference_center.retrieve,
        )
        self.reset = async_to_streamed_response_wrapper(
            preference_center.reset,
        )
        self.upsert = async_to_streamed_response_wrapper(
            preference_center.upsert,
        )

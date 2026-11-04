# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.environments import default_update_params
from ...types.environments.environment_defaults import EnvironmentDefaults
from ...types.environments.environment_defaults_preference_set_param import EnvironmentDefaultsPreferenceSetParam

__all__ = ["DefaultsResource", "AsyncDefaultsResource"]


class DefaultsResource(SyncAPIResource):
    """
    Environments are isolated instances of your account that map to your infrastructure.
    """

    @cached_property
    def with_raw_response(self) -> DefaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return DefaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return DefaultsResourceWithStreamingResponse(self)

    def update(
        self,
        environment_slug: str,
        *,
        preference_set: Optional[EnvironmentDefaultsPreferenceSetParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentDefaults:
        """Creates or replaces the default settings for an environment.

        The change applies
        to the environment immediately, including production. It is not committed or
        promoted, and concurrent writes are last-write-wins. The `preference_set`
        replaces any existing set in full, and `null` clears it.

        Args:
          preference_set: A preference set applied to every recipient in the environment unless the
              recipient overrides it. The `__persistence_strategy__` and `__strategy__` keys
              are not supported, because defaults are always replaced in full.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_slug:
            raise ValueError(f"Expected a non-empty value for `environment_slug` but received {environment_slug!r}")
        return self._put(
            path_template("/v1/environments/{environment_slug}/defaults", environment_slug=environment_slug),
            body=maybe_transform({"preference_set": preference_set}, default_update_params.DefaultUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentDefaults,
        )

    def list(
        self,
        environment_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentDefaults:
        """Returns the default settings for an environment.

        When no defaults have been set,
        `preference_set` and both timestamps are `null`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_slug:
            raise ValueError(f"Expected a non-empty value for `environment_slug` but received {environment_slug!r}")
        return self._get(
            path_template("/v1/environments/{environment_slug}/defaults", environment_slug=environment_slug),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentDefaults,
        )


class AsyncDefaultsResource(AsyncAPIResource):
    """
    Environments are isolated instances of your account that map to your infrastructure.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDefaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncDefaultsResourceWithStreamingResponse(self)

    async def update(
        self,
        environment_slug: str,
        *,
        preference_set: Optional[EnvironmentDefaultsPreferenceSetParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentDefaults:
        """Creates or replaces the default settings for an environment.

        The change applies
        to the environment immediately, including production. It is not committed or
        promoted, and concurrent writes are last-write-wins. The `preference_set`
        replaces any existing set in full, and `null` clears it.

        Args:
          preference_set: A preference set applied to every recipient in the environment unless the
              recipient overrides it. The `__persistence_strategy__` and `__strategy__` keys
              are not supported, because defaults are always replaced in full.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_slug:
            raise ValueError(f"Expected a non-empty value for `environment_slug` but received {environment_slug!r}")
        return await self._put(
            path_template("/v1/environments/{environment_slug}/defaults", environment_slug=environment_slug),
            body=await async_maybe_transform(
                {"preference_set": preference_set}, default_update_params.DefaultUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentDefaults,
        )

    async def list(
        self,
        environment_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentDefaults:
        """Returns the default settings for an environment.

        When no defaults have been set,
        `preference_set` and both timestamps are `null`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment_slug:
            raise ValueError(f"Expected a non-empty value for `environment_slug` but received {environment_slug!r}")
        return await self._get(
            path_template("/v1/environments/{environment_slug}/defaults", environment_slug=environment_slug),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentDefaults,
        )


class DefaultsResourceWithRawResponse:
    def __init__(self, defaults: DefaultsResource) -> None:
        self._defaults = defaults

        self.update = to_raw_response_wrapper(
            defaults.update,
        )
        self.list = to_raw_response_wrapper(
            defaults.list,
        )


class AsyncDefaultsResourceWithRawResponse:
    def __init__(self, defaults: AsyncDefaultsResource) -> None:
        self._defaults = defaults

        self.update = async_to_raw_response_wrapper(
            defaults.update,
        )
        self.list = async_to_raw_response_wrapper(
            defaults.list,
        )


class DefaultsResourceWithStreamingResponse:
    def __init__(self, defaults: DefaultsResource) -> None:
        self._defaults = defaults

        self.update = to_streamed_response_wrapper(
            defaults.update,
        )
        self.list = to_streamed_response_wrapper(
            defaults.list,
        )


class AsyncDefaultsResourceWithStreamingResponse:
    def __init__(self, defaults: AsyncDefaultsResource) -> None:
        self._defaults = defaults

        self.update = async_to_streamed_response_wrapper(
            defaults.update,
        )
        self.list = async_to_streamed_response_wrapper(
            defaults.list,
        )

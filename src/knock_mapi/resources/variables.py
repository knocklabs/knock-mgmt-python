# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import variable_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.variable import Variable

__all__ = ["VariablesResource", "AsyncVariablesResource"]


class VariablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return VariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return VariablesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Variable:
        """
        Returns a single variable by key with per-environment value overrides.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/v1/variables/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Variable,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        limit: int | Omit = omit,
        type: Literal["public", "secret"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Variable]:
        """Returns a list of variables.

        When an environment is specified, returns
        per-environment variables. Otherwise, returns project-scoped variables with
        per-environment overrides.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          limit: The number of entries to fetch per-page.

          type: Filter variables by type. Supports 'public' or 'secret'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/variables",
            page=SyncEntriesCursor[Variable],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "after": after,
                        "before": before,
                        "branch": branch,
                        "limit": limit,
                        "type": type,
                    },
                    variable_list_params.VariableListParams,
                ),
            ),
            model=Variable,
        )


class AsyncVariablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncVariablesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Variable:
        """
        Returns a single variable by key with per-environment value overrides.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/v1/variables/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Variable,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        limit: int | Omit = omit,
        type: Literal["public", "secret"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Variable, AsyncEntriesCursor[Variable]]:
        """Returns a list of variables.

        When an environment is specified, returns
        per-environment variables. Otherwise, returns project-scoped variables with
        per-environment overrides.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          limit: The number of entries to fetch per-page.

          type: Filter variables by type. Supports 'public' or 'secret'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/variables",
            page=AsyncEntriesCursor[Variable],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "after": after,
                        "before": before,
                        "branch": branch,
                        "limit": limit,
                        "type": type,
                    },
                    variable_list_params.VariableListParams,
                ),
            ),
            model=Variable,
        )


class VariablesResourceWithRawResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.retrieve = to_raw_response_wrapper(
            variables.retrieve,
        )
        self.list = to_raw_response_wrapper(
            variables.list,
        )


class AsyncVariablesResourceWithRawResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.retrieve = async_to_raw_response_wrapper(
            variables.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            variables.list,
        )


class VariablesResourceWithStreamingResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.retrieve = to_streamed_response_wrapper(
            variables.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            variables.list,
        )


class AsyncVariablesResourceWithStreamingResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.retrieve = async_to_streamed_response_wrapper(
            variables.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            variables.list,
        )

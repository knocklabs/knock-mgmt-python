# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import variable_list_params, variable_delete_params, variable_upsert_params
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
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
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used
              for authorization while the response remains project-scoped.

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
                        "after": after,
                        "before": before,
                        "branch": branch,
                        "environment": environment,
                        "limit": limit,
                        "type": type,
                    },
                    variable_list_params.VariableListParams,
                ),
            ),
            model=Variable,
        )

    def delete(
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
    ) -> None:
        """Deletes a variable and all of its environment overrides.

        When an environment is
        specified, only the override for that environment is cleared, so the default
        value applies there.

        Args:
          environment: The environment slug. When provided, only the variable's override for this
              environment is cleared. When omitted, the whole variable is deleted and the
              account's default environment is used for authorization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/variables/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, variable_delete_params.VariableDeleteParams),
            ),
            cast_to=NoneType,
        )

    def upsert(
        self,
        key: str,
        *,
        type: Literal["public", "secret"],
        description: Optional[str] | Omit = omit,
        environment_values: Dict[str, Optional[str]] | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Variable:
        """
        Creates or updates a variable by key, along with its per-environment overrides.
        On an update, any attribute or environment that is omitted or null is left
        unchanged, and an empty string unsets it. The response never includes the value
        of a secret variable.

        Args:
          type: The type of the variable. Required, and it cannot be changed after the variable
              is created.

          description: The description of the variable. When omitted or null on an update, the existing
              description is kept. An empty string clears it.

          environment_values: A map of root environment slugs to override values. An environment that is
              omitted or null is left unchanged. An empty string clears the override, so the
              default value applies.

          value: The default value of the variable. Required when creating a variable. When
              omitted or null on an update, the existing value is kept. An empty string clears
              the default value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._put(
            path_template("/v1/variables/{key}", key=key),
            body=maybe_transform(
                {
                    "type": type,
                    "description": description,
                    "environment_values": environment_values,
                    "value": value,
                },
                variable_upsert_params.VariableUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Variable,
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
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
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used
              for authorization while the response remains project-scoped.

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
                        "after": after,
                        "before": before,
                        "branch": branch,
                        "environment": environment,
                        "limit": limit,
                        "type": type,
                    },
                    variable_list_params.VariableListParams,
                ),
            ),
            model=Variable,
        )

    async def delete(
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
    ) -> None:
        """Deletes a variable and all of its environment overrides.

        When an environment is
        specified, only the override for that environment is cleared, so the default
        value applies there.

        Args:
          environment: The environment slug. When provided, only the variable's override for this
              environment is cleared. When omitted, the whole variable is deleted and the
              account's default environment is used for authorization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/variables/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, variable_delete_params.VariableDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def upsert(
        self,
        key: str,
        *,
        type: Literal["public", "secret"],
        description: Optional[str] | Omit = omit,
        environment_values: Dict[str, Optional[str]] | Omit = omit,
        value: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Variable:
        """
        Creates or updates a variable by key, along with its per-environment overrides.
        On an update, any attribute or environment that is omitted or null is left
        unchanged, and an empty string unsets it. The response never includes the value
        of a secret variable.

        Args:
          type: The type of the variable. Required, and it cannot be changed after the variable
              is created.

          description: The description of the variable. When omitted or null on an update, the existing
              description is kept. An empty string clears it.

          environment_values: A map of root environment slugs to override values. An environment that is
              omitted or null is left unchanged. An empty string clears the override, so the
              default value applies.

          value: The default value of the variable. Required when creating a variable. When
              omitted or null on an update, the existing value is kept. An empty string clears
              the default value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._put(
            path_template("/v1/variables/{key}", key=key),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "description": description,
                    "environment_values": environment_values,
                    "value": value,
                },
                variable_upsert_params.VariableUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Variable,
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
        self.delete = to_raw_response_wrapper(
            variables.delete,
        )
        self.upsert = to_raw_response_wrapper(
            variables.upsert,
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
        self.delete = async_to_raw_response_wrapper(
            variables.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            variables.upsert,
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
        self.delete = to_streamed_response_wrapper(
            variables.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            variables.upsert,
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
        self.delete = async_to_streamed_response_wrapper(
            variables.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            variables.upsert,
        )

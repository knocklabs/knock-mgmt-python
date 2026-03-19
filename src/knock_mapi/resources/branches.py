# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import branch_list_params, branch_create_params, branch_delete_params, branch_retrieve_params
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
from ..types.branch import Branch

__all__ = ["BranchesResource", "AsyncBranchesResource"]


class BranchesResource(SyncAPIResource):
    """Branches in Knock are a way to isolate changes to your Knock resources."""

    @cached_property
    def with_raw_response(self) -> BranchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return BranchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BranchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return BranchesResourceWithStreamingResponse(self)

    def create(
        self,
        branch_slug: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Branch:
        """
        Creates a new branch off of the development environment with the given slug.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not branch_slug:
            raise ValueError(f"Expected a non-empty value for `branch_slug` but received {branch_slug!r}")
        return self._post(
            path_template("/v1/branches/{branch_slug}", branch_slug=branch_slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, branch_create_params.BranchCreateParams),
            ),
            cast_to=Branch,
        )

    def retrieve(
        self,
        branch_slug: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Branch:
        """
        Returns a single branch by the `branch_slug`.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not branch_slug:
            raise ValueError(f"Expected a non-empty value for `branch_slug` but received {branch_slug!r}")
        return self._get(
            path_template("/v1/branches/{branch_slug}", branch_slug=branch_slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, branch_retrieve_params.BranchRetrieveParams),
            ),
            cast_to=Branch,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Branch]:
        """Returns a paginated list of branches.

        The branches will be returned in order of
        their last commit time (newest first).

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/branches",
            page=SyncEntriesCursor[Branch],
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
                        "limit": limit,
                    },
                    branch_list_params.BranchListParams,
                ),
            ),
            model=Branch,
        )

    def delete(
        self,
        branch_slug: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a branch by the `branch_slug`.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not branch_slug:
            raise ValueError(f"Expected a non-empty value for `branch_slug` but received {branch_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/branches/{branch_slug}", branch_slug=branch_slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, branch_delete_params.BranchDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncBranchesResource(AsyncAPIResource):
    """Branches in Knock are a way to isolate changes to your Knock resources."""

    @cached_property
    def with_raw_response(self) -> AsyncBranchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBranchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBranchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncBranchesResourceWithStreamingResponse(self)

    async def create(
        self,
        branch_slug: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Branch:
        """
        Creates a new branch off of the development environment with the given slug.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not branch_slug:
            raise ValueError(f"Expected a non-empty value for `branch_slug` but received {branch_slug!r}")
        return await self._post(
            path_template("/v1/branches/{branch_slug}", branch_slug=branch_slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, branch_create_params.BranchCreateParams
                ),
            ),
            cast_to=Branch,
        )

    async def retrieve(
        self,
        branch_slug: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Branch:
        """
        Returns a single branch by the `branch_slug`.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not branch_slug:
            raise ValueError(f"Expected a non-empty value for `branch_slug` but received {branch_slug!r}")
        return await self._get(
            path_template("/v1/branches/{branch_slug}", branch_slug=branch_slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, branch_retrieve_params.BranchRetrieveParams
                ),
            ),
            cast_to=Branch,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Branch, AsyncEntriesCursor[Branch]]:
        """Returns a paginated list of branches.

        The branches will be returned in order of
        their last commit time (newest first).

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/branches",
            page=AsyncEntriesCursor[Branch],
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
                        "limit": limit,
                    },
                    branch_list_params.BranchListParams,
                ),
            ),
            model=Branch,
        )

    async def delete(
        self,
        branch_slug: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a branch by the `branch_slug`.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not branch_slug:
            raise ValueError(f"Expected a non-empty value for `branch_slug` but received {branch_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/branches/{branch_slug}", branch_slug=branch_slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, branch_delete_params.BranchDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class BranchesResourceWithRawResponse:
    def __init__(self, branches: BranchesResource) -> None:
        self._branches = branches

        self.create = to_raw_response_wrapper(
            branches.create,
        )
        self.retrieve = to_raw_response_wrapper(
            branches.retrieve,
        )
        self.list = to_raw_response_wrapper(
            branches.list,
        )
        self.delete = to_raw_response_wrapper(
            branches.delete,
        )


class AsyncBranchesResourceWithRawResponse:
    def __init__(self, branches: AsyncBranchesResource) -> None:
        self._branches = branches

        self.create = async_to_raw_response_wrapper(
            branches.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            branches.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            branches.list,
        )
        self.delete = async_to_raw_response_wrapper(
            branches.delete,
        )


class BranchesResourceWithStreamingResponse:
    def __init__(self, branches: BranchesResource) -> None:
        self._branches = branches

        self.create = to_streamed_response_wrapper(
            branches.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            branches.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            branches.list,
        )
        self.delete = to_streamed_response_wrapper(
            branches.delete,
        )


class AsyncBranchesResourceWithStreamingResponse:
    def __init__(self, branches: AsyncBranchesResource) -> None:
        self._branches = branches

        self.create = async_to_streamed_response_wrapper(
            branches.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            branches.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            branches.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            branches.delete,
        )

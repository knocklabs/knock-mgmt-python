# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import commit_list_params, commit_commit_all_params, commit_promote_all_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.commit import Commit
from ..types.commit_commit_all_response import CommitCommitAllResponse
from ..types.commit_promote_all_response import CommitPromoteAllResponse
from ..types.commit_promote_one_response import CommitPromoteOneResponse

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return CommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return CommitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Commit:
        """
        Retrieve a single commit by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/commits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Commit,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        promoted: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Commit]:
        """Returns a paginated list of commits in a given environment.

        The commits are
        ordered from most recent first.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          limit: The number of entries to fetch per-page.

          promoted: Whether to show commits in the given environment that have not been promoted to
              the subsequent environment (false) or commits which have been promoted (true).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/commits",
            page=SyncEntriesCursor[Commit],
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
                        "promoted": promoted,
                    },
                    commit_list_params.CommitListParams,
                ),
            ),
            model=Commit,
        )

    def commit_all(
        self,
        *,
        environment: str,
        commit_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitCommitAllResponse:
        """
        Commit all changes across all resources in the development environment.

        Args:
          environment: The environment slug.

          commit_message: An optional message to include in a commit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/commits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "commit_message": commit_message,
                    },
                    commit_commit_all_params.CommitCommitAllParams,
                ),
            ),
            cast_to=CommitCommitAllResponse,
        )

    def promote_all(
        self,
        *,
        to_environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitPromoteAllResponse:
        """
        Promote all changes across all resources to the target environment from its
        preceding environment.

        Args:
          to_environment: A slug of the target environment to which you want to promote all changes from
              its directly preceding environment.

              For example, if you have three environments “development”, “staging”, and
              “production” (in that order), setting this param to “production” will promote
              all commits not currently in production from staging.

              Note: This must be a non-development environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/commits/promote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"to_environment": to_environment}, commit_promote_all_params.CommitPromoteAllParams
                ),
            ),
            cast_to=CommitPromoteAllResponse,
        )

    def promote_one(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitPromoteOneResponse:
        """
        Promotes one change to the subsequent environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/commits/{id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitPromoteOneResponse,
        )


class AsyncCommitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncCommitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Commit:
        """
        Retrieve a single commit by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/commits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Commit,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        promoted: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Commit, AsyncEntriesCursor[Commit]]:
        """Returns a paginated list of commits in a given environment.

        The commits are
        ordered from most recent first.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          limit: The number of entries to fetch per-page.

          promoted: Whether to show commits in the given environment that have not been promoted to
              the subsequent environment (false) or commits which have been promoted (true).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/commits",
            page=AsyncEntriesCursor[Commit],
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
                        "promoted": promoted,
                    },
                    commit_list_params.CommitListParams,
                ),
            ),
            model=Commit,
        )

    async def commit_all(
        self,
        *,
        environment: str,
        commit_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitCommitAllResponse:
        """
        Commit all changes across all resources in the development environment.

        Args:
          environment: The environment slug.

          commit_message: An optional message to include in a commit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/commits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "commit_message": commit_message,
                    },
                    commit_commit_all_params.CommitCommitAllParams,
                ),
            ),
            cast_to=CommitCommitAllResponse,
        )

    async def promote_all(
        self,
        *,
        to_environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitPromoteAllResponse:
        """
        Promote all changes across all resources to the target environment from its
        preceding environment.

        Args:
          to_environment: A slug of the target environment to which you want to promote all changes from
              its directly preceding environment.

              For example, if you have three environments “development”, “staging”, and
              “production” (in that order), setting this param to “production” will promote
              all commits not currently in production from staging.

              Note: This must be a non-development environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/commits/promote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"to_environment": to_environment}, commit_promote_all_params.CommitPromoteAllParams
                ),
            ),
            cast_to=CommitPromoteAllResponse,
        )

    async def promote_one(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitPromoteOneResponse:
        """
        Promotes one change to the subsequent environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/commits/{id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitPromoteOneResponse,
        )


class CommitsResourceWithRawResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.retrieve = to_raw_response_wrapper(
            commits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            commits.list,
        )
        self.commit_all = to_raw_response_wrapper(
            commits.commit_all,
        )
        self.promote_all = to_raw_response_wrapper(
            commits.promote_all,
        )
        self.promote_one = to_raw_response_wrapper(
            commits.promote_one,
        )


class AsyncCommitsResourceWithRawResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.retrieve = async_to_raw_response_wrapper(
            commits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            commits.list,
        )
        self.commit_all = async_to_raw_response_wrapper(
            commits.commit_all,
        )
        self.promote_all = async_to_raw_response_wrapper(
            commits.promote_all,
        )
        self.promote_one = async_to_raw_response_wrapper(
            commits.promote_one,
        )


class CommitsResourceWithStreamingResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.retrieve = to_streamed_response_wrapper(
            commits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            commits.list,
        )
        self.commit_all = to_streamed_response_wrapper(
            commits.commit_all,
        )
        self.promote_all = to_streamed_response_wrapper(
            commits.promote_all,
        )
        self.promote_one = to_streamed_response_wrapper(
            commits.promote_one,
        )


class AsyncCommitsResourceWithStreamingResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.retrieve = async_to_streamed_response_wrapper(
            commits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            commits.list,
        )
        self.commit_all = async_to_streamed_response_wrapper(
            commits.commit_all,
        )
        self.promote_all = async_to_streamed_response_wrapper(
            commits.promote_all,
        )
        self.promote_one = async_to_streamed_response_wrapper(
            commits.promote_one,
        )

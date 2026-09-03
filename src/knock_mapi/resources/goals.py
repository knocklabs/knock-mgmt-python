# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    goal_list_params,
    goal_clone_params,
    goal_upsert_params,
    goal_archive_params,
    goal_retrieve_params,
    goal_validate_params,
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
from ..types.goal import Goal
from .._base_client import AsyncPaginator, make_request_options
from ..types.goal_request_param import GoalRequestParam
from ..types.goal_clone_response import GoalCloneResponse
from ..types.goal_upsert_response import GoalUpsertResponse
from ..types.goal_archive_response import GoalArchiveResponse
from ..types.goal_validate_response import GoalValidateResponse

__all__ = ["GoalsResource", "AsyncGoalsResource"]


class GoalsResource(SyncAPIResource):
    """
    Goals define event conditions that are tracked and attributed to messaging resources.
    """

    @cached_property
    def with_raw_response(self) -> GoalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return GoalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return GoalsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        goal_key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Retrieve a goal by its key in a given environment.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return self._get(
            path_template("/v1/goals/{goal_key}", goal_key=goal_key),
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
                    goal_retrieve_params.GoalRetrieveParams,
                ),
            ),
            cast_to=Goal,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Goal]:
        """
        Returns a paginated list of goals for the given environment.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/goals",
            page=SyncEntriesCursor[Goal],
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
                        "limit": limit,
                    },
                    goal_list_params.GoalListParams,
                ),
            ),
            model=Goal,
        )

    def archive(
        self,
        goal_key: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalArchiveResponse:
        """Archives a given goal across all environments.

        Refuses if any workflow, guide,
        or broadcast is attached to the goal.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return self._delete(
            path_template("/v1/goals/{goal_key}", goal_key=goal_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, goal_archive_params.GoalArchiveParams),
            ),
            cast_to=GoalArchiveResponse,
        )

    def clone(
        self,
        goal_key: str,
        *,
        environment: str,
        clone: goal_clone_params.Clone,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalCloneResponse:
        """
        Clones a goal into a destination environment.

        Args:
          environment: The environment slug.

          clone: The destination key, name, and environment for the cloned goal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return self._post(
            path_template("/v1/goals/{goal_key}/clone", goal_key=goal_key),
            body=maybe_transform({"clone": clone}, goal_clone_params.GoalCloneParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, goal_clone_params.GoalCloneParams),
            ),
            cast_to=GoalCloneResponse,
        )

    def upsert(
        self,
        goal_key: str,
        *,
        environment: str,
        goal: GoalRequestParam,
        annotate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalUpsertResponse:
        """
        Updates a goal of a given key, or creates a new one if it does not yet exist.
        The goal is published immediately; this endpoint does not accept a commit
        parameter.

        Args:
          environment: The environment slug.

          goal: A goal payload for upsert or validate.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return self._put(
            path_template("/v1/goals/{goal_key}", goal_key=goal_key),
            body=maybe_transform({"goal": goal}, goal_upsert_params.GoalUpsertParams),
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
                    goal_upsert_params.GoalUpsertParams,
                ),
            ),
            cast_to=GoalUpsertResponse,
        )

    def validate(
        self,
        goal_key: str,
        *,
        environment: str,
        goal: GoalRequestParam,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalValidateResponse:
        """
        Validates a goal payload without persisting it.

        Args:
          environment: The environment slug.

          goal: A goal payload for upsert or validate.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return self._put(
            path_template("/v1/goals/{goal_key}/validate", goal_key=goal_key),
            body=maybe_transform({"goal": goal}, goal_validate_params.GoalValidateParams),
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
                    goal_validate_params.GoalValidateParams,
                ),
            ),
            cast_to=GoalValidateResponse,
        )


class AsyncGoalsResource(AsyncAPIResource):
    """
    Goals define event conditions that are tracked and attributed to messaging resources.
    """

    @cached_property
    def with_raw_response(self) -> AsyncGoalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGoalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncGoalsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        goal_key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Goal:
        """
        Retrieve a goal by its key in a given environment.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return await self._get(
            path_template("/v1/goals/{goal_key}", goal_key=goal_key),
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
                    goal_retrieve_params.GoalRetrieveParams,
                ),
            ),
            cast_to=Goal,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Goal, AsyncEntriesCursor[Goal]]:
        """
        Returns a paginated list of goals for the given environment.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/goals",
            page=AsyncEntriesCursor[Goal],
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
                        "limit": limit,
                    },
                    goal_list_params.GoalListParams,
                ),
            ),
            model=Goal,
        )

    async def archive(
        self,
        goal_key: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalArchiveResponse:
        """Archives a given goal across all environments.

        Refuses if any workflow, guide,
        or broadcast is attached to the goal.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return await self._delete(
            path_template("/v1/goals/{goal_key}", goal_key=goal_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"environment": environment}, goal_archive_params.GoalArchiveParams),
            ),
            cast_to=GoalArchiveResponse,
        )

    async def clone(
        self,
        goal_key: str,
        *,
        environment: str,
        clone: goal_clone_params.Clone,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalCloneResponse:
        """
        Clones a goal into a destination environment.

        Args:
          environment: The environment slug.

          clone: The destination key, name, and environment for the cloned goal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return await self._post(
            path_template("/v1/goals/{goal_key}/clone", goal_key=goal_key),
            body=await async_maybe_transform({"clone": clone}, goal_clone_params.GoalCloneParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"environment": environment}, goal_clone_params.GoalCloneParams),
            ),
            cast_to=GoalCloneResponse,
        )

    async def upsert(
        self,
        goal_key: str,
        *,
        environment: str,
        goal: GoalRequestParam,
        annotate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalUpsertResponse:
        """
        Updates a goal of a given key, or creates a new one if it does not yet exist.
        The goal is published immediately; this endpoint does not accept a commit
        parameter.

        Args:
          environment: The environment slug.

          goal: A goal payload for upsert or validate.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return await self._put(
            path_template("/v1/goals/{goal_key}", goal_key=goal_key),
            body=await async_maybe_transform({"goal": goal}, goal_upsert_params.GoalUpsertParams),
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
                    goal_upsert_params.GoalUpsertParams,
                ),
            ),
            cast_to=GoalUpsertResponse,
        )

    async def validate(
        self,
        goal_key: str,
        *,
        environment: str,
        goal: GoalRequestParam,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalValidateResponse:
        """
        Validates a goal payload without persisting it.

        Args:
          environment: The environment slug.

          goal: A goal payload for upsert or validate.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return await self._put(
            path_template("/v1/goals/{goal_key}/validate", goal_key=goal_key),
            body=await async_maybe_transform({"goal": goal}, goal_validate_params.GoalValidateParams),
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
                    goal_validate_params.GoalValidateParams,
                ),
            ),
            cast_to=GoalValidateResponse,
        )


class GoalsResourceWithRawResponse:
    def __init__(self, goals: GoalsResource) -> None:
        self._goals = goals

        self.retrieve = to_raw_response_wrapper(
            goals.retrieve,
        )
        self.list = to_raw_response_wrapper(
            goals.list,
        )
        self.archive = to_raw_response_wrapper(
            goals.archive,
        )
        self.clone = to_raw_response_wrapper(
            goals.clone,
        )
        self.upsert = to_raw_response_wrapper(
            goals.upsert,
        )
        self.validate = to_raw_response_wrapper(
            goals.validate,
        )


class AsyncGoalsResourceWithRawResponse:
    def __init__(self, goals: AsyncGoalsResource) -> None:
        self._goals = goals

        self.retrieve = async_to_raw_response_wrapper(
            goals.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            goals.list,
        )
        self.archive = async_to_raw_response_wrapper(
            goals.archive,
        )
        self.clone = async_to_raw_response_wrapper(
            goals.clone,
        )
        self.upsert = async_to_raw_response_wrapper(
            goals.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            goals.validate,
        )


class GoalsResourceWithStreamingResponse:
    def __init__(self, goals: GoalsResource) -> None:
        self._goals = goals

        self.retrieve = to_streamed_response_wrapper(
            goals.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            goals.list,
        )
        self.archive = to_streamed_response_wrapper(
            goals.archive,
        )
        self.clone = to_streamed_response_wrapper(
            goals.clone,
        )
        self.upsert = to_streamed_response_wrapper(
            goals.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            goals.validate,
        )


class AsyncGoalsResourceWithStreamingResponse:
    def __init__(self, goals: AsyncGoalsResource) -> None:
        self._goals = goals

        self.retrieve = async_to_streamed_response_wrapper(
            goals.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            goals.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            goals.archive,
        )
        self.clone = async_to_streamed_response_wrapper(
            goals.clone,
        )
        self.upsert = async_to_streamed_response_wrapper(
            goals.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            goals.validate,
        )

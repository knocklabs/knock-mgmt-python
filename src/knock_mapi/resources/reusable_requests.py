# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    reusable_request_list_params,
    reusable_request_upsert_params,
    reusable_request_archive_params,
    reusable_request_retrieve_params,
    reusable_request_validate_params,
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
from ..types.reusable_request import ReusableRequest
from ..types.reusable_request_request_param import ReusableRequestRequestParam
from ..types.reusable_request_upsert_response import ReusableRequestUpsertResponse
from ..types.reusable_request_archive_response import ReusableRequestArchiveResponse
from ..types.reusable_request_validate_response import ReusableRequestValidateResponse

__all__ = ["ReusableRequestsResource", "AsyncReusableRequestsResource"]


class ReusableRequestsResource(SyncAPIResource):
    """
    Reusable requests are HTTP steps that workflows can link to and share across an account.
    """

    @cached_property
    def with_raw_response(self) -> ReusableRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return ReusableRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReusableRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return ReusableRequestsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        reusable_request_key: str,
        *,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequest:
        """
        Retrieves a reusable request by its key.

        Args:
          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return self._get(
            path_template("/v1/reusable_requests/{reusable_request_key}", reusable_request_key=reusable_request_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annotate": annotate,
                        "branch": branch,
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    reusable_request_retrieve_params.ReusableRequestRetrieveParams,
                ),
            ),
            cast_to=ReusableRequest,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[ReusableRequest]:
        """
        Returns a paginated list of reusable requests for an environment.

        Args:
          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/reusable_requests",
            page=SyncEntriesCursor[ReusableRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "annotate": annotate,
                        "before": before,
                        "branch": branch,
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    reusable_request_list_params.ReusableRequestListParams,
                ),
            ),
            model=ReusableRequest,
        )

    def archive(
        self,
        reusable_request_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequestArchiveResponse:
        """
        Archives a reusable request by key across all environments.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return self._delete(
            path_template("/v1/reusable_requests/{reusable_request_key}", reusable_request_key=reusable_request_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, reusable_request_archive_params.ReusableRequestArchiveParams
                ),
            ),
            cast_to=ReusableRequestArchiveResponse,
        )

    def upsert(
        self,
        reusable_request_key: str,
        *,
        reusable_request: ReusableRequestRequestParam,
        allow_empty: bool | Omit = omit,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        environment: str | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequestUpsertResponse:
        """
        Updates a reusable request of a given key, or creates a new one if it does not
        yet exist.

        The write targets the environment in the request. Accounts that allow writes in
        every environment can create and update in that environment. Pass force to write
        outside the request's origin environment. When writes are limited to
        development, this endpoint accepts the development environment unless force is
        set.

        Args:
          reusable_request: A reusable request object with attributes to update or create a reusable
              request.

          allow_empty: When used with commit, creates a new version with identical content and commits
              it if there are no unpublished changes.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          environment: The environment slug. When omitted, the account's default environment is used.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return self._put(
            path_template("/v1/reusable_requests/{reusable_request_key}", reusable_request_key=reusable_request_key),
            body=maybe_transform(
                {"reusable_request": reusable_request}, reusable_request_upsert_params.ReusableRequestUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "allow_empty": allow_empty,
                        "annotate": annotate,
                        "branch": branch,
                        "commit": commit,
                        "commit_message": commit_message,
                        "environment": environment,
                        "force": force,
                    },
                    reusable_request_upsert_params.ReusableRequestUpsertParams,
                ),
            ),
            cast_to=ReusableRequestUpsertResponse,
        )

    def validate(
        self,
        reusable_request_key: str,
        *,
        reusable_request: ReusableRequestRequestParam,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequestValidateResponse:
        """
        Validates a reusable request payload without persisting it.

        Validation uses the environment in the request. Accounts that allow writes in
        every environment can validate in that environment. When writes are limited to
        development, this endpoint accepts the development environment.

        Args:
          reusable_request: A reusable request object with attributes to update or create a reusable
              request.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return self._put(
            path_template(
                "/v1/reusable_requests/{reusable_request_key}/validate", reusable_request_key=reusable_request_key
            ),
            body=maybe_transform(
                {"reusable_request": reusable_request}, reusable_request_validate_params.ReusableRequestValidateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "branch": branch,
                        "environment": environment,
                    },
                    reusable_request_validate_params.ReusableRequestValidateParams,
                ),
            ),
            cast_to=ReusableRequestValidateResponse,
        )


class AsyncReusableRequestsResource(AsyncAPIResource):
    """
    Reusable requests are HTTP steps that workflows can link to and share across an account.
    """

    @cached_property
    def with_raw_response(self) -> AsyncReusableRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReusableRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReusableRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncReusableRequestsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        reusable_request_key: str,
        *,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequest:
        """
        Retrieves a reusable request by its key.

        Args:
          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return await self._get(
            path_template("/v1/reusable_requests/{reusable_request_key}", reusable_request_key=reusable_request_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "annotate": annotate,
                        "branch": branch,
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    reusable_request_retrieve_params.ReusableRequestRetrieveParams,
                ),
            ),
            cast_to=ReusableRequest,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReusableRequest, AsyncEntriesCursor[ReusableRequest]]:
        """
        Returns a paginated list of reusable requests for an environment.

        Args:
          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/reusable_requests",
            page=AsyncEntriesCursor[ReusableRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "annotate": annotate,
                        "before": before,
                        "branch": branch,
                        "environment": environment,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    reusable_request_list_params.ReusableRequestListParams,
                ),
            ),
            model=ReusableRequest,
        )

    async def archive(
        self,
        reusable_request_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequestArchiveResponse:
        """
        Archives a reusable request by key across all environments.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return await self._delete(
            path_template("/v1/reusable_requests/{reusable_request_key}", reusable_request_key=reusable_request_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, reusable_request_archive_params.ReusableRequestArchiveParams
                ),
            ),
            cast_to=ReusableRequestArchiveResponse,
        )

    async def upsert(
        self,
        reusable_request_key: str,
        *,
        reusable_request: ReusableRequestRequestParam,
        allow_empty: bool | Omit = omit,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        environment: str | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequestUpsertResponse:
        """
        Updates a reusable request of a given key, or creates a new one if it does not
        yet exist.

        The write targets the environment in the request. Accounts that allow writes in
        every environment can create and update in that environment. Pass force to write
        outside the request's origin environment. When writes are limited to
        development, this endpoint accepts the development environment unless force is
        set.

        Args:
          reusable_request: A reusable request object with attributes to update or create a reusable
              request.

          allow_empty: When used with commit, creates a new version with identical content and commits
              it if there are no unpublished changes.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          environment: The environment slug. When omitted, the account's default environment is used.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return await self._put(
            path_template("/v1/reusable_requests/{reusable_request_key}", reusable_request_key=reusable_request_key),
            body=await async_maybe_transform(
                {"reusable_request": reusable_request}, reusable_request_upsert_params.ReusableRequestUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "allow_empty": allow_empty,
                        "annotate": annotate,
                        "branch": branch,
                        "commit": commit,
                        "commit_message": commit_message,
                        "environment": environment,
                        "force": force,
                    },
                    reusable_request_upsert_params.ReusableRequestUpsertParams,
                ),
            ),
            cast_to=ReusableRequestUpsertResponse,
        )

    async def validate(
        self,
        reusable_request_key: str,
        *,
        reusable_request: ReusableRequestRequestParam,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReusableRequestValidateResponse:
        """
        Validates a reusable request payload without persisting it.

        Validation uses the environment in the request. Accounts that allow writes in
        every environment can validate in that environment. When writes are limited to
        development, this endpoint accepts the development environment.

        Args:
          reusable_request: A reusable request object with attributes to update or create a reusable
              request.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reusable_request_key:
            raise ValueError(
                f"Expected a non-empty value for `reusable_request_key` but received {reusable_request_key!r}"
            )
        return await self._put(
            path_template(
                "/v1/reusable_requests/{reusable_request_key}/validate", reusable_request_key=reusable_request_key
            ),
            body=await async_maybe_transform(
                {"reusable_request": reusable_request}, reusable_request_validate_params.ReusableRequestValidateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "branch": branch,
                        "environment": environment,
                    },
                    reusable_request_validate_params.ReusableRequestValidateParams,
                ),
            ),
            cast_to=ReusableRequestValidateResponse,
        )


class ReusableRequestsResourceWithRawResponse:
    def __init__(self, reusable_requests: ReusableRequestsResource) -> None:
        self._reusable_requests = reusable_requests

        self.retrieve = to_raw_response_wrapper(
            reusable_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            reusable_requests.list,
        )
        self.archive = to_raw_response_wrapper(
            reusable_requests.archive,
        )
        self.upsert = to_raw_response_wrapper(
            reusable_requests.upsert,
        )
        self.validate = to_raw_response_wrapper(
            reusable_requests.validate,
        )


class AsyncReusableRequestsResourceWithRawResponse:
    def __init__(self, reusable_requests: AsyncReusableRequestsResource) -> None:
        self._reusable_requests = reusable_requests

        self.retrieve = async_to_raw_response_wrapper(
            reusable_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            reusable_requests.list,
        )
        self.archive = async_to_raw_response_wrapper(
            reusable_requests.archive,
        )
        self.upsert = async_to_raw_response_wrapper(
            reusable_requests.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            reusable_requests.validate,
        )


class ReusableRequestsResourceWithStreamingResponse:
    def __init__(self, reusable_requests: ReusableRequestsResource) -> None:
        self._reusable_requests = reusable_requests

        self.retrieve = to_streamed_response_wrapper(
            reusable_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            reusable_requests.list,
        )
        self.archive = to_streamed_response_wrapper(
            reusable_requests.archive,
        )
        self.upsert = to_streamed_response_wrapper(
            reusable_requests.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            reusable_requests.validate,
        )


class AsyncReusableRequestsResourceWithStreamingResponse:
    def __init__(self, reusable_requests: AsyncReusableRequestsResource) -> None:
        self._reusable_requests = reusable_requests

        self.retrieve = async_to_streamed_response_wrapper(
            reusable_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            reusable_requests.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            reusable_requests.archive,
        )
        self.upsert = async_to_streamed_response_wrapper(
            reusable_requests.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            reusable_requests.validate,
        )

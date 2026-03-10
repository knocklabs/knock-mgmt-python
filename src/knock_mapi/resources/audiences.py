# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..types import (
    audience_list_params,
    audience_upsert_params,
    audience_archive_params,
    audience_retrieve_params,
    audience_validate_params,
)
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
from ..pagination import SyncEntriesCursor, AsyncEntriesCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.audience import Audience
from ..types.audience_upsert_response import AudienceUpsertResponse
from ..types.audience_archive_response import AudienceArchiveResponse
from ..types.audience_validate_response import AudienceValidateResponse

__all__ = ["AudiencesResource", "AsyncAudiencesResource"]


class AudiencesResource(SyncAPIResource):
    """Audiences define sets of users that can be targeted for notifications."""

    @cached_property
    def with_raw_response(self) -> AudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AudiencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        audience_key: str,
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
    ) -> Audience:
        """
        Retrieve an audience by its key in a given environment.

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
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return cast(
            Audience,
            self._get(
                f"/v1/audiences/{audience_key}",
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
                        audience_retrieve_params.AudienceRetrieveParams,
                    ),
                ),
                cast_to=cast(Any, Audience),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SyncEntriesCursor[Audience]:
        """
        Returns a paginated list of audiences for the given environment.

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
            "/v1/audiences",
            page=SyncEntriesCursor[Audience],
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
                    audience_list_params.AudienceListParams,
                ),
            ),
            model=cast(Any, Audience),  # Union types cannot be passed in as arguments in the type system
        )

    def archive(
        self,
        audience_key: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceArchiveResponse:
        """
        Archives a given audience across all environments.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return self._delete(
            f"/v1/audiences/{audience_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, audience_archive_params.AudienceArchiveParams),
            ),
            cast_to=AudienceArchiveResponse,
        )

    def upsert(
        self,
        audience_key: str,
        *,
        environment: str,
        audience: audience_upsert_params.Audience,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceUpsertResponse:
        """
        Updates an audience of a given key, or creates a new one if it does not yet
        exist.

        Args:
          environment: The environment slug.

          audience: An audience object with attributes to create or update an audience. Use
              `type: static` for audiences with explicitly managed members, or `type: dynamic`
              for audiences with segment-based membership.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return self._put(
            f"/v1/audiences/{audience_key}",
            body=maybe_transform({"audience": audience}, audience_upsert_params.AudienceUpsertParams),
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
                        "commit": commit,
                        "commit_message": commit_message,
                    },
                    audience_upsert_params.AudienceUpsertParams,
                ),
            ),
            cast_to=AudienceUpsertResponse,
        )

    def validate(
        self,
        audience_key: str,
        *,
        environment: str,
        audience: audience_validate_params.Audience,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceValidateResponse:
        """
        Validates an audience payload without persisting it.

        Args:
          environment: The environment slug.

          audience: An audience object with attributes to create or update an audience. Use
              `type: static` for audiences with explicitly managed members, or `type: dynamic`
              for audiences with segment-based membership.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return self._put(
            f"/v1/audiences/{audience_key}/validate",
            body=maybe_transform({"audience": audience}, audience_validate_params.AudienceValidateParams),
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
                    audience_validate_params.AudienceValidateParams,
                ),
            ),
            cast_to=AudienceValidateResponse,
        )


class AsyncAudiencesResource(AsyncAPIResource):
    """Audiences define sets of users that can be targeted for notifications."""

    @cached_property
    def with_raw_response(self) -> AsyncAudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncAudiencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        audience_key: str,
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
    ) -> Audience:
        """
        Retrieve an audience by its key in a given environment.

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
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return cast(
            Audience,
            await self._get(
                f"/v1/audiences/{audience_key}",
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
                        audience_retrieve_params.AudienceRetrieveParams,
                    ),
                ),
                cast_to=cast(Any, Audience),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AsyncPaginator[Audience, AsyncEntriesCursor[Audience]]:
        """
        Returns a paginated list of audiences for the given environment.

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
            "/v1/audiences",
            page=AsyncEntriesCursor[Audience],
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
                    audience_list_params.AudienceListParams,
                ),
            ),
            model=cast(Any, Audience),  # Union types cannot be passed in as arguments in the type system
        )

    async def archive(
        self,
        audience_key: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceArchiveResponse:
        """
        Archives a given audience across all environments.

        Args:
          environment: The environment slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return await self._delete(
            f"/v1/audiences/{audience_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, audience_archive_params.AudienceArchiveParams
                ),
            ),
            cast_to=AudienceArchiveResponse,
        )

    async def upsert(
        self,
        audience_key: str,
        *,
        environment: str,
        audience: audience_upsert_params.Audience,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceUpsertResponse:
        """
        Updates an audience of a given key, or creates a new one if it does not yet
        exist.

        Args:
          environment: The environment slug.

          audience: An audience object with attributes to create or update an audience. Use
              `type: static` for audiences with explicitly managed members, or `type: dynamic`
              for audiences with segment-based membership.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return await self._put(
            f"/v1/audiences/{audience_key}",
            body=await async_maybe_transform({"audience": audience}, audience_upsert_params.AudienceUpsertParams),
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
                        "commit": commit,
                        "commit_message": commit_message,
                    },
                    audience_upsert_params.AudienceUpsertParams,
                ),
            ),
            cast_to=AudienceUpsertResponse,
        )

    async def validate(
        self,
        audience_key: str,
        *,
        environment: str,
        audience: audience_validate_params.Audience,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceValidateResponse:
        """
        Validates an audience payload without persisting it.

        Args:
          environment: The environment slug.

          audience: An audience object with attributes to create or update an audience. Use
              `type: static` for audiences with explicitly managed members, or `type: dynamic`
              for audiences with segment-based membership.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_key:
            raise ValueError(f"Expected a non-empty value for `audience_key` but received {audience_key!r}")
        return await self._put(
            f"/v1/audiences/{audience_key}/validate",
            body=await async_maybe_transform({"audience": audience}, audience_validate_params.AudienceValidateParams),
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
                    audience_validate_params.AudienceValidateParams,
                ),
            ),
            cast_to=AudienceValidateResponse,
        )


class AudiencesResourceWithRawResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = to_raw_response_wrapper(
            audiences.retrieve,
        )
        self.list = to_raw_response_wrapper(
            audiences.list,
        )
        self.archive = to_raw_response_wrapper(
            audiences.archive,
        )
        self.upsert = to_raw_response_wrapper(
            audiences.upsert,
        )
        self.validate = to_raw_response_wrapper(
            audiences.validate,
        )


class AsyncAudiencesResourceWithRawResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = async_to_raw_response_wrapper(
            audiences.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            audiences.list,
        )
        self.archive = async_to_raw_response_wrapper(
            audiences.archive,
        )
        self.upsert = async_to_raw_response_wrapper(
            audiences.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            audiences.validate,
        )


class AudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = to_streamed_response_wrapper(
            audiences.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            audiences.list,
        )
        self.archive = to_streamed_response_wrapper(
            audiences.archive,
        )
        self.upsert = to_streamed_response_wrapper(
            audiences.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            audiences.validate,
        )


class AsyncAudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = async_to_streamed_response_wrapper(
            audiences.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            audiences.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            audiences.archive,
        )
        self.upsert = async_to_streamed_response_wrapper(
            audiences.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            audiences.validate,
        )

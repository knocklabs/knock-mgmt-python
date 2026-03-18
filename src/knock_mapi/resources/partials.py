# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import partial_list_params, partial_upsert_params, partial_retrieve_params, partial_validate_params
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
from ..types.partial import Partial
from ..types.partial_upsert_response import PartialUpsertResponse
from ..types.partial_validate_response import PartialValidateResponse

__all__ = ["PartialsResource", "AsyncPartialsResource"]


class PartialsResource(SyncAPIResource):
    """Partials allow you to reuse content across templates."""

    @cached_property
    def with_raw_response(self) -> PartialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return PartialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return PartialsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        partial_key: str,
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
    ) -> Partial:
        """
        Get a partial by its key.

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
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return self._get(
            f"/v1/partials/{partial_key}",
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
                    partial_retrieve_params.PartialRetrieveParams,
                ),
            ),
            cast_to=Partial,
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
    ) -> SyncEntriesCursor[Partial]:
        """
        List all partials for a given environment.

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
            "/v1/partials",
            page=SyncEntriesCursor[Partial],
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
                    partial_list_params.PartialListParams,
                ),
            ),
            model=Partial,
        )

    def upsert(
        self,
        partial_key: str,
        *,
        environment: str,
        partial: partial_upsert_params.Partial,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartialUpsertResponse:
        """
        Updates a partial of a given key, or creates a new one if it does not yet exist.

        Note: this endpoint only operates on partials in the “development” environment.

        Args:
          environment: The environment slug.

          partial: A partial object with attributes to update or create a partial.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return self._put(
            f"/v1/partials/{partial_key}",
            body=maybe_transform({"partial": partial}, partial_upsert_params.PartialUpsertParams),
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
                        "force": force,
                    },
                    partial_upsert_params.PartialUpsertParams,
                ),
            ),
            cast_to=PartialUpsertResponse,
        )

    def validate(
        self,
        partial_key: str,
        *,
        environment: str,
        partial: partial_validate_params.Partial,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartialValidateResponse:
        """
        Validates a partial payload without persisting it.

        Note: this endpoint only operates on partials in the “development” environment.

        Args:
          environment: The environment slug.

          partial: A partial object with attributes to update or create a partial.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return self._put(
            f"/v1/partials/{partial_key}/validate",
            body=maybe_transform({"partial": partial}, partial_validate_params.PartialValidateParams),
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
                    partial_validate_params.PartialValidateParams,
                ),
            ),
            cast_to=PartialValidateResponse,
        )


class AsyncPartialsResource(AsyncAPIResource):
    """Partials allow you to reuse content across templates."""

    @cached_property
    def with_raw_response(self) -> AsyncPartialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPartialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncPartialsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        partial_key: str,
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
    ) -> Partial:
        """
        Get a partial by its key.

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
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return await self._get(
            f"/v1/partials/{partial_key}",
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
                    partial_retrieve_params.PartialRetrieveParams,
                ),
            ),
            cast_to=Partial,
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
    ) -> AsyncPaginator[Partial, AsyncEntriesCursor[Partial]]:
        """
        List all partials for a given environment.

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
            "/v1/partials",
            page=AsyncEntriesCursor[Partial],
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
                    partial_list_params.PartialListParams,
                ),
            ),
            model=Partial,
        )

    async def upsert(
        self,
        partial_key: str,
        *,
        environment: str,
        partial: partial_upsert_params.Partial,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartialUpsertResponse:
        """
        Updates a partial of a given key, or creates a new one if it does not yet exist.

        Note: this endpoint only operates on partials in the “development” environment.

        Args:
          environment: The environment slug.

          partial: A partial object with attributes to update or create a partial.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return await self._put(
            f"/v1/partials/{partial_key}",
            body=await async_maybe_transform({"partial": partial}, partial_upsert_params.PartialUpsertParams),
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
                        "force": force,
                    },
                    partial_upsert_params.PartialUpsertParams,
                ),
            ),
            cast_to=PartialUpsertResponse,
        )

    async def validate(
        self,
        partial_key: str,
        *,
        environment: str,
        partial: partial_validate_params.Partial,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartialValidateResponse:
        """
        Validates a partial payload without persisting it.

        Note: this endpoint only operates on partials in the “development” environment.

        Args:
          environment: The environment slug.

          partial: A partial object with attributes to update or create a partial.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return await self._put(
            f"/v1/partials/{partial_key}/validate",
            body=await async_maybe_transform({"partial": partial}, partial_validate_params.PartialValidateParams),
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
                    partial_validate_params.PartialValidateParams,
                ),
            ),
            cast_to=PartialValidateResponse,
        )


class PartialsResourceWithRawResponse:
    def __init__(self, partials: PartialsResource) -> None:
        self._partials = partials

        self.retrieve = to_raw_response_wrapper(
            partials.retrieve,
        )
        self.list = to_raw_response_wrapper(
            partials.list,
        )
        self.upsert = to_raw_response_wrapper(
            partials.upsert,
        )
        self.validate = to_raw_response_wrapper(
            partials.validate,
        )


class AsyncPartialsResourceWithRawResponse:
    def __init__(self, partials: AsyncPartialsResource) -> None:
        self._partials = partials

        self.retrieve = async_to_raw_response_wrapper(
            partials.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            partials.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            partials.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            partials.validate,
        )


class PartialsResourceWithStreamingResponse:
    def __init__(self, partials: PartialsResource) -> None:
        self._partials = partials

        self.retrieve = to_streamed_response_wrapper(
            partials.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            partials.list,
        )
        self.upsert = to_streamed_response_wrapper(
            partials.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            partials.validate,
        )


class AsyncPartialsResourceWithStreamingResponse:
    def __init__(self, partials: AsyncPartialsResource) -> None:
        self._partials = partials

        self.retrieve = async_to_streamed_response_wrapper(
            partials.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            partials.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            partials.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            partials.validate,
        )

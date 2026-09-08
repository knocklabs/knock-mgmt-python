# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import (
    partial_list_params,
    partial_upsert_params,
    partial_preview_params,
    partial_retrieve_params,
    partial_validate_params,
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
from ..types.partial import Partial
from ..types.partial_request_param import PartialRequestParam
from ..types.partial_upsert_response import PartialUpsertResponse
from ..types.partial_preview_response import PartialPreviewResponse
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
    ) -> Partial:
        """Get a partial by its key.

        Args:
          annotate: Whether to annotate the resource.

        Only used in the Knock CLI.

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
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return self._get(
            path_template("/v1/partials/{partial_key}", partial_key=partial_key),
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
                    partial_retrieve_params.PartialRetrieveParams,
                ),
            ),
            cast_to=Partial,
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
    ) -> SyncEntriesCursor[Partial]:
        """
        List all partials for a given environment.

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
            "/v1/partials",
            page=SyncEntriesCursor[Partial],
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
                    partial_list_params.PartialListParams,
                ),
            ),
            model=Partial,
        )

    def preview(
        self,
        *,
        partial: PartialRequestParam,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        layout: Optional[partial_preview_params.Layout] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartialPreviewResponse:
        """
        Renders a partial in isolation, without requiring the partial to be persisted in
        Knock.

        Useful for iterating on a partial locally and seeing how it renders against
        sample data.

        Args:
          partial: A partial object with attributes to update or create a partial.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          data: The data to pass to the partial when rendering. Top-level keys are exposed as
              variables in the partial template.

          layout: Email layout configuration. Only applicable for `html` partials. When omitted,
              the rendered partial is returned unwrapped.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/partials/preview",
            body=maybe_transform(
                {
                    "partial": partial,
                    "data": data,
                    "layout": layout,
                },
                partial_preview_params.PartialPreviewParams,
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
                    partial_preview_params.PartialPreviewParams,
                ),
            ),
            cast_to=PartialPreviewResponse,
        )

    def upsert(
        self,
        partial_key: str,
        *,
        partial: PartialRequestParam,
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
    ) -> PartialUpsertResponse:
        """
        Updates a partial of a given key, or creates a new one if it does not yet exist.

        Note: this endpoint only operates on partials in the “development” environment.

        Args:
          partial: A partial object with attributes to update or create a partial.

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
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return self._put(
            path_template("/v1/partials/{partial_key}", partial_key=partial_key),
            body=maybe_transform({"partial": partial}, partial_upsert_params.PartialUpsertParams),
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
                    partial_upsert_params.PartialUpsertParams,
                ),
            ),
            cast_to=PartialUpsertResponse,
        )

    def validate(
        self,
        partial_key: str,
        *,
        partial: PartialRequestParam,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
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
          partial: A partial object with attributes to update or create a partial.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return self._put(
            path_template("/v1/partials/{partial_key}/validate", partial_key=partial_key),
            body=maybe_transform({"partial": partial}, partial_validate_params.PartialValidateParams),
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
    ) -> Partial:
        """Get a partial by its key.

        Args:
          annotate: Whether to annotate the resource.

        Only used in the Knock CLI.

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
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return await self._get(
            path_template("/v1/partials/{partial_key}", partial_key=partial_key),
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
                    partial_retrieve_params.PartialRetrieveParams,
                ),
            ),
            cast_to=Partial,
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
    ) -> AsyncPaginator[Partial, AsyncEntriesCursor[Partial]]:
        """
        List all partials for a given environment.

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
            "/v1/partials",
            page=AsyncEntriesCursor[Partial],
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
                    partial_list_params.PartialListParams,
                ),
            ),
            model=Partial,
        )

    async def preview(
        self,
        *,
        partial: PartialRequestParam,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        layout: Optional[partial_preview_params.Layout] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartialPreviewResponse:
        """
        Renders a partial in isolation, without requiring the partial to be persisted in
        Knock.

        Useful for iterating on a partial locally and seeing how it renders against
        sample data.

        Args:
          partial: A partial object with attributes to update or create a partial.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          data: The data to pass to the partial when rendering. Top-level keys are exposed as
              variables in the partial template.

          layout: Email layout configuration. Only applicable for `html` partials. When omitted,
              the rendered partial is returned unwrapped.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/partials/preview",
            body=await async_maybe_transform(
                {
                    "partial": partial,
                    "data": data,
                    "layout": layout,
                },
                partial_preview_params.PartialPreviewParams,
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
                    partial_preview_params.PartialPreviewParams,
                ),
            ),
            cast_to=PartialPreviewResponse,
        )

    async def upsert(
        self,
        partial_key: str,
        *,
        partial: PartialRequestParam,
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
    ) -> PartialUpsertResponse:
        """
        Updates a partial of a given key, or creates a new one if it does not yet exist.

        Note: this endpoint only operates on partials in the “development” environment.

        Args:
          partial: A partial object with attributes to update or create a partial.

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
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return await self._put(
            path_template("/v1/partials/{partial_key}", partial_key=partial_key),
            body=await async_maybe_transform({"partial": partial}, partial_upsert_params.PartialUpsertParams),
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
                    partial_upsert_params.PartialUpsertParams,
                ),
            ),
            cast_to=PartialUpsertResponse,
        )

    async def validate(
        self,
        partial_key: str,
        *,
        partial: PartialRequestParam,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
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
          partial: A partial object with attributes to update or create a partial.

          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partial_key:
            raise ValueError(f"Expected a non-empty value for `partial_key` but received {partial_key!r}")
        return await self._put(
            path_template("/v1/partials/{partial_key}/validate", partial_key=partial_key),
            body=await async_maybe_transform({"partial": partial}, partial_validate_params.PartialValidateParams),
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
        self.preview = to_raw_response_wrapper(
            partials.preview,
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
        self.preview = async_to_raw_response_wrapper(
            partials.preview,
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
        self.preview = to_streamed_response_wrapper(
            partials.preview,
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
        self.preview = async_to_streamed_response_wrapper(
            partials.preview,
        )
        self.upsert = async_to_streamed_response_wrapper(
            partials.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            partials.validate,
        )

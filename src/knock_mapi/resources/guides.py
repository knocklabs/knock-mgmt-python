# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import overload

import httpx

from ..types import (
    guide_list_params,
    guide_upsert_params,
    guide_activate_params,
    guide_retrieve_params,
    guide_validate_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncEntriesCursor, AsyncEntriesCursor
from ..types.guide import Guide
from .._base_client import AsyncPaginator, make_request_options
from ..types.guide_upsert_response import GuideUpsertResponse
from ..types.guide_activate_response import GuideActivateResponse
from ..types.guide_validate_response import GuideValidateResponse

__all__ = ["GuidesResource", "AsyncGuidesResource"]


class GuidesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GuidesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return GuidesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuidesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return GuidesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        guide_key: str,
        *,
        environment: str,
        annotate: bool | NotGiven = NOT_GIVEN,
        hide_uncommitted_changes: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Guide:
        """
        Get a guide by its key.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return self._get(
            f"/v1/guides/{guide_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    guide_retrieve_params.GuideRetrieveParams,
                ),
            ),
            cast_to=Guide,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | NotGiven = NOT_GIVEN,
        annotate: bool | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        hide_uncommitted_changes: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Guide]:
        """
        Returns a paginated list of guides available in a given environment.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/guides",
            page=SyncEntriesCursor[Guide],
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
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    guide_list_params.GuideListParams,
                ),
            ),
            model=Guide,
        )

    @overload
    def activate(
        self,
        guide_key: str,
        *,
        environment: str,
        status: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideActivateResponse:
        """Activates (or deactivates) a guide in a given environment.

        You can either set
        the active status immediately or schedule it.

        Note: This immediately enables or disables a guide in a given environment
        without needing to go through environment promotion.

        Args:
          environment: The environment slug.

          status: Whether to activate or deactivate the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def activate(
        self,
        guide_key: str,
        *,
        environment: str,
        from_: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideActivateResponse:
        """Activates (or deactivates) a guide in a given environment.

        You can either set
        the active status immediately or schedule it.

        Note: This immediately enables or disables a guide in a given environment
        without needing to go through environment promotion.

        Args:
          environment: The environment slug.

          from_: When to activate the guide. If provided, the guide will be scheduled to activate
              at this time. Must be in ISO 8601 UTC format.

          until: When to deactivate the guide. If provided, the guide will be scheduled to
              deactivate at this time. Must be in ISO 8601 UTC format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["environment", "status"], ["environment"])
    def activate(
        self,
        guide_key: str,
        *,
        environment: str,
        status: bool | NotGiven = NOT_GIVEN,
        from_: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideActivateResponse:
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return self._put(
            f"/v1/guides/{guide_key}/activate",
            body=maybe_transform(
                {
                    "status": status,
                    "from_": from_,
                    "until": until,
                },
                guide_activate_params.GuideActivateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, guide_activate_params.GuideActivateParams),
            ),
            cast_to=GuideActivateResponse,
        )

    def upsert(
        self,
        guide_key: str,
        *,
        environment: str,
        guide: guide_upsert_params.Guide,
        annotate: bool | NotGiven = NOT_GIVEN,
        commit: bool | NotGiven = NOT_GIVEN,
        commit_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideUpsertResponse:
        """
        Updates a guide of a given key, or creates a new one if it does not yet exist.

        Note: this endpoint only operates on guides in the "development" environment.

        Args:
          environment: The environment slug.

          guide: A request to create or update a guide.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return self._put(
            f"/v1/guides/{guide_key}",
            body=maybe_transform({"guide": guide}, guide_upsert_params.GuideUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "commit": commit,
                        "commit_message": commit_message,
                    },
                    guide_upsert_params.GuideUpsertParams,
                ),
            ),
            cast_to=GuideUpsertResponse,
        )

    def validate(
        self,
        guide_key: str,
        *,
        environment: str,
        guide: guide_validate_params.Guide,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideValidateResponse:
        """
        Validates a guide payload without persisting it.

        Note: Validating a guide is only done in the development environment context.

        Args:
          environment: The environment slug.

          guide: A request to create or update a guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return self._put(
            f"/v1/guides/{guide_key}/validate",
            body=maybe_transform({"guide": guide}, guide_validate_params.GuideValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, guide_validate_params.GuideValidateParams),
            ),
            cast_to=GuideValidateResponse,
        )


class AsyncGuidesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGuidesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGuidesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuidesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncGuidesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        guide_key: str,
        *,
        environment: str,
        annotate: bool | NotGiven = NOT_GIVEN,
        hide_uncommitted_changes: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Guide:
        """
        Get a guide by its key.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return await self._get(
            f"/v1/guides/{guide_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                    },
                    guide_retrieve_params.GuideRetrieveParams,
                ),
            ),
            cast_to=Guide,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | NotGiven = NOT_GIVEN,
        annotate: bool | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        hide_uncommitted_changes: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Guide, AsyncEntriesCursor[Guide]]:
        """
        Returns a paginated list of guides available in a given environment.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/guides",
            page=AsyncEntriesCursor[Guide],
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
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                    },
                    guide_list_params.GuideListParams,
                ),
            ),
            model=Guide,
        )

    @overload
    async def activate(
        self,
        guide_key: str,
        *,
        environment: str,
        status: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideActivateResponse:
        """Activates (or deactivates) a guide in a given environment.

        You can either set
        the active status immediately or schedule it.

        Note: This immediately enables or disables a guide in a given environment
        without needing to go through environment promotion.

        Args:
          environment: The environment slug.

          status: Whether to activate or deactivate the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def activate(
        self,
        guide_key: str,
        *,
        environment: str,
        from_: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideActivateResponse:
        """Activates (or deactivates) a guide in a given environment.

        You can either set
        the active status immediately or schedule it.

        Note: This immediately enables or disables a guide in a given environment
        without needing to go through environment promotion.

        Args:
          environment: The environment slug.

          from_: When to activate the guide. If provided, the guide will be scheduled to activate
              at this time. Must be in ISO 8601 UTC format.

          until: When to deactivate the guide. If provided, the guide will be scheduled to
              deactivate at this time. Must be in ISO 8601 UTC format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["environment", "status"], ["environment"])
    async def activate(
        self,
        guide_key: str,
        *,
        environment: str,
        status: bool | NotGiven = NOT_GIVEN,
        from_: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideActivateResponse:
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return await self._put(
            f"/v1/guides/{guide_key}/activate",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "from_": from_,
                    "until": until,
                },
                guide_activate_params.GuideActivateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, guide_activate_params.GuideActivateParams
                ),
            ),
            cast_to=GuideActivateResponse,
        )

    async def upsert(
        self,
        guide_key: str,
        *,
        environment: str,
        guide: guide_upsert_params.Guide,
        annotate: bool | NotGiven = NOT_GIVEN,
        commit: bool | NotGiven = NOT_GIVEN,
        commit_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideUpsertResponse:
        """
        Updates a guide of a given key, or creates a new one if it does not yet exist.

        Note: this endpoint only operates on guides in the "development" environment.

        Args:
          environment: The environment slug.

          guide: A request to create or update a guide.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return await self._put(
            f"/v1/guides/{guide_key}",
            body=await async_maybe_transform({"guide": guide}, guide_upsert_params.GuideUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "annotate": annotate,
                        "commit": commit,
                        "commit_message": commit_message,
                    },
                    guide_upsert_params.GuideUpsertParams,
                ),
            ),
            cast_to=GuideUpsertResponse,
        )

    async def validate(
        self,
        guide_key: str,
        *,
        environment: str,
        guide: guide_validate_params.Guide,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideValidateResponse:
        """
        Validates a guide payload without persisting it.

        Note: Validating a guide is only done in the development environment context.

        Args:
          environment: The environment slug.

          guide: A request to create or update a guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guide_key:
            raise ValueError(f"Expected a non-empty value for `guide_key` but received {guide_key!r}")
        return await self._put(
            f"/v1/guides/{guide_key}/validate",
            body=await async_maybe_transform({"guide": guide}, guide_validate_params.GuideValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, guide_validate_params.GuideValidateParams
                ),
            ),
            cast_to=GuideValidateResponse,
        )


class GuidesResourceWithRawResponse:
    def __init__(self, guides: GuidesResource) -> None:
        self._guides = guides

        self.retrieve = to_raw_response_wrapper(
            guides.retrieve,
        )
        self.list = to_raw_response_wrapper(
            guides.list,
        )
        self.activate = to_raw_response_wrapper(
            guides.activate,
        )
        self.upsert = to_raw_response_wrapper(
            guides.upsert,
        )
        self.validate = to_raw_response_wrapper(
            guides.validate,
        )


class AsyncGuidesResourceWithRawResponse:
    def __init__(self, guides: AsyncGuidesResource) -> None:
        self._guides = guides

        self.retrieve = async_to_raw_response_wrapper(
            guides.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            guides.list,
        )
        self.activate = async_to_raw_response_wrapper(
            guides.activate,
        )
        self.upsert = async_to_raw_response_wrapper(
            guides.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            guides.validate,
        )


class GuidesResourceWithStreamingResponse:
    def __init__(self, guides: GuidesResource) -> None:
        self._guides = guides

        self.retrieve = to_streamed_response_wrapper(
            guides.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            guides.list,
        )
        self.activate = to_streamed_response_wrapper(
            guides.activate,
        )
        self.upsert = to_streamed_response_wrapper(
            guides.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            guides.validate,
        )


class AsyncGuidesResourceWithStreamingResponse:
    def __init__(self, guides: AsyncGuidesResource) -> None:
        self._guides = guides

        self.retrieve = async_to_streamed_response_wrapper(
            guides.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            guides.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            guides.activate,
        )
        self.upsert = async_to_streamed_response_wrapper(
            guides.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            guides.validate,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.preference_category_list_response import PreferenceCategoryListResponse
from ..types.preference_category_upsert_response import PreferenceCategoryUpsertResponse

__all__ = ["PreferenceCategoriesResource", "AsyncPreferenceCategoriesResource"]


class PreferenceCategoriesResource(SyncAPIResource):
    """
    Preference categories are a project-level catalog of categories that can be applied to workflows and broadcasts.
    """

    @cached_property
    def with_raw_response(self) -> PreferenceCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return PreferenceCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferenceCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return PreferenceCategoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCategoryListResponse:
        """
        Returns all preference categories in the project's catalog, ordered by name.
        Preference categories are project-scoped and not tied to an environment.
        """
        return self._get(
            "/v1/preference_categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCategoryListResponse,
        )

    def delete(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archives a preference category by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/preference_categories/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upsert(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCategoryUpsertResponse:
        """Creates a preference category by name.

        If a non-archived category with the same
        name already exists, returns the existing category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._put(
            path_template("/v1/preference_categories/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCategoryUpsertResponse,
        )


class AsyncPreferenceCategoriesResource(AsyncAPIResource):
    """
    Preference categories are a project-level catalog of categories that can be applied to workflows and broadcasts.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPreferenceCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferenceCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferenceCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncPreferenceCategoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCategoryListResponse:
        """
        Returns all preference categories in the project's catalog, ordered by name.
        Preference categories are project-scoped and not tied to an environment.
        """
        return await self._get(
            "/v1/preference_categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCategoryListResponse,
        )

    async def delete(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archives a preference category by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/preference_categories/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upsert(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCategoryUpsertResponse:
        """Creates a preference category by name.

        If a non-archived category with the same
        name already exists, returns the existing category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._put(
            path_template("/v1/preference_categories/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCategoryUpsertResponse,
        )


class PreferenceCategoriesResourceWithRawResponse:
    def __init__(self, preference_categories: PreferenceCategoriesResource) -> None:
        self._preference_categories = preference_categories

        self.list = to_raw_response_wrapper(
            preference_categories.list,
        )
        self.delete = to_raw_response_wrapper(
            preference_categories.delete,
        )
        self.upsert = to_raw_response_wrapper(
            preference_categories.upsert,
        )


class AsyncPreferenceCategoriesResourceWithRawResponse:
    def __init__(self, preference_categories: AsyncPreferenceCategoriesResource) -> None:
        self._preference_categories = preference_categories

        self.list = async_to_raw_response_wrapper(
            preference_categories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            preference_categories.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            preference_categories.upsert,
        )


class PreferenceCategoriesResourceWithStreamingResponse:
    def __init__(self, preference_categories: PreferenceCategoriesResource) -> None:
        self._preference_categories = preference_categories

        self.list = to_streamed_response_wrapper(
            preference_categories.list,
        )
        self.delete = to_streamed_response_wrapper(
            preference_categories.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            preference_categories.upsert,
        )


class AsyncPreferenceCategoriesResourceWithStreamingResponse:
    def __init__(self, preference_categories: AsyncPreferenceCategoriesResource) -> None:
        self._preference_categories = preference_categories

        self.list = async_to_streamed_response_wrapper(
            preference_categories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            preference_categories.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            preference_categories.upsert,
        )

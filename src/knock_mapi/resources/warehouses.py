# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import warehouse_list_params, warehouse_retrieve_params
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
from ..types.warehouse import Warehouse

__all__ = ["WarehousesResource", "AsyncWarehousesResource"]


class WarehousesResource(SyncAPIResource):
    """Warehouses are the databases in your data warehouse that Knock reads from."""

    @cached_property
    def with_raw_response(self) -> WarehousesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return WarehousesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WarehousesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return WarehousesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        warehouse_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Warehouse:
        """Retrieve a warehouse by its key.

        Args:
          environment: The environment slug.

        When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_key` but received {warehouse_key!r}")
        return self._get(
            path_template("/v1/warehouses/{warehouse_key}", warehouse_key=warehouse_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, warehouse_retrieve_params.WarehouseRetrieveParams),
            ),
            cast_to=Warehouse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        environment: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Warehouse]:
        """Returns a paginated list of the project's warehouses.

        Warehouses are shared by
        every environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          environment: The environment slug. When omitted, the account's default environment is used.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/warehouses",
            page=SyncEntriesCursor[Warehouse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "environment": environment,
                        "limit": limit,
                    },
                    warehouse_list_params.WarehouseListParams,
                ),
            ),
            model=Warehouse,
        )


class AsyncWarehousesResource(AsyncAPIResource):
    """Warehouses are the databases in your data warehouse that Knock reads from."""

    @cached_property
    def with_raw_response(self) -> AsyncWarehousesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWarehousesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWarehousesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncWarehousesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        warehouse_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Warehouse:
        """Retrieve a warehouse by its key.

        Args:
          environment: The environment slug.

        When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not warehouse_key:
            raise ValueError(f"Expected a non-empty value for `warehouse_key` but received {warehouse_key!r}")
        return await self._get(
            path_template("/v1/warehouses/{warehouse_key}", warehouse_key=warehouse_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, warehouse_retrieve_params.WarehouseRetrieveParams
                ),
            ),
            cast_to=Warehouse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        environment: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Warehouse, AsyncEntriesCursor[Warehouse]]:
        """Returns a paginated list of the project's warehouses.

        Warehouses are shared by
        every environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          environment: The environment slug. When omitted, the account's default environment is used.

          limit: The number of entries to fetch per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/warehouses",
            page=AsyncEntriesCursor[Warehouse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "environment": environment,
                        "limit": limit,
                    },
                    warehouse_list_params.WarehouseListParams,
                ),
            ),
            model=Warehouse,
        )


class WarehousesResourceWithRawResponse:
    def __init__(self, warehouses: WarehousesResource) -> None:
        self._warehouses = warehouses

        self.retrieve = to_raw_response_wrapper(
            warehouses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            warehouses.list,
        )


class AsyncWarehousesResourceWithRawResponse:
    def __init__(self, warehouses: AsyncWarehousesResource) -> None:
        self._warehouses = warehouses

        self.retrieve = async_to_raw_response_wrapper(
            warehouses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            warehouses.list,
        )


class WarehousesResourceWithStreamingResponse:
    def __init__(self, warehouses: WarehousesResource) -> None:
        self._warehouses = warehouses

        self.retrieve = to_streamed_response_wrapper(
            warehouses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            warehouses.list,
        )


class AsyncWarehousesResourceWithStreamingResponse:
    def __init__(self, warehouses: AsyncWarehousesResource) -> None:
        self._warehouses = warehouses

        self.retrieve = async_to_streamed_response_wrapper(
            warehouses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            warehouses.list,
        )

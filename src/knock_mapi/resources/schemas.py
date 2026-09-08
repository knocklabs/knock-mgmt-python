# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import schema_list_params, schema_upsert_params, schema_retrieve_params, schema_validate_params
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
from .._base_client import make_request_options
from ..types.schema_list_response import SchemaListResponse

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return SchemasResourceWithStreamingResponse(self)

    def retrieve(
        self,
        item_type: str,
        *,
        branch: str | Omit = omit,
        collection: str | Omit = omit,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve the configuration for an item schema (`user`, `tenant`, or `object`) in
        a given environment, including all of its configured properties.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          collection: The object collection, required when `item_type` is `object`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_type:
            raise ValueError(f"Expected a non-empty value for `item_type` but received {item_type!r}")
        return self._get(
            path_template("/v1/schemas/{item_type}", item_type=item_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "branch": branch,
                        "collection": collection,
                        "environment": environment,
                    },
                    schema_retrieve_params.SchemaRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        item_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """
        Retrieve the configuration for all managed item schemas (`user`, `tenant`, and
        `object`) in a given environment. Branch-qualified reads return the schemas
        inherited from the parent environment.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          item_type: Filter schemas by item type (`user`, `tenant`, or `object`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "branch": branch,
                        "environment": environment,
                        "item_type": item_type,
                    },
                    schema_list_params.SchemaListParams,
                ),
            ),
            cast_to=SchemaListResponse,
        )

    def upsert(
        self,
        item_type: str,
        *,
        branch: str | Omit = omit,
        collection: str | Omit = omit,
        environment: str | Omit = omit,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Applies changes for the item schema properties in the request.

        Omitted
        properties are left unchanged; hide a property with `visible: false` rather than
        removing it. The required permissions depend on what changes: changing a
        property's display settings (`visible`/`description`) requires
        `item_schemas:manage`; changing a property's type or example, or adding a
        property, requires `item_schemas:edit`. Adding a property that is already hidden
        or already has a description requires both.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          collection: The object collection, required when `item_type` is `object`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_type:
            raise ValueError(f"Expected a non-empty value for `item_type` but received {item_type!r}")
        return self._put(
            path_template("/v1/schemas/{item_type}", item_type=item_type),
            body=maybe_transform(body, schema_upsert_params.SchemaUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "branch": branch,
                        "collection": collection,
                        "environment": environment,
                    },
                    schema_upsert_params.SchemaUpsertParams,
                ),
            ),
            cast_to=object,
        )

    def validate(
        self,
        item_type: str,
        *,
        branch: str | Omit = omit,
        collection: str | Omit = omit,
        environment: str | Omit = omit,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Checks an item schema configuration payload and reports which permissions it
        would require, without saving any changes.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          collection: The object collection, required when `item_type` is `object`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_type:
            raise ValueError(f"Expected a non-empty value for `item_type` but received {item_type!r}")
        return self._put(
            path_template("/v1/schemas/{item_type}/validate", item_type=item_type),
            body=maybe_transform(body, schema_validate_params.SchemaValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "branch": branch,
                        "collection": collection,
                        "environment": environment,
                    },
                    schema_validate_params.SchemaValidateParams,
                ),
            ),
            cast_to=object,
        )


class AsyncSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        item_type: str,
        *,
        branch: str | Omit = omit,
        collection: str | Omit = omit,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve the configuration for an item schema (`user`, `tenant`, or `object`) in
        a given environment, including all of its configured properties.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          collection: The object collection, required when `item_type` is `object`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_type:
            raise ValueError(f"Expected a non-empty value for `item_type` but received {item_type!r}")
        return await self._get(
            path_template("/v1/schemas/{item_type}", item_type=item_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "branch": branch,
                        "collection": collection,
                        "environment": environment,
                    },
                    schema_retrieve_params.SchemaRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        branch: str | Omit = omit,
        environment: str | Omit = omit,
        item_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """
        Retrieve the configuration for all managed item schemas (`user`, `tenant`, and
        `object`) in a given environment. Branch-qualified reads return the schemas
        inherited from the parent environment.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          environment: The environment slug. When omitted, the account's default environment is used.

          item_type: Filter schemas by item type (`user`, `tenant`, or `object`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "branch": branch,
                        "environment": environment,
                        "item_type": item_type,
                    },
                    schema_list_params.SchemaListParams,
                ),
            ),
            cast_to=SchemaListResponse,
        )

    async def upsert(
        self,
        item_type: str,
        *,
        branch: str | Omit = omit,
        collection: str | Omit = omit,
        environment: str | Omit = omit,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Applies changes for the item schema properties in the request.

        Omitted
        properties are left unchanged; hide a property with `visible: false` rather than
        removing it. The required permissions depend on what changes: changing a
        property's display settings (`visible`/`description`) requires
        `item_schemas:manage`; changing a property's type or example, or adding a
        property, requires `item_schemas:edit`. Adding a property that is already hidden
        or already has a description requires both.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          collection: The object collection, required when `item_type` is `object`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_type:
            raise ValueError(f"Expected a non-empty value for `item_type` but received {item_type!r}")
        return await self._put(
            path_template("/v1/schemas/{item_type}", item_type=item_type),
            body=await async_maybe_transform(body, schema_upsert_params.SchemaUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "branch": branch,
                        "collection": collection,
                        "environment": environment,
                    },
                    schema_upsert_params.SchemaUpsertParams,
                ),
            ),
            cast_to=object,
        )

    async def validate(
        self,
        item_type: str,
        *,
        branch: str | Omit = omit,
        collection: str | Omit = omit,
        environment: str | Omit = omit,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Checks an item schema configuration payload and reports which permissions it
        would require, without saving any changes.

        Args:
          branch: The slug of a branch to use. When `environment` is omitted, the branch is
              resolved from Development after the account default is injected. When
              `environment` is supplied, it must be `"development"`.

          collection: The object collection, required when `item_type` is `object`.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_type:
            raise ValueError(f"Expected a non-empty value for `item_type` but received {item_type!r}")
        return await self._put(
            path_template("/v1/schemas/{item_type}/validate", item_type=item_type),
            body=await async_maybe_transform(body, schema_validate_params.SchemaValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "branch": branch,
                        "collection": collection,
                        "environment": environment,
                    },
                    schema_validate_params.SchemaValidateParams,
                ),
            ),
            cast_to=object,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.upsert = to_raw_response_wrapper(
            schemas.upsert,
        )
        self.validate = to_raw_response_wrapper(
            schemas.validate,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = async_to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            schemas.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            schemas.validate,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.upsert = to_streamed_response_wrapper(
            schemas.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            schemas.validate,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = async_to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            schemas.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            schemas.validate,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    message_type_list_params,
    message_type_upsert_params,
    message_type_retrieve_params,
    message_type_validate_params,
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
from ..types.message_type import MessageType
from ..types.message_type_upsert_response import MessageTypeUpsertResponse
from ..types.message_type_validate_response import MessageTypeValidateResponse

__all__ = ["MessageTypesResource", "AsyncMessageTypesResource"]


class MessageTypesResource(SyncAPIResource):
    """
    A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
    """

    @cached_property
    def with_raw_response(self) -> MessageTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return MessageTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return MessageTypesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_type_key: str,
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
    ) -> MessageType:
        """
        Retrieve a message type by its key, in a given environment.

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
        if not message_type_key:
            raise ValueError(f"Expected a non-empty value for `message_type_key` but received {message_type_key!r}")
        return self._get(
            f"/v1/message_types/{message_type_key}",
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
                    message_type_retrieve_params.MessageTypeRetrieveParams,
                ),
            ),
            cast_to=MessageType,
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
    ) -> SyncEntriesCursor[MessageType]:
        """
        Returns a paginated list of message types available in a given environment.

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
            "/v1/message_types",
            page=SyncEntriesCursor[MessageType],
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
                    message_type_list_params.MessageTypeListParams,
                ),
            ),
            model=MessageType,
        )

    def upsert(
        self,
        message_type_key: str,
        *,
        environment: str,
        message_type: message_type_upsert_params.MessageType,
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
    ) -> MessageTypeUpsertResponse:
        """
        Updates a message type, or creates a new one if it does not yet exist.

        Note: this endpoint only operates in the `development` environment.

        Args:
          environment: The environment slug.

          message_type: A request to create a message type.

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
        if not message_type_key:
            raise ValueError(f"Expected a non-empty value for `message_type_key` but received {message_type_key!r}")
        return self._put(
            f"/v1/message_types/{message_type_key}",
            body=maybe_transform({"message_type": message_type}, message_type_upsert_params.MessageTypeUpsertParams),
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
                    message_type_upsert_params.MessageTypeUpsertParams,
                ),
            ),
            cast_to=MessageTypeUpsertResponse,
        )

    def validate(
        self,
        message_type_key: str,
        *,
        environment: str,
        message_type: message_type_validate_params.MessageType,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTypeValidateResponse:
        """
        Validates a message type payload without persisting it.

        Note: this endpoint only operates on message types in the `development`
        environment.

        Args:
          environment: The environment slug.

          message_type: A request to create a message type.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_type_key:
            raise ValueError(f"Expected a non-empty value for `message_type_key` but received {message_type_key!r}")
        return self._put(
            f"/v1/message_types/{message_type_key}/validate",
            body=maybe_transform(
                {"message_type": message_type}, message_type_validate_params.MessageTypeValidateParams
            ),
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
                    message_type_validate_params.MessageTypeValidateParams,
                ),
            ),
            cast_to=MessageTypeValidateResponse,
        )


class AsyncMessageTypesResource(AsyncAPIResource):
    """
    A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMessageTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessageTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncMessageTypesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_type_key: str,
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
    ) -> MessageType:
        """
        Retrieve a message type by its key, in a given environment.

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
        if not message_type_key:
            raise ValueError(f"Expected a non-empty value for `message_type_key` but received {message_type_key!r}")
        return await self._get(
            f"/v1/message_types/{message_type_key}",
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
                    message_type_retrieve_params.MessageTypeRetrieveParams,
                ),
            ),
            cast_to=MessageType,
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
    ) -> AsyncPaginator[MessageType, AsyncEntriesCursor[MessageType]]:
        """
        Returns a paginated list of message types available in a given environment.

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
            "/v1/message_types",
            page=AsyncEntriesCursor[MessageType],
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
                    message_type_list_params.MessageTypeListParams,
                ),
            ),
            model=MessageType,
        )

    async def upsert(
        self,
        message_type_key: str,
        *,
        environment: str,
        message_type: message_type_upsert_params.MessageType,
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
    ) -> MessageTypeUpsertResponse:
        """
        Updates a message type, or creates a new one if it does not yet exist.

        Note: this endpoint only operates in the `development` environment.

        Args:
          environment: The environment slug.

          message_type: A request to create a message type.

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
        if not message_type_key:
            raise ValueError(f"Expected a non-empty value for `message_type_key` but received {message_type_key!r}")
        return await self._put(
            f"/v1/message_types/{message_type_key}",
            body=await async_maybe_transform(
                {"message_type": message_type}, message_type_upsert_params.MessageTypeUpsertParams
            ),
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
                    message_type_upsert_params.MessageTypeUpsertParams,
                ),
            ),
            cast_to=MessageTypeUpsertResponse,
        )

    async def validate(
        self,
        message_type_key: str,
        *,
        environment: str,
        message_type: message_type_validate_params.MessageType,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTypeValidateResponse:
        """
        Validates a message type payload without persisting it.

        Note: this endpoint only operates on message types in the `development`
        environment.

        Args:
          environment: The environment slug.

          message_type: A request to create a message type.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_type_key:
            raise ValueError(f"Expected a non-empty value for `message_type_key` but received {message_type_key!r}")
        return await self._put(
            f"/v1/message_types/{message_type_key}/validate",
            body=await async_maybe_transform(
                {"message_type": message_type}, message_type_validate_params.MessageTypeValidateParams
            ),
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
                    message_type_validate_params.MessageTypeValidateParams,
                ),
            ),
            cast_to=MessageTypeValidateResponse,
        )


class MessageTypesResourceWithRawResponse:
    def __init__(self, message_types: MessageTypesResource) -> None:
        self._message_types = message_types

        self.retrieve = to_raw_response_wrapper(
            message_types.retrieve,
        )
        self.list = to_raw_response_wrapper(
            message_types.list,
        )
        self.upsert = to_raw_response_wrapper(
            message_types.upsert,
        )
        self.validate = to_raw_response_wrapper(
            message_types.validate,
        )


class AsyncMessageTypesResourceWithRawResponse:
    def __init__(self, message_types: AsyncMessageTypesResource) -> None:
        self._message_types = message_types

        self.retrieve = async_to_raw_response_wrapper(
            message_types.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            message_types.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            message_types.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            message_types.validate,
        )


class MessageTypesResourceWithStreamingResponse:
    def __init__(self, message_types: MessageTypesResource) -> None:
        self._message_types = message_types

        self.retrieve = to_streamed_response_wrapper(
            message_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            message_types.list,
        )
        self.upsert = to_streamed_response_wrapper(
            message_types.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            message_types.validate,
        )


class AsyncMessageTypesResourceWithStreamingResponse:
    def __init__(self, message_types: AsyncMessageTypesResource) -> None:
        self._message_types = message_types

        self.retrieve = async_to_streamed_response_wrapper(
            message_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            message_types.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            message_types.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            message_types.validate,
        )

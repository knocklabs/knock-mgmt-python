# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.goals import attachment_list_params, attachment_delete_params, attachment_update_params
from ..._base_client import make_request_options
from ...types.goals.attachment_list_response import AttachmentListResponse
from ...types.goals.attachment_delete_response import AttachmentDeleteResponse
from ...types.goals.attachment_update_response import AttachmentUpdateResponse

__all__ = ["AttachmentsResource", "AsyncAttachmentsResource"]


class AttachmentsResource(SyncAPIResource):
    """
    Goals define event conditions that are tracked and attributed to messaging resources.
    """

    @cached_property
    def with_raw_response(self) -> AttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AttachmentsResourceWithStreamingResponse(self)

    def update(
        self,
        resource_key: str,
        *,
        goal_key: str,
        resource_type: Literal["workflow", "guide", "broadcast"],
        attachment: attachment_update_params.Attachment,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentUpdateResponse:
        """
        Attaches the goal to a workflow, guide, or broadcast in the given environment,
        or updates its attribution window. The attachment goes live without a commit:
        the resource is published in the background, so the response doesn't wait on it.
        Workflows and guides must have been committed in the environment, and broadcasts
        must not have been sent. A resource holds one goal, so this replaces any other
        goal attached to it.

        Args:
          attachment: Settings for the goal attachment.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_key:
            raise ValueError(f"Expected a non-empty value for `resource_key` but received {resource_key!r}")
        return self._put(
            path_template(
                "/v1/goals/{goal_key}/attachments/{resource_type}/{resource_key}",
                goal_key=goal_key,
                resource_type=resource_type,
                resource_key=resource_key,
            ),
            body=maybe_transform({"attachment": attachment}, attachment_update_params.AttachmentUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, attachment_update_params.AttachmentUpdateParams),
            ),
            cast_to=AttachmentUpdateResponse,
        )

    def list(
        self,
        goal_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentListResponse:
        """
        Returns the workflows, guides, and broadcasts the goal is attached to in the
        given environment.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return self._get(
            path_template("/v1/goals/{goal_key}/attachments", goal_key=goal_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, attachment_list_params.AttachmentListParams),
            ),
            cast_to=AttachmentListResponse,
        )

    def delete(
        self,
        resource_key: str,
        *,
        goal_key: str,
        resource_type: Literal["workflow", "guide", "broadcast"],
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentDeleteResponse:
        """
        Detaches the goal from a workflow, guide, or broadcast in the given environment.
        The change goes live without a commit: the resource is published in the
        background, so the response doesn't wait on it. Returns 404 when the goal isn't
        attached to the resource.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_key:
            raise ValueError(f"Expected a non-empty value for `resource_key` but received {resource_key!r}")
        return self._delete(
            path_template(
                "/v1/goals/{goal_key}/attachments/{resource_type}/{resource_key}",
                goal_key=goal_key,
                resource_type=resource_type,
                resource_key=resource_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, attachment_delete_params.AttachmentDeleteParams),
            ),
            cast_to=AttachmentDeleteResponse,
        )


class AsyncAttachmentsResource(AsyncAPIResource):
    """
    Goals define event conditions that are tracked and attributed to messaging resources.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncAttachmentsResourceWithStreamingResponse(self)

    async def update(
        self,
        resource_key: str,
        *,
        goal_key: str,
        resource_type: Literal["workflow", "guide", "broadcast"],
        attachment: attachment_update_params.Attachment,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentUpdateResponse:
        """
        Attaches the goal to a workflow, guide, or broadcast in the given environment,
        or updates its attribution window. The attachment goes live without a commit:
        the resource is published in the background, so the response doesn't wait on it.
        Workflows and guides must have been committed in the environment, and broadcasts
        must not have been sent. A resource holds one goal, so this replaces any other
        goal attached to it.

        Args:
          attachment: Settings for the goal attachment.

          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_key:
            raise ValueError(f"Expected a non-empty value for `resource_key` but received {resource_key!r}")
        return await self._put(
            path_template(
                "/v1/goals/{goal_key}/attachments/{resource_type}/{resource_key}",
                goal_key=goal_key,
                resource_type=resource_type,
                resource_key=resource_key,
            ),
            body=await async_maybe_transform(
                {"attachment": attachment}, attachment_update_params.AttachmentUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, attachment_update_params.AttachmentUpdateParams
                ),
            ),
            cast_to=AttachmentUpdateResponse,
        )

    async def list(
        self,
        goal_key: str,
        *,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentListResponse:
        """
        Returns the workflows, guides, and broadcasts the goal is attached to in the
        given environment.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        return await self._get(
            path_template("/v1/goals/{goal_key}/attachments", goal_key=goal_key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, attachment_list_params.AttachmentListParams
                ),
            ),
            cast_to=AttachmentListResponse,
        )

    async def delete(
        self,
        resource_key: str,
        *,
        goal_key: str,
        resource_type: Literal["workflow", "guide", "broadcast"],
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentDeleteResponse:
        """
        Detaches the goal from a workflow, guide, or broadcast in the given environment.
        The change goes live without a commit: the resource is published in the
        background, so the response doesn't wait on it. Returns 404 when the goal isn't
        attached to the resource.

        Args:
          environment: The environment slug. When omitted, the account's default environment is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_key:
            raise ValueError(f"Expected a non-empty value for `goal_key` but received {goal_key!r}")
        if not resource_type:
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if not resource_key:
            raise ValueError(f"Expected a non-empty value for `resource_key` but received {resource_key!r}")
        return await self._delete(
            path_template(
                "/v1/goals/{goal_key}/attachments/{resource_type}/{resource_key}",
                goal_key=goal_key,
                resource_type=resource_type,
                resource_key=resource_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, attachment_delete_params.AttachmentDeleteParams
                ),
            ),
            cast_to=AttachmentDeleteResponse,
        )


class AttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.update = to_raw_response_wrapper(
            attachments.update,
        )
        self.list = to_raw_response_wrapper(
            attachments.list,
        )
        self.delete = to_raw_response_wrapper(
            attachments.delete,
        )


class AsyncAttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.update = async_to_raw_response_wrapper(
            attachments.update,
        )
        self.list = async_to_raw_response_wrapper(
            attachments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            attachments.delete,
        )


class AttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.update = to_streamed_response_wrapper(
            attachments.update,
        )
        self.list = to_streamed_response_wrapper(
            attachments.list,
        )
        self.delete = to_streamed_response_wrapper(
            attachments.delete,
        )


class AsyncAttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.update = async_to_streamed_response_wrapper(
            attachments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            attachments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            attachments.delete,
        )

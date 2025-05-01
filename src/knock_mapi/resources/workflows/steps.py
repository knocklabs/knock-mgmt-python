# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workflows import step_preview_template_params
from ...types.workflows.step_preview_template_response import StepPreviewTemplateResponse

__all__ = ["StepsResource", "AsyncStepsResource"]


class StepsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StepsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return StepsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StepsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return StepsResourceWithStreamingResponse(self)

    def preview_template(
        self,
        step_ref: str,
        *,
        workflow_key: str,
        environment: str,
        recipient: step_preview_template_params.Recipient,
        actor: Optional[step_preview_template_params.Actor] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepPreviewTemplateResponse:
        """
        Generates a rendered template for a given channel step in a workflow.

        Args:
          environment: The environment slug.

          recipient: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          actor: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          data: The data to pass to the workflow template for rendering.

          tenant: The tenant to associate the workflow with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        if not step_ref:
            raise ValueError(f"Expected a non-empty value for `step_ref` but received {step_ref!r}")
        return self._post(
            f"/v1/workflows/{workflow_key}/steps/{step_ref}/preview_template",
            body=maybe_transform(
                {
                    "recipient": recipient,
                    "actor": actor,
                    "data": data,
                    "tenant": tenant,
                },
                step_preview_template_params.StepPreviewTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"environment": environment}, step_preview_template_params.StepPreviewTemplateParams
                ),
            ),
            cast_to=StepPreviewTemplateResponse,
        )


class AsyncStepsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStepsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStepsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStepsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncStepsResourceWithStreamingResponse(self)

    async def preview_template(
        self,
        step_ref: str,
        *,
        workflow_key: str,
        environment: str,
        recipient: step_preview_template_params.Recipient,
        actor: Optional[step_preview_template_params.Actor] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StepPreviewTemplateResponse:
        """
        Generates a rendered template for a given channel step in a workflow.

        Args:
          environment: The environment slug.

          recipient: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          actor: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          data: The data to pass to the workflow template for rendering.

          tenant: The tenant to associate the workflow with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        if not step_ref:
            raise ValueError(f"Expected a non-empty value for `step_ref` but received {step_ref!r}")
        return await self._post(
            f"/v1/workflows/{workflow_key}/steps/{step_ref}/preview_template",
            body=await async_maybe_transform(
                {
                    "recipient": recipient,
                    "actor": actor,
                    "data": data,
                    "tenant": tenant,
                },
                step_preview_template_params.StepPreviewTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, step_preview_template_params.StepPreviewTemplateParams
                ),
            ),
            cast_to=StepPreviewTemplateResponse,
        )


class StepsResourceWithRawResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.preview_template = to_raw_response_wrapper(
            steps.preview_template,
        )


class AsyncStepsResourceWithRawResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.preview_template = async_to_raw_response_wrapper(
            steps.preview_template,
        )


class StepsResourceWithStreamingResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.preview_template = to_streamed_response_wrapper(
            steps.preview_template,
        )


class AsyncStepsResourceWithStreamingResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.preview_template = async_to_streamed_response_wrapper(
            steps.preview_template,
        )

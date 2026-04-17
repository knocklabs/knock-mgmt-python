# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import template_preview_params
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
from .._base_client import make_request_options
from ..types.template_preview_response import TemplatePreviewResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def preview(
        self,
        *,
        environment: str,
        channel_type: Literal["email", "sms", "push", "chat", "in_app_feed"],
        recipient: template_preview_params.Recipient,
        template: template_preview_params.Template,
        branch: str | Omit = omit,
        actor: Optional[template_preview_params.Actor] | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        layout: Optional[template_preview_params.Layout] | Omit = omit,
        tenant: Optional[str] | Omit = omit,
        workflow: Optional[template_preview_params.Workflow] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplatePreviewResponse:
        """
        Renders a template preview, without requiring a template to be persisted within
        Knock. This is useful for previewing templates in isolation, without the need to
        use a workflow.

        For email templates, you can optionally specify a layout by key or provide
        inline layout content.

        Args:
          environment: The environment slug.

          channel_type: The channel type of the template to preview.

          recipient: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          template: The template content to preview. Structure depends on channel_type.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          actor: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          data: The data to pass to the template for rendering.

          layout: Email layout configuration. Only applicable for email channel type. Falls back
              to environment default if not provided.

          tenant: The tenant to associate with the preview. Must not contain whitespace.

          workflow: Optional workflow context for variable hydration. When provided,
              recipient/actor/tenant are resolved via Knock.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/templates/preview",
            body=maybe_transform(
                {
                    "channel_type": channel_type,
                    "recipient": recipient,
                    "template": template,
                    "actor": actor,
                    "data": data,
                    "layout": layout,
                    "tenant": tenant,
                    "workflow": workflow,
                },
                template_preview_params.TemplatePreviewParams,
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
                    template_preview_params.TemplatePreviewParams,
                ),
            ),
            cast_to=TemplatePreviewResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def preview(
        self,
        *,
        environment: str,
        channel_type: Literal["email", "sms", "push", "chat", "in_app_feed"],
        recipient: template_preview_params.Recipient,
        template: template_preview_params.Template,
        branch: str | Omit = omit,
        actor: Optional[template_preview_params.Actor] | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        layout: Optional[template_preview_params.Layout] | Omit = omit,
        tenant: Optional[str] | Omit = omit,
        workflow: Optional[template_preview_params.Workflow] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplatePreviewResponse:
        """
        Renders a template preview, without requiring a template to be persisted within
        Knock. This is useful for previewing templates in isolation, without the need to
        use a workflow.

        For email templates, you can optionally specify a layout by key or provide
        inline layout content.

        Args:
          environment: The environment slug.

          channel_type: The channel type of the template to preview.

          recipient: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          template: The template content to preview. Structure depends on channel_type.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          actor: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          data: The data to pass to the template for rendering.

          layout: Email layout configuration. Only applicable for email channel type. Falls back
              to environment default if not provided.

          tenant: The tenant to associate with the preview. Must not contain whitespace.

          workflow: Optional workflow context for variable hydration. When provided,
              recipient/actor/tenant are resolved via Knock.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/templates/preview",
            body=await async_maybe_transform(
                {
                    "channel_type": channel_type,
                    "recipient": recipient,
                    "template": template,
                    "actor": actor,
                    "data": data,
                    "layout": layout,
                    "tenant": tenant,
                    "workflow": workflow,
                },
                template_preview_params.TemplatePreviewParams,
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
                    template_preview_params.TemplatePreviewParams,
                ),
            ),
            cast_to=TemplatePreviewResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.preview = to_raw_response_wrapper(
            templates.preview,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.preview = async_to_raw_response_wrapper(
            templates.preview,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.preview = to_streamed_response_wrapper(
            templates.preview,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.preview = async_to_streamed_response_wrapper(
            templates.preview,
        )

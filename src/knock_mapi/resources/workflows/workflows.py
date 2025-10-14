# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .steps import (
    StepsResource,
    AsyncStepsResource,
    StepsResourceWithRawResponse,
    AsyncStepsResourceWithRawResponse,
    StepsResourceWithStreamingResponse,
    AsyncStepsResourceWithStreamingResponse,
)
from ...types import (
    workflow_run_params,
    workflow_list_params,
    workflow_upsert_params,
    workflow_activate_params,
    workflow_retrieve_params,
    workflow_validate_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncEntriesCursor, AsyncEntriesCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workflow import Workflow
from ...types.workflow_run_response import WorkflowRunResponse
from ...types.workflow_upsert_response import WorkflowUpsertResponse
from ...types.workflow_activate_response import WorkflowActivateResponse
from ...types.workflow_retrieve_response import WorkflowRetrieveResponse
from ...types.workflow_validate_response import WorkflowValidateResponse

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def steps(self) -> StepsResource:
        return StepsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        workflow_key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRetrieveResponse:
        """
        Retrieve a workflow by its key in a given environment.

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
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return self._get(
            f"/v1/workflows/{workflow_key}",
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
                    workflow_retrieve_params.WorkflowRetrieveParams,
                ),
            ),
            cast_to=WorkflowRetrieveResponse,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Workflow]:
        """Returns a paginated list of workflows available in a given environment.

        The
        workflows are returned alphabetically by `key`.

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
            "/v1/workflows",
            page=SyncEntriesCursor[Workflow],
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
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            model=Workflow,
        )

    def activate(
        self,
        workflow_key: str,
        *,
        environment: str,
        status: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowActivateResponse:
        """Activates (or deactivates) a workflow in a given environment.

        Read more in the
        [docs](https://docs.knock.app/concepts/workflows#workflow-status).

        Note: This immediately enables or disables a workflow in a given environment
        without needing to go through environment promotion.

        Args:
          environment: The environment slug.

          status: Whether to activate or deactivate the workflow. Set to `true` by default, which
              will activate the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return self._put(
            f"/v1/workflows/{workflow_key}/activate",
            body=maybe_transform({"status": status}, workflow_activate_params.WorkflowActivateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, workflow_activate_params.WorkflowActivateParams),
            ),
            cast_to=WorkflowActivateResponse,
        )

    def run(
        self,
        workflow_key: str,
        *,
        environment: str,
        recipients: SequenceNotStr[workflow_run_params.Recipient],
        actor: Optional[workflow_run_params.Actor] | Omit = omit,
        cancellation_key: Optional[str] | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        tenant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRunResponse:
        """
        Runs the latest version of a committed workflow in a given environment using the
        params provided.

        Args:
          environment: The environment slug.

          recipients: A list of recipients to run the workflow for.

          actor: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          cancellation_key: A key to cancel the workflow run.

          data: A map of data to be used in the workflow run.

          tenant: The tenant to associate the workflow run with. Must not contain whitespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return self._put(
            f"/v1/workflows/{workflow_key}/run",
            body=maybe_transform(
                {
                    "recipients": recipients,
                    "actor": actor,
                    "cancellation_key": cancellation_key,
                    "data": data,
                    "tenant": tenant,
                },
                workflow_run_params.WorkflowRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, workflow_run_params.WorkflowRunParams),
            ),
            cast_to=WorkflowRunResponse,
        )

    def upsert(
        self,
        workflow_key: str,
        *,
        environment: str,
        workflow: workflow_upsert_params.Workflow,
        annotate: bool | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowUpsertResponse:
        """
        Updates a workflow of a given key, or creates a new one if it does not yet
        exist.

        Note: this endpoint only operates on workflows in the `development` environment.

        Args:
          environment: The environment slug.

          workflow: A workflow request for upserting a workflow.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return self._put(
            f"/v1/workflows/{workflow_key}",
            body=maybe_transform({"workflow": workflow}, workflow_upsert_params.WorkflowUpsertParams),
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
                    workflow_upsert_params.WorkflowUpsertParams,
                ),
            ),
            cast_to=WorkflowUpsertResponse,
        )

    def validate(
        self,
        workflow_key: str,
        *,
        environment: str,
        workflow: workflow_validate_params.Workflow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowValidateResponse:
        """Validates a workflow payload without persisting it.

        Some read-only fields will
        be empty as they are generated by the system when persisted.

        Note: Validating a workflow is only done in the development environment context.

        Args:
          environment: The environment slug.

          workflow: A workflow request for upserting a workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return self._put(
            f"/v1/workflows/{workflow_key}/validate",
            body=maybe_transform({"workflow": workflow}, workflow_validate_params.WorkflowValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, workflow_validate_params.WorkflowValidateParams),
            ),
            cast_to=WorkflowValidateResponse,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def steps(self) -> AsyncStepsResource:
        return AsyncStepsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        workflow_key: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRetrieveResponse:
        """
        Retrieve a workflow by its key in a given environment.

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
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return await self._get(
            f"/v1/workflows/{workflow_key}",
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
                    workflow_retrieve_params.WorkflowRetrieveParams,
                ),
            ),
            cast_to=WorkflowRetrieveResponse,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workflow, AsyncEntriesCursor[Workflow]]:
        """Returns a paginated list of workflows available in a given environment.

        The
        workflows are returned alphabetically by `key`.

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
            "/v1/workflows",
            page=AsyncEntriesCursor[Workflow],
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
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            model=Workflow,
        )

    async def activate(
        self,
        workflow_key: str,
        *,
        environment: str,
        status: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowActivateResponse:
        """Activates (or deactivates) a workflow in a given environment.

        Read more in the
        [docs](https://docs.knock.app/concepts/workflows#workflow-status).

        Note: This immediately enables or disables a workflow in a given environment
        without needing to go through environment promotion.

        Args:
          environment: The environment slug.

          status: Whether to activate or deactivate the workflow. Set to `true` by default, which
              will activate the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return await self._put(
            f"/v1/workflows/{workflow_key}/activate",
            body=await async_maybe_transform({"status": status}, workflow_activate_params.WorkflowActivateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, workflow_activate_params.WorkflowActivateParams
                ),
            ),
            cast_to=WorkflowActivateResponse,
        )

    async def run(
        self,
        workflow_key: str,
        *,
        environment: str,
        recipients: SequenceNotStr[workflow_run_params.Recipient],
        actor: Optional[workflow_run_params.Actor] | Omit = omit,
        cancellation_key: Optional[str] | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        tenant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRunResponse:
        """
        Runs the latest version of a committed workflow in a given environment using the
        params provided.

        Args:
          environment: The environment slug.

          recipients: A list of recipients to run the workflow for.

          actor: A recipient reference, used when referencing a recipient by either their ID (for
              a user), or by a reference for an object.

          cancellation_key: A key to cancel the workflow run.

          data: A map of data to be used in the workflow run.

          tenant: The tenant to associate the workflow run with. Must not contain whitespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return await self._put(
            f"/v1/workflows/{workflow_key}/run",
            body=await async_maybe_transform(
                {
                    "recipients": recipients,
                    "actor": actor,
                    "cancellation_key": cancellation_key,
                    "data": data,
                    "tenant": tenant,
                },
                workflow_run_params.WorkflowRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"environment": environment}, workflow_run_params.WorkflowRunParams),
            ),
            cast_to=WorkflowRunResponse,
        )

    async def upsert(
        self,
        workflow_key: str,
        *,
        environment: str,
        workflow: workflow_upsert_params.Workflow,
        annotate: bool | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowUpsertResponse:
        """
        Updates a workflow of a given key, or creates a new one if it does not yet
        exist.

        Note: this endpoint only operates on workflows in the `development` environment.

        Args:
          environment: The environment slug.

          workflow: A workflow request for upserting a workflow.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return await self._put(
            f"/v1/workflows/{workflow_key}",
            body=await async_maybe_transform({"workflow": workflow}, workflow_upsert_params.WorkflowUpsertParams),
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
                    workflow_upsert_params.WorkflowUpsertParams,
                ),
            ),
            cast_to=WorkflowUpsertResponse,
        )

    async def validate(
        self,
        workflow_key: str,
        *,
        environment: str,
        workflow: workflow_validate_params.Workflow,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowValidateResponse:
        """Validates a workflow payload without persisting it.

        Some read-only fields will
        be empty as they are generated by the system when persisted.

        Note: Validating a workflow is only done in the development environment context.

        Args:
          environment: The environment slug.

          workflow: A workflow request for upserting a workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_key:
            raise ValueError(f"Expected a non-empty value for `workflow_key` but received {workflow_key!r}")
        return await self._put(
            f"/v1/workflows/{workflow_key}/validate",
            body=await async_maybe_transform({"workflow": workflow}, workflow_validate_params.WorkflowValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, workflow_validate_params.WorkflowValidateParams
                ),
            ),
            cast_to=WorkflowValidateResponse,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.list = to_raw_response_wrapper(
            workflows.list,
        )
        self.activate = to_raw_response_wrapper(
            workflows.activate,
        )
        self.run = to_raw_response_wrapper(
            workflows.run,
        )
        self.upsert = to_raw_response_wrapper(
            workflows.upsert,
        )
        self.validate = to_raw_response_wrapper(
            workflows.validate,
        )

    @cached_property
    def steps(self) -> StepsResourceWithRawResponse:
        return StepsResourceWithRawResponse(self._workflows.steps)


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = async_to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            workflows.list,
        )
        self.activate = async_to_raw_response_wrapper(
            workflows.activate,
        )
        self.run = async_to_raw_response_wrapper(
            workflows.run,
        )
        self.upsert = async_to_raw_response_wrapper(
            workflows.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            workflows.validate,
        )

    @cached_property
    def steps(self) -> AsyncStepsResourceWithRawResponse:
        return AsyncStepsResourceWithRawResponse(self._workflows.steps)


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            workflows.list,
        )
        self.activate = to_streamed_response_wrapper(
            workflows.activate,
        )
        self.run = to_streamed_response_wrapper(
            workflows.run,
        )
        self.upsert = to_streamed_response_wrapper(
            workflows.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            workflows.validate,
        )

    @cached_property
    def steps(self) -> StepsResourceWithStreamingResponse:
        return StepsResourceWithStreamingResponse(self._workflows.steps)


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = async_to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            workflows.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            workflows.activate,
        )
        self.run = async_to_streamed_response_wrapper(
            workflows.run,
        )
        self.upsert = async_to_streamed_response_wrapper(
            workflows.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            workflows.validate,
        )

    @cached_property
    def steps(self) -> AsyncStepsResourceWithStreamingResponse:
        return AsyncStepsResourceWithStreamingResponse(self._workflows.steps)

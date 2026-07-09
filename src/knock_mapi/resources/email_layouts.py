# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    email_layout_list_params,
    email_layout_upsert_params,
    email_layout_retrieve_params,
    email_layout_validate_params,
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
from ..types.email_layout import EmailLayout
from ..types.email_layout_upsert_response import EmailLayoutUpsertResponse
from ..types.email_layout_validate_response import EmailLayoutValidateResponse

__all__ = ["EmailLayoutsResource", "AsyncEmailLayoutsResource"]


class EmailLayoutsResource(SyncAPIResource):
    """Email layouts wrap your email templates and provide a consistent look and feel."""

    @cached_property
    def with_raw_response(self) -> EmailLayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return EmailLayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailLayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return EmailLayoutsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        email_layout_key: str,
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
    ) -> EmailLayout:
        """
        Retrieve an email layout by its key, in a given environment.

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
        if not email_layout_key:
            raise ValueError(f"Expected a non-empty value for `email_layout_key` but received {email_layout_key!r}")
        return self._get(
            path_template("/v1/email_layouts/{email_layout_key}", email_layout_key=email_layout_key),
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
                    email_layout_retrieve_params.EmailLayoutRetrieveParams,
                ),
            ),
            cast_to=EmailLayout,
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
    ) -> SyncEntriesCursor[EmailLayout]:
        """
        Returns a paginated list of email layouts available in a given environment.

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
            "/v1/email_layouts",
            page=SyncEntriesCursor[EmailLayout],
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
                    email_layout_list_params.EmailLayoutListParams,
                ),
            ),
            model=EmailLayout,
        )

    def upsert(
        self,
        email_layout_key: str,
        *,
        environment: str,
        email_layout: email_layout_upsert_params.EmailLayout,
        allow_empty: bool | Omit = omit,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailLayoutUpsertResponse:
        """
        Updates an email layout, or creates a new one if it does not yet exist.

        Note: this endpoint only operates in the "development" environment.

        Args:
          environment: The environment slug.

          email_layout: A request to update or create an email layout.

          allow_empty: When used with commit, creates a new version with identical content and commits
              it if there are no unpublished changes.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_layout_key:
            raise ValueError(f"Expected a non-empty value for `email_layout_key` but received {email_layout_key!r}")
        return self._put(
            path_template("/v1/email_layouts/{email_layout_key}", email_layout_key=email_layout_key),
            body=maybe_transform({"email_layout": email_layout}, email_layout_upsert_params.EmailLayoutUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "allow_empty": allow_empty,
                        "annotate": annotate,
                        "branch": branch,
                        "commit": commit,
                        "commit_message": commit_message,
                        "force": force,
                    },
                    email_layout_upsert_params.EmailLayoutUpsertParams,
                ),
            ),
            cast_to=EmailLayoutUpsertResponse,
        )

    def validate(
        self,
        email_layout_key: str,
        *,
        environment: str,
        email_layout: email_layout_validate_params.EmailLayout,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailLayoutValidateResponse:
        """
        Validates an email layout payload without persisting it.

        Note: this endpoint only operates in the "development" environment.

        Args:
          environment: The environment slug.

          email_layout: A request to update or create an email layout.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_layout_key:
            raise ValueError(f"Expected a non-empty value for `email_layout_key` but received {email_layout_key!r}")
        return self._put(
            path_template("/v1/email_layouts/{email_layout_key}/validate", email_layout_key=email_layout_key),
            body=maybe_transform(
                {"email_layout": email_layout}, email_layout_validate_params.EmailLayoutValidateParams
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
                    email_layout_validate_params.EmailLayoutValidateParams,
                ),
            ),
            cast_to=EmailLayoutValidateResponse,
        )


class AsyncEmailLayoutsResource(AsyncAPIResource):
    """Email layouts wrap your email templates and provide a consistent look and feel."""

    @cached_property
    def with_raw_response(self) -> AsyncEmailLayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailLayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailLayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncEmailLayoutsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        email_layout_key: str,
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
    ) -> EmailLayout:
        """
        Retrieve an email layout by its key, in a given environment.

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
        if not email_layout_key:
            raise ValueError(f"Expected a non-empty value for `email_layout_key` but received {email_layout_key!r}")
        return await self._get(
            path_template("/v1/email_layouts/{email_layout_key}", email_layout_key=email_layout_key),
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
                    email_layout_retrieve_params.EmailLayoutRetrieveParams,
                ),
            ),
            cast_to=EmailLayout,
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
    ) -> AsyncPaginator[EmailLayout, AsyncEntriesCursor[EmailLayout]]:
        """
        Returns a paginated list of email layouts available in a given environment.

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
            "/v1/email_layouts",
            page=AsyncEntriesCursor[EmailLayout],
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
                    email_layout_list_params.EmailLayoutListParams,
                ),
            ),
            model=EmailLayout,
        )

    async def upsert(
        self,
        email_layout_key: str,
        *,
        environment: str,
        email_layout: email_layout_upsert_params.EmailLayout,
        allow_empty: bool | Omit = omit,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailLayoutUpsertResponse:
        """
        Updates an email layout, or creates a new one if it does not yet exist.

        Note: this endpoint only operates in the "development" environment.

        Args:
          environment: The environment slug.

          email_layout: A request to update or create an email layout.

          allow_empty: When used with commit, creates a new version with identical content and commits
              it if there are no unpublished changes.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_layout_key:
            raise ValueError(f"Expected a non-empty value for `email_layout_key` but received {email_layout_key!r}")
        return await self._put(
            path_template("/v1/email_layouts/{email_layout_key}", email_layout_key=email_layout_key),
            body=await async_maybe_transform(
                {"email_layout": email_layout}, email_layout_upsert_params.EmailLayoutUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "allow_empty": allow_empty,
                        "annotate": annotate,
                        "branch": branch,
                        "commit": commit,
                        "commit_message": commit_message,
                        "force": force,
                    },
                    email_layout_upsert_params.EmailLayoutUpsertParams,
                ),
            ),
            cast_to=EmailLayoutUpsertResponse,
        )

    async def validate(
        self,
        email_layout_key: str,
        *,
        environment: str,
        email_layout: email_layout_validate_params.EmailLayout,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailLayoutValidateResponse:
        """
        Validates an email layout payload without persisting it.

        Note: this endpoint only operates in the "development" environment.

        Args:
          environment: The environment slug.

          email_layout: A request to update or create an email layout.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_layout_key:
            raise ValueError(f"Expected a non-empty value for `email_layout_key` but received {email_layout_key!r}")
        return await self._put(
            path_template("/v1/email_layouts/{email_layout_key}/validate", email_layout_key=email_layout_key),
            body=await async_maybe_transform(
                {"email_layout": email_layout}, email_layout_validate_params.EmailLayoutValidateParams
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
                    email_layout_validate_params.EmailLayoutValidateParams,
                ),
            ),
            cast_to=EmailLayoutValidateResponse,
        )


class EmailLayoutsResourceWithRawResponse:
    def __init__(self, email_layouts: EmailLayoutsResource) -> None:
        self._email_layouts = email_layouts

        self.retrieve = to_raw_response_wrapper(
            email_layouts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            email_layouts.list,
        )
        self.upsert = to_raw_response_wrapper(
            email_layouts.upsert,
        )
        self.validate = to_raw_response_wrapper(
            email_layouts.validate,
        )


class AsyncEmailLayoutsResourceWithRawResponse:
    def __init__(self, email_layouts: AsyncEmailLayoutsResource) -> None:
        self._email_layouts = email_layouts

        self.retrieve = async_to_raw_response_wrapper(
            email_layouts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            email_layouts.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            email_layouts.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            email_layouts.validate,
        )


class EmailLayoutsResourceWithStreamingResponse:
    def __init__(self, email_layouts: EmailLayoutsResource) -> None:
        self._email_layouts = email_layouts

        self.retrieve = to_streamed_response_wrapper(
            email_layouts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            email_layouts.list,
        )
        self.upsert = to_streamed_response_wrapper(
            email_layouts.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            email_layouts.validate,
        )


class AsyncEmailLayoutsResourceWithStreamingResponse:
    def __init__(self, email_layouts: AsyncEmailLayoutsResource) -> None:
        self._email_layouts = email_layouts

        self.retrieve = async_to_streamed_response_wrapper(
            email_layouts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            email_layouts.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            email_layouts.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            email_layouts.validate,
        )

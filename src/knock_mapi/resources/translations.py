# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    translation_list_params,
    translation_upsert_params,
    translation_retrieve_params,
    translation_validate_params,
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
from ..types.translation import Translation
from ..types.translation_upsert_response import TranslationUpsertResponse
from ..types.translation_retrieve_response import TranslationRetrieveResponse
from ..types.translation_validate_response import TranslationValidateResponse

__all__ = ["TranslationsResource", "AsyncTranslationsResource"]


class TranslationsResource(SyncAPIResource):
    """Translations are per-locale string files that can be used in your templates."""

    @cached_property
    def with_raw_response(self) -> TranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return TranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return TranslationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        locale_code: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        format: Literal["json", "po"] | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationRetrieveResponse:
        """
        Retrieve a translation by its locale and namespace, in a given environment.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          format: Optionally specify the returned content format. Supports 'json' and 'po'.
              Defaults to 'json'.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          namespace: A specific namespace to filter translations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not locale_code:
            raise ValueError(f"Expected a non-empty value for `locale_code` but received {locale_code!r}")
        return self._get(
            f"/v1/translations/{locale_code}",
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
                        "format": format,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "namespace": namespace,
                    },
                    translation_retrieve_params.TranslationRetrieveParams,
                ),
            ),
            cast_to=TranslationRetrieveResponse,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        format: Literal["json", "po"] | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        locale_code: str | Omit = omit,
        namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Translation]:
        """Returns a paginated list of translations available in a given environment.

        The
        translations are returned in alphabetical order by locale code.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          format: Optionally specify the returned content format. Supports 'json' and 'po'.
              Defaults to 'json'.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          locale_code: A specific locale code to filter translations for.

          namespace: A specific namespace to filter translations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/translations",
            page=SyncEntriesCursor[Translation],
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
                        "format": format,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                        "locale_code": locale_code,
                        "namespace": namespace,
                    },
                    translation_list_params.TranslationListParams,
                ),
            ),
            model=Translation,
        )

    def upsert(
        self,
        locale_code: str,
        *,
        environment: str,
        namespace: str,
        translation: translation_upsert_params.Translation,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        force: bool | Omit = omit,
        format: Literal["json", "po"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationUpsertResponse:
        """
        Updates a translation of a given locale code + namespace, or creates a new one
        if it does not yet exist.

        Note: this endpoint only operates on translations in the "development"
        environment.

        Args:
          environment: The environment slug.

          namespace: An optional namespace that identifies the translation.

          translation: A translation object with a content attribute used to update or create a
              translation.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          format: Optionally specify the returned content format. Supports 'json' and 'po'.
              Defaults to 'json'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not locale_code:
            raise ValueError(f"Expected a non-empty value for `locale_code` but received {locale_code!r}")
        return self._put(
            f"/v1/translations/{locale_code}",
            body=maybe_transform({"translation": translation}, translation_upsert_params.TranslationUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "namespace": namespace,
                        "annotate": annotate,
                        "branch": branch,
                        "commit": commit,
                        "commit_message": commit_message,
                        "force": force,
                        "format": format,
                    },
                    translation_upsert_params.TranslationUpsertParams,
                ),
            ),
            cast_to=TranslationUpsertResponse,
        )

    def validate(
        self,
        locale_code: str,
        *,
        environment: str,
        translation: translation_validate_params.Translation,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationValidateResponse:
        """
        Validates a translation payload without persisting it.

        Note: this endpoint only operates on translations in the "development"
        environment.

        Args:
          environment: The environment slug.

          translation: A translation object with a content attribute used to update or create a
              translation.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not locale_code:
            raise ValueError(f"Expected a non-empty value for `locale_code` but received {locale_code!r}")
        return self._put(
            f"/v1/translations/{locale_code}/validate",
            body=maybe_transform({"translation": translation}, translation_validate_params.TranslationValidateParams),
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
                    translation_validate_params.TranslationValidateParams,
                ),
            ),
            cast_to=TranslationValidateResponse,
        )


class AsyncTranslationsResource(AsyncAPIResource):
    """Translations are per-locale string files that can be used in your templates."""

    @cached_property
    def with_raw_response(self) -> AsyncTranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncTranslationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        locale_code: str,
        *,
        environment: str,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        format: Literal["json", "po"] | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationRetrieveResponse:
        """
        Retrieve a translation by its locale and namespace, in a given environment.

        Args:
          environment: The environment slug.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          format: Optionally specify the returned content format. Supports 'json' and 'po'.
              Defaults to 'json'.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          namespace: A specific namespace to filter translations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not locale_code:
            raise ValueError(f"Expected a non-empty value for `locale_code` but received {locale_code!r}")
        return await self._get(
            f"/v1/translations/{locale_code}",
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
                        "format": format,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "namespace": namespace,
                    },
                    translation_retrieve_params.TranslationRetrieveParams,
                ),
            ),
            cast_to=TranslationRetrieveResponse,
        )

    def list(
        self,
        *,
        environment: str,
        after: str | Omit = omit,
        annotate: bool | Omit = omit,
        before: str | Omit = omit,
        branch: str | Omit = omit,
        format: Literal["json", "po"] | Omit = omit,
        hide_uncommitted_changes: bool | Omit = omit,
        limit: int | Omit = omit,
        locale_code: str | Omit = omit,
        namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Translation, AsyncEntriesCursor[Translation]]:
        """Returns a paginated list of translations available in a given environment.

        The
        translations are returned in alphabetical order by locale code.

        Args:
          environment: The environment slug.

          after: The cursor to fetch entries after.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          before: The cursor to fetch entries before.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          format: Optionally specify the returned content format. Supports 'json' and 'po'.
              Defaults to 'json'.

          hide_uncommitted_changes: Whether to hide uncommitted changes. When true, only committed changes will be
              returned. When false, both committed and uncommitted changes will be returned.

          limit: The number of entries to fetch per-page.

          locale_code: A specific locale code to filter translations for.

          namespace: A specific namespace to filter translations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/translations",
            page=AsyncEntriesCursor[Translation],
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
                        "format": format,
                        "hide_uncommitted_changes": hide_uncommitted_changes,
                        "limit": limit,
                        "locale_code": locale_code,
                        "namespace": namespace,
                    },
                    translation_list_params.TranslationListParams,
                ),
            ),
            model=Translation,
        )

    async def upsert(
        self,
        locale_code: str,
        *,
        environment: str,
        namespace: str,
        translation: translation_upsert_params.Translation,
        annotate: bool | Omit = omit,
        branch: str | Omit = omit,
        commit: bool | Omit = omit,
        commit_message: str | Omit = omit,
        force: bool | Omit = omit,
        format: Literal["json", "po"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationUpsertResponse:
        """
        Updates a translation of a given locale code + namespace, or creates a new one
        if it does not yet exist.

        Note: this endpoint only operates on translations in the "development"
        environment.

        Args:
          environment: The environment slug.

          namespace: An optional namespace that identifies the translation.

          translation: A translation object with a content attribute used to update or create a
              translation.

          annotate: Whether to annotate the resource. Only used in the Knock CLI.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          commit: Whether to commit the resource at the same time as modifying it.

          commit_message: The message to commit the resource with, only used if `commit` is `true`.

          force: When set to true, forces the upsert to override existing content regardless of
              environment restrictions. This bypasses the development-only environment check
              and origin environment checks.

          format: Optionally specify the returned content format. Supports 'json' and 'po'.
              Defaults to 'json'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not locale_code:
            raise ValueError(f"Expected a non-empty value for `locale_code` but received {locale_code!r}")
        return await self._put(
            f"/v1/translations/{locale_code}",
            body=await async_maybe_transform(
                {"translation": translation}, translation_upsert_params.TranslationUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "namespace": namespace,
                        "annotate": annotate,
                        "branch": branch,
                        "commit": commit,
                        "commit_message": commit_message,
                        "force": force,
                        "format": format,
                    },
                    translation_upsert_params.TranslationUpsertParams,
                ),
            ),
            cast_to=TranslationUpsertResponse,
        )

    async def validate(
        self,
        locale_code: str,
        *,
        environment: str,
        translation: translation_validate_params.Translation,
        branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationValidateResponse:
        """
        Validates a translation payload without persisting it.

        Note: this endpoint only operates on translations in the "development"
        environment.

        Args:
          environment: The environment slug.

          translation: A translation object with a content attribute used to update or create a
              translation.

          branch: The slug of a branch to use. This option can only be used when `environment` is
              `"development"`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not locale_code:
            raise ValueError(f"Expected a non-empty value for `locale_code` but received {locale_code!r}")
        return await self._put(
            f"/v1/translations/{locale_code}/validate",
            body=await async_maybe_transform(
                {"translation": translation}, translation_validate_params.TranslationValidateParams
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
                    translation_validate_params.TranslationValidateParams,
                ),
            ),
            cast_to=TranslationValidateResponse,
        )


class TranslationsResourceWithRawResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.retrieve = to_raw_response_wrapper(
            translations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            translations.list,
        )
        self.upsert = to_raw_response_wrapper(
            translations.upsert,
        )
        self.validate = to_raw_response_wrapper(
            translations.validate,
        )


class AsyncTranslationsResourceWithRawResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.retrieve = async_to_raw_response_wrapper(
            translations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            translations.list,
        )
        self.upsert = async_to_raw_response_wrapper(
            translations.upsert,
        )
        self.validate = async_to_raw_response_wrapper(
            translations.validate,
        )


class TranslationsResourceWithStreamingResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.retrieve = to_streamed_response_wrapper(
            translations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            translations.list,
        )
        self.upsert = to_streamed_response_wrapper(
            translations.upsert,
        )
        self.validate = to_streamed_response_wrapper(
            translations.validate,
        )


class AsyncTranslationsResourceWithStreamingResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.retrieve = async_to_streamed_response_wrapper(
            translations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            translations.list,
        )
        self.upsert = async_to_streamed_response_wrapper(
            translations.upsert,
        )
        self.validate = async_to_streamed_response_wrapper(
            translations.validate,
        )

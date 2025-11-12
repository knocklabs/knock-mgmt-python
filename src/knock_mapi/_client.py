# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    auth,
    guides,
    commits,
    api_keys,
    branches,
    channels,
    partials,
    variables,
    environments,
    translations,
    email_layouts,
    message_types,
    channel_groups,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, KnockMgmtError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.workflows import workflows

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "KnockMgmt",
    "AsyncKnockMgmt",
    "Client",
    "AsyncClient",
]


class KnockMgmt(SyncAPIClient):
    email_layouts: email_layouts.EmailLayoutsResource
    commits: commits.CommitsResource
    partials: partials.PartialsResource
    translations: translations.TranslationsResource
    workflows: workflows.WorkflowsResource
    message_types: message_types.MessageTypesResource
    auth: auth.AuthResource
    api_keys: api_keys.APIKeysResource
    channel_groups: channel_groups.ChannelGroupsResource
    channels: channels.ChannelsResource
    environments: environments.EnvironmentsResource
    variables: variables.VariablesResource
    guides: guides.GuidesResource
    branches: branches.BranchesResource
    with_raw_response: KnockMgmtWithRawResponse
    with_streaming_response: KnockMgmtWithStreamedResponse

    # client options
    service_token: str

    def __init__(
        self,
        *,
        service_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous KnockMgmt client instance.

        This automatically infers the `service_token` argument from the `KNOCK_SERVICE_TOKEN` environment variable if it is not provided.
        """
        if service_token is None:
            service_token = os.environ.get("KNOCK_SERVICE_TOKEN")
        if service_token is None:
            raise KnockMgmtError(
                "The service_token client option must be set either by passing service_token to the client or by setting the KNOCK_SERVICE_TOKEN environment variable"
            )
        self.service_token = service_token

        if base_url is None:
            base_url = os.environ.get("KNOCK_MGMT_BASE_URL")
        if base_url is None:
            base_url = f"https://control.knock.app"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.email_layouts = email_layouts.EmailLayoutsResource(self)
        self.commits = commits.CommitsResource(self)
        self.partials = partials.PartialsResource(self)
        self.translations = translations.TranslationsResource(self)
        self.workflows = workflows.WorkflowsResource(self)
        self.message_types = message_types.MessageTypesResource(self)
        self.auth = auth.AuthResource(self)
        self.api_keys = api_keys.APIKeysResource(self)
        self.channel_groups = channel_groups.ChannelGroupsResource(self)
        self.channels = channels.ChannelsResource(self)
        self.environments = environments.EnvironmentsResource(self)
        self.variables = variables.VariablesResource(self)
        self.guides = guides.GuidesResource(self)
        self.branches = branches.BranchesResource(self)
        self.with_raw_response = KnockMgmtWithRawResponse(self)
        self.with_streaming_response = KnockMgmtWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        service_token = self.service_token
        return {"Authorization": f"Bearer {service_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        service_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            service_token=service_token or self.service_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKnockMgmt(AsyncAPIClient):
    email_layouts: email_layouts.AsyncEmailLayoutsResource
    commits: commits.AsyncCommitsResource
    partials: partials.AsyncPartialsResource
    translations: translations.AsyncTranslationsResource
    workflows: workflows.AsyncWorkflowsResource
    message_types: message_types.AsyncMessageTypesResource
    auth: auth.AsyncAuthResource
    api_keys: api_keys.AsyncAPIKeysResource
    channel_groups: channel_groups.AsyncChannelGroupsResource
    channels: channels.AsyncChannelsResource
    environments: environments.AsyncEnvironmentsResource
    variables: variables.AsyncVariablesResource
    guides: guides.AsyncGuidesResource
    branches: branches.AsyncBranchesResource
    with_raw_response: AsyncKnockMgmtWithRawResponse
    with_streaming_response: AsyncKnockMgmtWithStreamedResponse

    # client options
    service_token: str

    def __init__(
        self,
        *,
        service_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKnockMgmt client instance.

        This automatically infers the `service_token` argument from the `KNOCK_SERVICE_TOKEN` environment variable if it is not provided.
        """
        if service_token is None:
            service_token = os.environ.get("KNOCK_SERVICE_TOKEN")
        if service_token is None:
            raise KnockMgmtError(
                "The service_token client option must be set either by passing service_token to the client or by setting the KNOCK_SERVICE_TOKEN environment variable"
            )
        self.service_token = service_token

        if base_url is None:
            base_url = os.environ.get("KNOCK_MGMT_BASE_URL")
        if base_url is None:
            base_url = f"https://control.knock.app"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.email_layouts = email_layouts.AsyncEmailLayoutsResource(self)
        self.commits = commits.AsyncCommitsResource(self)
        self.partials = partials.AsyncPartialsResource(self)
        self.translations = translations.AsyncTranslationsResource(self)
        self.workflows = workflows.AsyncWorkflowsResource(self)
        self.message_types = message_types.AsyncMessageTypesResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.api_keys = api_keys.AsyncAPIKeysResource(self)
        self.channel_groups = channel_groups.AsyncChannelGroupsResource(self)
        self.channels = channels.AsyncChannelsResource(self)
        self.environments = environments.AsyncEnvironmentsResource(self)
        self.variables = variables.AsyncVariablesResource(self)
        self.guides = guides.AsyncGuidesResource(self)
        self.branches = branches.AsyncBranchesResource(self)
        self.with_raw_response = AsyncKnockMgmtWithRawResponse(self)
        self.with_streaming_response = AsyncKnockMgmtWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        service_token = self.service_token
        return {"Authorization": f"Bearer {service_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        service_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            service_token=service_token or self.service_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KnockMgmtWithRawResponse:
    def __init__(self, client: KnockMgmt) -> None:
        self.email_layouts = email_layouts.EmailLayoutsResourceWithRawResponse(client.email_layouts)
        self.commits = commits.CommitsResourceWithRawResponse(client.commits)
        self.partials = partials.PartialsResourceWithRawResponse(client.partials)
        self.translations = translations.TranslationsResourceWithRawResponse(client.translations)
        self.workflows = workflows.WorkflowsResourceWithRawResponse(client.workflows)
        self.message_types = message_types.MessageTypesResourceWithRawResponse(client.message_types)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)
        self.channel_groups = channel_groups.ChannelGroupsResourceWithRawResponse(client.channel_groups)
        self.channels = channels.ChannelsResourceWithRawResponse(client.channels)
        self.environments = environments.EnvironmentsResourceWithRawResponse(client.environments)
        self.variables = variables.VariablesResourceWithRawResponse(client.variables)
        self.guides = guides.GuidesResourceWithRawResponse(client.guides)
        self.branches = branches.BranchesResourceWithRawResponse(client.branches)


class AsyncKnockMgmtWithRawResponse:
    def __init__(self, client: AsyncKnockMgmt) -> None:
        self.email_layouts = email_layouts.AsyncEmailLayoutsResourceWithRawResponse(client.email_layouts)
        self.commits = commits.AsyncCommitsResourceWithRawResponse(client.commits)
        self.partials = partials.AsyncPartialsResourceWithRawResponse(client.partials)
        self.translations = translations.AsyncTranslationsResourceWithRawResponse(client.translations)
        self.workflows = workflows.AsyncWorkflowsResourceWithRawResponse(client.workflows)
        self.message_types = message_types.AsyncMessageTypesResourceWithRawResponse(client.message_types)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.channel_groups = channel_groups.AsyncChannelGroupsResourceWithRawResponse(client.channel_groups)
        self.channels = channels.AsyncChannelsResourceWithRawResponse(client.channels)
        self.environments = environments.AsyncEnvironmentsResourceWithRawResponse(client.environments)
        self.variables = variables.AsyncVariablesResourceWithRawResponse(client.variables)
        self.guides = guides.AsyncGuidesResourceWithRawResponse(client.guides)
        self.branches = branches.AsyncBranchesResourceWithRawResponse(client.branches)


class KnockMgmtWithStreamedResponse:
    def __init__(self, client: KnockMgmt) -> None:
        self.email_layouts = email_layouts.EmailLayoutsResourceWithStreamingResponse(client.email_layouts)
        self.commits = commits.CommitsResourceWithStreamingResponse(client.commits)
        self.partials = partials.PartialsResourceWithStreamingResponse(client.partials)
        self.translations = translations.TranslationsResourceWithStreamingResponse(client.translations)
        self.workflows = workflows.WorkflowsResourceWithStreamingResponse(client.workflows)
        self.message_types = message_types.MessageTypesResourceWithStreamingResponse(client.message_types)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.channel_groups = channel_groups.ChannelGroupsResourceWithStreamingResponse(client.channel_groups)
        self.channels = channels.ChannelsResourceWithStreamingResponse(client.channels)
        self.environments = environments.EnvironmentsResourceWithStreamingResponse(client.environments)
        self.variables = variables.VariablesResourceWithStreamingResponse(client.variables)
        self.guides = guides.GuidesResourceWithStreamingResponse(client.guides)
        self.branches = branches.BranchesResourceWithStreamingResponse(client.branches)


class AsyncKnockMgmtWithStreamedResponse:
    def __init__(self, client: AsyncKnockMgmt) -> None:
        self.email_layouts = email_layouts.AsyncEmailLayoutsResourceWithStreamingResponse(client.email_layouts)
        self.commits = commits.AsyncCommitsResourceWithStreamingResponse(client.commits)
        self.partials = partials.AsyncPartialsResourceWithStreamingResponse(client.partials)
        self.translations = translations.AsyncTranslationsResourceWithStreamingResponse(client.translations)
        self.workflows = workflows.AsyncWorkflowsResourceWithStreamingResponse(client.workflows)
        self.message_types = message_types.AsyncMessageTypesResourceWithStreamingResponse(client.message_types)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.channel_groups = channel_groups.AsyncChannelGroupsResourceWithStreamingResponse(client.channel_groups)
        self.channels = channels.AsyncChannelsResourceWithStreamingResponse(client.channels)
        self.environments = environments.AsyncEnvironmentsResourceWithStreamingResponse(client.environments)
        self.variables = variables.AsyncVariablesResourceWithStreamingResponse(client.variables)
        self.guides = guides.AsyncGuidesResourceWithStreamingResponse(client.guides)
        self.branches = branches.AsyncBranchesResourceWithStreamingResponse(client.branches)


Client = KnockMgmt

AsyncClient = AsyncKnockMgmt

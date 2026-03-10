# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, KnockMgmtError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        auth,
        guides,
        commits,
        members,
        api_keys,
        branches,
        channels,
        partials,
        audiences,
        variables,
        workflows,
        broadcasts,
        environments,
        translations,
        email_layouts,
        message_types,
        channel_groups,
    )
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.guides import GuidesResource, AsyncGuidesResource
    from .resources.commits import CommitsResource, AsyncCommitsResource
    from .resources.members import MembersResource, AsyncMembersResource
    from .resources.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.branches import BranchesResource, AsyncBranchesResource
    from .resources.channels import ChannelsResource, AsyncChannelsResource
    from .resources.partials import PartialsResource, AsyncPartialsResource
    from .resources.audiences import AudiencesResource, AsyncAudiencesResource
    from .resources.variables import VariablesResource, AsyncVariablesResource
    from .resources.broadcasts import BroadcastsResource, AsyncBroadcastsResource
    from .resources.environments import EnvironmentsResource, AsyncEnvironmentsResource
    from .resources.translations import TranslationsResource, AsyncTranslationsResource
    from .resources.email_layouts import EmailLayoutsResource, AsyncEmailLayoutsResource
    from .resources.message_types import MessageTypesResource, AsyncMessageTypesResource
    from .resources.channel_groups import ChannelGroupsResource, AsyncChannelGroupsResource
    from .resources.workflows.workflows import WorkflowsResource, AsyncWorkflowsResource

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

    @cached_property
    def email_layouts(self) -> EmailLayoutsResource:
        """Email layouts wrap your email templates and provide a consistent look and feel."""
        from .resources.email_layouts import EmailLayoutsResource

        return EmailLayoutsResource(self)

    @cached_property
    def commits(self) -> CommitsResource:
        """Commits are versioned changes to resources."""
        from .resources.commits import CommitsResource

        return CommitsResource(self)

    @cached_property
    def partials(self) -> PartialsResource:
        """Partials allow you to reuse content across templates."""
        from .resources.partials import PartialsResource

        return PartialsResource(self)

    @cached_property
    def translations(self) -> TranslationsResource:
        """Translations are per-locale string files that can be used in your templates."""
        from .resources.translations import TranslationsResource

        return TranslationsResource(self)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        """Workflows let you express your cross-channel notification logic."""
        from .resources.workflows import WorkflowsResource

        return WorkflowsResource(self)

    @cached_property
    def message_types(self) -> MessageTypesResource:
        """
        A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
        """
        from .resources.message_types import MessageTypesResource

        return MessageTypesResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        """Resources for managing your Knock account."""
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def channel_groups(self) -> ChannelGroupsResource:
        from .resources.channel_groups import ChannelGroupsResource

        return ChannelGroupsResource(self)

    @cached_property
    def channels(self) -> ChannelsResource:
        from .resources.channels import ChannelsResource

        return ChannelsResource(self)

    @cached_property
    def members(self) -> MembersResource:
        from .resources.members import MembersResource

        return MembersResource(self)

    @cached_property
    def environments(self) -> EnvironmentsResource:
        """
        Environments are isolated instances of your account that map to your infrastructure.
        """
        from .resources.environments import EnvironmentsResource

        return EnvironmentsResource(self)

    @cached_property
    def variables(self) -> VariablesResource:
        from .resources.variables import VariablesResource

        return VariablesResource(self)

    @cached_property
    def guides(self) -> GuidesResource:
        """
        Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
        """
        from .resources.guides import GuidesResource

        return GuidesResource(self)

    @cached_property
    def branches(self) -> BranchesResource:
        """Branches in Knock are a way to isolate changes to your Knock resources."""
        from .resources.branches import BranchesResource

        return BranchesResource(self)

    @cached_property
    def broadcasts(self) -> BroadcastsResource:
        from .resources.broadcasts import BroadcastsResource

        return BroadcastsResource(self)

    @cached_property
    def audiences(self) -> AudiencesResource:
        """Audiences define sets of users that can be targeted for notifications."""
        from .resources.audiences import AudiencesResource

        return AudiencesResource(self)

    @cached_property
    def with_raw_response(self) -> KnockMgmtWithRawResponse:
        return KnockMgmtWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnockMgmtWithStreamedResponse:
        return KnockMgmtWithStreamedResponse(self)

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

    @cached_property
    def email_layouts(self) -> AsyncEmailLayoutsResource:
        """Email layouts wrap your email templates and provide a consistent look and feel."""
        from .resources.email_layouts import AsyncEmailLayoutsResource

        return AsyncEmailLayoutsResource(self)

    @cached_property
    def commits(self) -> AsyncCommitsResource:
        """Commits are versioned changes to resources."""
        from .resources.commits import AsyncCommitsResource

        return AsyncCommitsResource(self)

    @cached_property
    def partials(self) -> AsyncPartialsResource:
        """Partials allow you to reuse content across templates."""
        from .resources.partials import AsyncPartialsResource

        return AsyncPartialsResource(self)

    @cached_property
    def translations(self) -> AsyncTranslationsResource:
        """Translations are per-locale string files that can be used in your templates."""
        from .resources.translations import AsyncTranslationsResource

        return AsyncTranslationsResource(self)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        """Workflows let you express your cross-channel notification logic."""
        from .resources.workflows import AsyncWorkflowsResource

        return AsyncWorkflowsResource(self)

    @cached_property
    def message_types(self) -> AsyncMessageTypesResource:
        """
        A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
        """
        from .resources.message_types import AsyncMessageTypesResource

        return AsyncMessageTypesResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """Resources for managing your Knock account."""
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def channel_groups(self) -> AsyncChannelGroupsResource:
        from .resources.channel_groups import AsyncChannelGroupsResource

        return AsyncChannelGroupsResource(self)

    @cached_property
    def channels(self) -> AsyncChannelsResource:
        from .resources.channels import AsyncChannelsResource

        return AsyncChannelsResource(self)

    @cached_property
    def members(self) -> AsyncMembersResource:
        from .resources.members import AsyncMembersResource

        return AsyncMembersResource(self)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResource:
        """
        Environments are isolated instances of your account that map to your infrastructure.
        """
        from .resources.environments import AsyncEnvironmentsResource

        return AsyncEnvironmentsResource(self)

    @cached_property
    def variables(self) -> AsyncVariablesResource:
        from .resources.variables import AsyncVariablesResource

        return AsyncVariablesResource(self)

    @cached_property
    def guides(self) -> AsyncGuidesResource:
        """
        Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
        """
        from .resources.guides import AsyncGuidesResource

        return AsyncGuidesResource(self)

    @cached_property
    def branches(self) -> AsyncBranchesResource:
        """Branches in Knock are a way to isolate changes to your Knock resources."""
        from .resources.branches import AsyncBranchesResource

        return AsyncBranchesResource(self)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResource:
        from .resources.broadcasts import AsyncBroadcastsResource

        return AsyncBroadcastsResource(self)

    @cached_property
    def audiences(self) -> AsyncAudiencesResource:
        """Audiences define sets of users that can be targeted for notifications."""
        from .resources.audiences import AsyncAudiencesResource

        return AsyncAudiencesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKnockMgmtWithRawResponse:
        return AsyncKnockMgmtWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnockMgmtWithStreamedResponse:
        return AsyncKnockMgmtWithStreamedResponse(self)

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
    _client: KnockMgmt

    def __init__(self, client: KnockMgmt) -> None:
        self._client = client

    @cached_property
    def email_layouts(self) -> email_layouts.EmailLayoutsResourceWithRawResponse:
        """Email layouts wrap your email templates and provide a consistent look and feel."""
        from .resources.email_layouts import EmailLayoutsResourceWithRawResponse

        return EmailLayoutsResourceWithRawResponse(self._client.email_layouts)

    @cached_property
    def commits(self) -> commits.CommitsResourceWithRawResponse:
        """Commits are versioned changes to resources."""
        from .resources.commits import CommitsResourceWithRawResponse

        return CommitsResourceWithRawResponse(self._client.commits)

    @cached_property
    def partials(self) -> partials.PartialsResourceWithRawResponse:
        """Partials allow you to reuse content across templates."""
        from .resources.partials import PartialsResourceWithRawResponse

        return PartialsResourceWithRawResponse(self._client.partials)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithRawResponse:
        """Translations are per-locale string files that can be used in your templates."""
        from .resources.translations import TranslationsResourceWithRawResponse

        return TranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithRawResponse:
        """Workflows let you express your cross-channel notification logic."""
        from .resources.workflows import WorkflowsResourceWithRawResponse

        return WorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def message_types(self) -> message_types.MessageTypesResourceWithRawResponse:
        """
        A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
        """
        from .resources.message_types import MessageTypesResourceWithRawResponse

        return MessageTypesResourceWithRawResponse(self._client.message_types)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        """Resources for managing your Knock account."""
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def channel_groups(self) -> channel_groups.ChannelGroupsResourceWithRawResponse:
        from .resources.channel_groups import ChannelGroupsResourceWithRawResponse

        return ChannelGroupsResourceWithRawResponse(self._client.channel_groups)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithRawResponse:
        from .resources.channels import ChannelsResourceWithRawResponse

        return ChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def members(self) -> members.MembersResourceWithRawResponse:
        from .resources.members import MembersResourceWithRawResponse

        return MembersResourceWithRawResponse(self._client.members)

    @cached_property
    def environments(self) -> environments.EnvironmentsResourceWithRawResponse:
        """
        Environments are isolated instances of your account that map to your infrastructure.
        """
        from .resources.environments import EnvironmentsResourceWithRawResponse

        return EnvironmentsResourceWithRawResponse(self._client.environments)

    @cached_property
    def variables(self) -> variables.VariablesResourceWithRawResponse:
        from .resources.variables import VariablesResourceWithRawResponse

        return VariablesResourceWithRawResponse(self._client.variables)

    @cached_property
    def guides(self) -> guides.GuidesResourceWithRawResponse:
        """
        Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
        """
        from .resources.guides import GuidesResourceWithRawResponse

        return GuidesResourceWithRawResponse(self._client.guides)

    @cached_property
    def branches(self) -> branches.BranchesResourceWithRawResponse:
        """Branches in Knock are a way to isolate changes to your Knock resources."""
        from .resources.branches import BranchesResourceWithRawResponse

        return BranchesResourceWithRawResponse(self._client.branches)

    @cached_property
    def broadcasts(self) -> broadcasts.BroadcastsResourceWithRawResponse:
        from .resources.broadcasts import BroadcastsResourceWithRawResponse

        return BroadcastsResourceWithRawResponse(self._client.broadcasts)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithRawResponse:
        """Audiences define sets of users that can be targeted for notifications."""
        from .resources.audiences import AudiencesResourceWithRawResponse

        return AudiencesResourceWithRawResponse(self._client.audiences)


class AsyncKnockMgmtWithRawResponse:
    _client: AsyncKnockMgmt

    def __init__(self, client: AsyncKnockMgmt) -> None:
        self._client = client

    @cached_property
    def email_layouts(self) -> email_layouts.AsyncEmailLayoutsResourceWithRawResponse:
        """Email layouts wrap your email templates and provide a consistent look and feel."""
        from .resources.email_layouts import AsyncEmailLayoutsResourceWithRawResponse

        return AsyncEmailLayoutsResourceWithRawResponse(self._client.email_layouts)

    @cached_property
    def commits(self) -> commits.AsyncCommitsResourceWithRawResponse:
        """Commits are versioned changes to resources."""
        from .resources.commits import AsyncCommitsResourceWithRawResponse

        return AsyncCommitsResourceWithRawResponse(self._client.commits)

    @cached_property
    def partials(self) -> partials.AsyncPartialsResourceWithRawResponse:
        """Partials allow you to reuse content across templates."""
        from .resources.partials import AsyncPartialsResourceWithRawResponse

        return AsyncPartialsResourceWithRawResponse(self._client.partials)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithRawResponse:
        """Translations are per-locale string files that can be used in your templates."""
        from .resources.translations import AsyncTranslationsResourceWithRawResponse

        return AsyncTranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithRawResponse:
        """Workflows let you express your cross-channel notification logic."""
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse

        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def message_types(self) -> message_types.AsyncMessageTypesResourceWithRawResponse:
        """
        A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
        """
        from .resources.message_types import AsyncMessageTypesResourceWithRawResponse

        return AsyncMessageTypesResourceWithRawResponse(self._client.message_types)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        """Resources for managing your Knock account."""
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def channel_groups(self) -> channel_groups.AsyncChannelGroupsResourceWithRawResponse:
        from .resources.channel_groups import AsyncChannelGroupsResourceWithRawResponse

        return AsyncChannelGroupsResourceWithRawResponse(self._client.channel_groups)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithRawResponse:
        from .resources.channels import AsyncChannelsResourceWithRawResponse

        return AsyncChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithRawResponse:
        from .resources.members import AsyncMembersResourceWithRawResponse

        return AsyncMembersResourceWithRawResponse(self._client.members)

    @cached_property
    def environments(self) -> environments.AsyncEnvironmentsResourceWithRawResponse:
        """
        Environments are isolated instances of your account that map to your infrastructure.
        """
        from .resources.environments import AsyncEnvironmentsResourceWithRawResponse

        return AsyncEnvironmentsResourceWithRawResponse(self._client.environments)

    @cached_property
    def variables(self) -> variables.AsyncVariablesResourceWithRawResponse:
        from .resources.variables import AsyncVariablesResourceWithRawResponse

        return AsyncVariablesResourceWithRawResponse(self._client.variables)

    @cached_property
    def guides(self) -> guides.AsyncGuidesResourceWithRawResponse:
        """
        Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
        """
        from .resources.guides import AsyncGuidesResourceWithRawResponse

        return AsyncGuidesResourceWithRawResponse(self._client.guides)

    @cached_property
    def branches(self) -> branches.AsyncBranchesResourceWithRawResponse:
        """Branches in Knock are a way to isolate changes to your Knock resources."""
        from .resources.branches import AsyncBranchesResourceWithRawResponse

        return AsyncBranchesResourceWithRawResponse(self._client.branches)

    @cached_property
    def broadcasts(self) -> broadcasts.AsyncBroadcastsResourceWithRawResponse:
        from .resources.broadcasts import AsyncBroadcastsResourceWithRawResponse

        return AsyncBroadcastsResourceWithRawResponse(self._client.broadcasts)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithRawResponse:
        """Audiences define sets of users that can be targeted for notifications."""
        from .resources.audiences import AsyncAudiencesResourceWithRawResponse

        return AsyncAudiencesResourceWithRawResponse(self._client.audiences)


class KnockMgmtWithStreamedResponse:
    _client: KnockMgmt

    def __init__(self, client: KnockMgmt) -> None:
        self._client = client

    @cached_property
    def email_layouts(self) -> email_layouts.EmailLayoutsResourceWithStreamingResponse:
        """Email layouts wrap your email templates and provide a consistent look and feel."""
        from .resources.email_layouts import EmailLayoutsResourceWithStreamingResponse

        return EmailLayoutsResourceWithStreamingResponse(self._client.email_layouts)

    @cached_property
    def commits(self) -> commits.CommitsResourceWithStreamingResponse:
        """Commits are versioned changes to resources."""
        from .resources.commits import CommitsResourceWithStreamingResponse

        return CommitsResourceWithStreamingResponse(self._client.commits)

    @cached_property
    def partials(self) -> partials.PartialsResourceWithStreamingResponse:
        """Partials allow you to reuse content across templates."""
        from .resources.partials import PartialsResourceWithStreamingResponse

        return PartialsResourceWithStreamingResponse(self._client.partials)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithStreamingResponse:
        """Translations are per-locale string files that can be used in your templates."""
        from .resources.translations import TranslationsResourceWithStreamingResponse

        return TranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithStreamingResponse:
        """Workflows let you express your cross-channel notification logic."""
        from .resources.workflows import WorkflowsResourceWithStreamingResponse

        return WorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def message_types(self) -> message_types.MessageTypesResourceWithStreamingResponse:
        """
        A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
        """
        from .resources.message_types import MessageTypesResourceWithStreamingResponse

        return MessageTypesResourceWithStreamingResponse(self._client.message_types)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        """Resources for managing your Knock account."""
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def channel_groups(self) -> channel_groups.ChannelGroupsResourceWithStreamingResponse:
        from .resources.channel_groups import ChannelGroupsResourceWithStreamingResponse

        return ChannelGroupsResourceWithStreamingResponse(self._client.channel_groups)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithStreamingResponse:
        from .resources.channels import ChannelsResourceWithStreamingResponse

        return ChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def members(self) -> members.MembersResourceWithStreamingResponse:
        from .resources.members import MembersResourceWithStreamingResponse

        return MembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def environments(self) -> environments.EnvironmentsResourceWithStreamingResponse:
        """
        Environments are isolated instances of your account that map to your infrastructure.
        """
        from .resources.environments import EnvironmentsResourceWithStreamingResponse

        return EnvironmentsResourceWithStreamingResponse(self._client.environments)

    @cached_property
    def variables(self) -> variables.VariablesResourceWithStreamingResponse:
        from .resources.variables import VariablesResourceWithStreamingResponse

        return VariablesResourceWithStreamingResponse(self._client.variables)

    @cached_property
    def guides(self) -> guides.GuidesResourceWithStreamingResponse:
        """
        Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
        """
        from .resources.guides import GuidesResourceWithStreamingResponse

        return GuidesResourceWithStreamingResponse(self._client.guides)

    @cached_property
    def branches(self) -> branches.BranchesResourceWithStreamingResponse:
        """Branches in Knock are a way to isolate changes to your Knock resources."""
        from .resources.branches import BranchesResourceWithStreamingResponse

        return BranchesResourceWithStreamingResponse(self._client.branches)

    @cached_property
    def broadcasts(self) -> broadcasts.BroadcastsResourceWithStreamingResponse:
        from .resources.broadcasts import BroadcastsResourceWithStreamingResponse

        return BroadcastsResourceWithStreamingResponse(self._client.broadcasts)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithStreamingResponse:
        """Audiences define sets of users that can be targeted for notifications."""
        from .resources.audiences import AudiencesResourceWithStreamingResponse

        return AudiencesResourceWithStreamingResponse(self._client.audiences)


class AsyncKnockMgmtWithStreamedResponse:
    _client: AsyncKnockMgmt

    def __init__(self, client: AsyncKnockMgmt) -> None:
        self._client = client

    @cached_property
    def email_layouts(self) -> email_layouts.AsyncEmailLayoutsResourceWithStreamingResponse:
        """Email layouts wrap your email templates and provide a consistent look and feel."""
        from .resources.email_layouts import AsyncEmailLayoutsResourceWithStreamingResponse

        return AsyncEmailLayoutsResourceWithStreamingResponse(self._client.email_layouts)

    @cached_property
    def commits(self) -> commits.AsyncCommitsResourceWithStreamingResponse:
        """Commits are versioned changes to resources."""
        from .resources.commits import AsyncCommitsResourceWithStreamingResponse

        return AsyncCommitsResourceWithStreamingResponse(self._client.commits)

    @cached_property
    def partials(self) -> partials.AsyncPartialsResourceWithStreamingResponse:
        """Partials allow you to reuse content across templates."""
        from .resources.partials import AsyncPartialsResourceWithStreamingResponse

        return AsyncPartialsResourceWithStreamingResponse(self._client.partials)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithStreamingResponse:
        """Translations are per-locale string files that can be used in your templates."""
        from .resources.translations import AsyncTranslationsResourceWithStreamingResponse

        return AsyncTranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithStreamingResponse:
        """Workflows let you express your cross-channel notification logic."""
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse

        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def message_types(self) -> message_types.AsyncMessageTypesResourceWithStreamingResponse:
        """
        A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
        """
        from .resources.message_types import AsyncMessageTypesResourceWithStreamingResponse

        return AsyncMessageTypesResourceWithStreamingResponse(self._client.message_types)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        """Resources for managing your Knock account."""
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def channel_groups(self) -> channel_groups.AsyncChannelGroupsResourceWithStreamingResponse:
        from .resources.channel_groups import AsyncChannelGroupsResourceWithStreamingResponse

        return AsyncChannelGroupsResourceWithStreamingResponse(self._client.channel_groups)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithStreamingResponse:
        from .resources.channels import AsyncChannelsResourceWithStreamingResponse

        return AsyncChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithStreamingResponse:
        from .resources.members import AsyncMembersResourceWithStreamingResponse

        return AsyncMembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def environments(self) -> environments.AsyncEnvironmentsResourceWithStreamingResponse:
        """
        Environments are isolated instances of your account that map to your infrastructure.
        """
        from .resources.environments import AsyncEnvironmentsResourceWithStreamingResponse

        return AsyncEnvironmentsResourceWithStreamingResponse(self._client.environments)

    @cached_property
    def variables(self) -> variables.AsyncVariablesResourceWithStreamingResponse:
        from .resources.variables import AsyncVariablesResourceWithStreamingResponse

        return AsyncVariablesResourceWithStreamingResponse(self._client.variables)

    @cached_property
    def guides(self) -> guides.AsyncGuidesResourceWithStreamingResponse:
        """
        Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
        """
        from .resources.guides import AsyncGuidesResourceWithStreamingResponse

        return AsyncGuidesResourceWithStreamingResponse(self._client.guides)

    @cached_property
    def branches(self) -> branches.AsyncBranchesResourceWithStreamingResponse:
        """Branches in Knock are a way to isolate changes to your Knock resources."""
        from .resources.branches import AsyncBranchesResourceWithStreamingResponse

        return AsyncBranchesResourceWithStreamingResponse(self._client.branches)

    @cached_property
    def broadcasts(self) -> broadcasts.AsyncBroadcastsResourceWithStreamingResponse:
        from .resources.broadcasts import AsyncBroadcastsResourceWithStreamingResponse

        return AsyncBroadcastsResourceWithStreamingResponse(self._client.broadcasts)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithStreamingResponse:
        """Audiences define sets of users that can be targeted for notifications."""
        from .resources.audiences import AsyncAudiencesResourceWithStreamingResponse

        return AsyncAudiencesResourceWithStreamingResponse(self._client.audiences)


Client = KnockMgmt

AsyncClient = AsyncKnockMgmt

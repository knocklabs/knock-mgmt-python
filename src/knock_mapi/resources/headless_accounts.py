# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import headless_account_claim_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.headless_account_claim_response import HeadlessAccountClaimResponse
from ..types.headless_account_create_response import HeadlessAccountCreateResponse
from ..types.headless_account_retrieve_status_response import HeadlessAccountRetrieveStatusResponse

__all__ = ["HeadlessAccountsResource", "AsyncHeadlessAccountsResource"]


class HeadlessAccountsResource(SyncAPIResource):
    """
    Headless accounts let an agent create a Knock account on its own and hand it to a person to claim.
    """

    @cached_property
    def with_raw_response(self) -> HeadlessAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return HeadlessAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeadlessAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return HeadlessAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeadlessAccountCreateResponse:
        """
        Creates an account that has no owner yet, and returns a service token the agent
        uses to work in it. The account is deleted after 24 hours unless a person claims
        it. This endpoint needs no authentication and is rate limited.
        """
        return self._post(
            "/v1/headless_accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeadlessAccountCreateResponse,
        )

    def claim(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeadlessAccountClaimResponse:
        """Starts handing the account to a person.

        Returns a link and a six-digit code for
        the agent to show that person. They open the link, sign in with the email given
        here, and type the code to become the account's owner. The service token keeps
        working afterwards. Starting a new claim replaces the previous link and code.

        Args:
          email: The email of the person who will own the account. Only they can finish the
              claim.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/headless_accounts/claim",
            body=maybe_transform({"email": email}, headless_account_claim_params.HeadlessAccountClaimParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeadlessAccountClaimResponse,
        )

    def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeadlessAccountRetrieveStatusResponse:
        """
        Returns whether the headless account is still being set up, waiting to be
        claimed, claimed by a person, or past its claim window. Agents poll this
        endpoint to find out when a person has claimed the account.
        """
        return self._get(
            "/v1/headless_accounts/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeadlessAccountRetrieveStatusResponse,
        )


class AsyncHeadlessAccountsResource(AsyncAPIResource):
    """
    Headless accounts let an agent create a Knock account on its own and hand it to a person to claim.
    """

    @cached_property
    def with_raw_response(self) -> AsyncHeadlessAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHeadlessAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeadlessAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-mgmt-python#with_streaming_response
        """
        return AsyncHeadlessAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeadlessAccountCreateResponse:
        """
        Creates an account that has no owner yet, and returns a service token the agent
        uses to work in it. The account is deleted after 24 hours unless a person claims
        it. This endpoint needs no authentication and is rate limited.
        """
        return await self._post(
            "/v1/headless_accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeadlessAccountCreateResponse,
        )

    async def claim(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeadlessAccountClaimResponse:
        """Starts handing the account to a person.

        Returns a link and a six-digit code for
        the agent to show that person. They open the link, sign in with the email given
        here, and type the code to become the account's owner. The service token keeps
        working afterwards. Starting a new claim replaces the previous link and code.

        Args:
          email: The email of the person who will own the account. Only they can finish the
              claim.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/headless_accounts/claim",
            body=await async_maybe_transform(
                {"email": email}, headless_account_claim_params.HeadlessAccountClaimParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeadlessAccountClaimResponse,
        )

    async def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeadlessAccountRetrieveStatusResponse:
        """
        Returns whether the headless account is still being set up, waiting to be
        claimed, claimed by a person, or past its claim window. Agents poll this
        endpoint to find out when a person has claimed the account.
        """
        return await self._get(
            "/v1/headless_accounts/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeadlessAccountRetrieveStatusResponse,
        )


class HeadlessAccountsResourceWithRawResponse:
    def __init__(self, headless_accounts: HeadlessAccountsResource) -> None:
        self._headless_accounts = headless_accounts

        self.create = to_raw_response_wrapper(
            headless_accounts.create,
        )
        self.claim = to_raw_response_wrapper(
            headless_accounts.claim,
        )
        self.retrieve_status = to_raw_response_wrapper(
            headless_accounts.retrieve_status,
        )


class AsyncHeadlessAccountsResourceWithRawResponse:
    def __init__(self, headless_accounts: AsyncHeadlessAccountsResource) -> None:
        self._headless_accounts = headless_accounts

        self.create = async_to_raw_response_wrapper(
            headless_accounts.create,
        )
        self.claim = async_to_raw_response_wrapper(
            headless_accounts.claim,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            headless_accounts.retrieve_status,
        )


class HeadlessAccountsResourceWithStreamingResponse:
    def __init__(self, headless_accounts: HeadlessAccountsResource) -> None:
        self._headless_accounts = headless_accounts

        self.create = to_streamed_response_wrapper(
            headless_accounts.create,
        )
        self.claim = to_streamed_response_wrapper(
            headless_accounts.claim,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            headless_accounts.retrieve_status,
        )


class AsyncHeadlessAccountsResourceWithStreamingResponse:
    def __init__(self, headless_accounts: AsyncHeadlessAccountsResource) -> None:
        self._headless_accounts = headless_accounts

        self.create = async_to_streamed_response_wrapper(
            headless_accounts.create,
        )
        self.claim = async_to_streamed_response_wrapper(
            headless_accounts.claim,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            headless_accounts.retrieve_status,
        )

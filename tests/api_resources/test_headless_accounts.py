# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    HeadlessAccountClaimResponse,
    HeadlessAccountCreateResponse,
    HeadlessAccountRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHeadlessAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: KnockMgmt) -> None:
        headless_account = client.headless_accounts.create()
        assert_matches_type(HeadlessAccountCreateResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KnockMgmt) -> None:
        response = client.headless_accounts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        headless_account = response.parse()
        assert_matches_type(HeadlessAccountCreateResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KnockMgmt) -> None:
        with client.headless_accounts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            headless_account = response.parse()
            assert_matches_type(HeadlessAccountCreateResponse, headless_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_claim(self, client: KnockMgmt) -> None:
        headless_account = client.headless_accounts.claim(
            email="founder@example.com",
        )
        assert_matches_type(HeadlessAccountClaimResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_claim(self, client: KnockMgmt) -> None:
        response = client.headless_accounts.with_raw_response.claim(
            email="founder@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        headless_account = response.parse()
        assert_matches_type(HeadlessAccountClaimResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_claim(self, client: KnockMgmt) -> None:
        with client.headless_accounts.with_streaming_response.claim(
            email="founder@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            headless_account = response.parse()
            assert_matches_type(HeadlessAccountClaimResponse, headless_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: KnockMgmt) -> None:
        headless_account = client.headless_accounts.retrieve_status()
        assert_matches_type(HeadlessAccountRetrieveStatusResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: KnockMgmt) -> None:
        response = client.headless_accounts.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        headless_account = response.parse()
        assert_matches_type(HeadlessAccountRetrieveStatusResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: KnockMgmt) -> None:
        with client.headless_accounts.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            headless_account = response.parse()
            assert_matches_type(HeadlessAccountRetrieveStatusResponse, headless_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHeadlessAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKnockMgmt) -> None:
        headless_account = await async_client.headless_accounts.create()
        assert_matches_type(HeadlessAccountCreateResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.headless_accounts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        headless_account = await response.parse()
        assert_matches_type(HeadlessAccountCreateResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.headless_accounts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            headless_account = await response.parse()
            assert_matches_type(HeadlessAccountCreateResponse, headless_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_claim(self, async_client: AsyncKnockMgmt) -> None:
        headless_account = await async_client.headless_accounts.claim(
            email="founder@example.com",
        )
        assert_matches_type(HeadlessAccountClaimResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_claim(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.headless_accounts.with_raw_response.claim(
            email="founder@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        headless_account = await response.parse()
        assert_matches_type(HeadlessAccountClaimResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_claim(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.headless_accounts.with_streaming_response.claim(
            email="founder@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            headless_account = await response.parse()
            assert_matches_type(HeadlessAccountClaimResponse, headless_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        headless_account = await async_client.headless_accounts.retrieve_status()
        assert_matches_type(HeadlessAccountRetrieveStatusResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.headless_accounts.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        headless_account = await response.parse()
        assert_matches_type(HeadlessAccountRetrieveStatusResponse, headless_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.headless_accounts.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            headless_account = await response.parse()
            assert_matches_type(HeadlessAccountRetrieveStatusResponse, headless_account, path=["response"])

        assert cast(Any, response.is_closed) is True

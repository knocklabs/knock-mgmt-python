# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import APIKeyExchangeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_exchange(self, client: KnockMgmt) -> None:
        api_key = client.api_keys.exchange(
            environment="development",
        )
        assert_matches_type(APIKeyExchangeResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_exchange(self, client: KnockMgmt) -> None:
        response = client.api_keys.with_raw_response.exchange(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyExchangeResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_exchange(self, client: KnockMgmt) -> None:
        with client.api_keys.with_streaming_response.exchange(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyExchangeResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_exchange(self, async_client: AsyncKnockMgmt) -> None:
        api_key = await async_client.api_keys.exchange(
            environment="development",
        )
        assert_matches_type(APIKeyExchangeResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_exchange(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.api_keys.with_raw_response.exchange(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyExchangeResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_exchange(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.api_keys.with_streaming_response.exchange(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyExchangeResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

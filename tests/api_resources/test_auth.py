# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import AuthVerifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: KnockMgmt) -> None:
        auth = client.auth.verify()
        assert_matches_type(AuthVerifyResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: KnockMgmt) -> None:
        response = client.auth.with_raw_response.verify()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthVerifyResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: KnockMgmt) -> None:
        with client.auth.with_streaming_response.verify() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthVerifyResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncKnockMgmt) -> None:
        auth = await async_client.auth.verify()
        assert_matches_type(AuthVerifyResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.auth.with_raw_response.verify()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthVerifyResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.auth.with_streaming_response.verify() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthVerifyResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

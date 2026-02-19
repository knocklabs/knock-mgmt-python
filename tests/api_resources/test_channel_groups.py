# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import ChannelGroup
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        channel_group = client.channel_groups.list()
        assert_matches_type(SyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        channel_group = client.channel_groups.list(
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.channel_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = response.parse()
        assert_matches_type(SyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.channel_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = response.parse()
            assert_matches_type(SyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChannelGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        channel_group = await async_client.channel_groups.list()
        assert_matches_type(AsyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        channel_group = await async_client.channel_groups.list(
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.channel_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = await response.parse()
        assert_matches_type(AsyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.channel_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = await response.parse()
            assert_matches_type(AsyncEntriesCursor[ChannelGroup], channel_group, path=["response"])

        assert cast(Any, response.is_closed) is True

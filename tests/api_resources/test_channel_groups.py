# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    ChannelGroup,
    ChannelGroupUpsertResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        channel_group = client.channel_groups.retrieve(
            "channel_group_key",
        )
        assert_matches_type(ChannelGroup, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.channel_groups.with_raw_response.retrieve(
            "channel_group_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = response.parse()
        assert_matches_type(ChannelGroup, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.channel_groups.with_streaming_response.retrieve(
            "channel_group_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = response.parse()
            assert_matches_type(ChannelGroup, channel_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_group_key` but received ''"):
            client.channel_groups.with_raw_response.retrieve(
                "",
            )

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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KnockMgmt) -> None:
        channel_group = client.channel_groups.delete(
            "channel_group_key",
        )
        assert channel_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KnockMgmt) -> None:
        response = client.channel_groups.with_raw_response.delete(
            "channel_group_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = response.parse()
        assert channel_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KnockMgmt) -> None:
        with client.channel_groups.with_streaming_response.delete(
            "channel_group_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = response.parse()
            assert channel_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_group_key` but received ''"):
            client.channel_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        channel_group = client.channel_groups.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
            },
        )
        assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        channel_group = client.channel_groups.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
                "channel_rules": [
                    {
                        "channel_key": "push-fcm",
                        "rule_type": "always",
                        "argument": "argument",
                        "index": 0,
                        "operator": "equal_to",
                        "variable": "variable",
                    }
                ],
                "operator": "any",
                "visible_in": ["workflow"],
            },
        )
        assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.channel_groups.with_raw_response.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = response.parse()
        assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.channel_groups.with_streaming_response.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = response.parse()
            assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_group_key` but received ''"):
            client.channel_groups.with_raw_response.upsert(
                channel_group_key="",
                channel_group={
                    "channel_type": "push",
                    "name": "Push Notification Group",
                },
            )


class TestAsyncChannelGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        channel_group = await async_client.channel_groups.retrieve(
            "channel_group_key",
        )
        assert_matches_type(ChannelGroup, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.channel_groups.with_raw_response.retrieve(
            "channel_group_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = await response.parse()
        assert_matches_type(ChannelGroup, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.channel_groups.with_streaming_response.retrieve(
            "channel_group_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = await response.parse()
            assert_matches_type(ChannelGroup, channel_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_group_key` but received ''"):
            await async_client.channel_groups.with_raw_response.retrieve(
                "",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnockMgmt) -> None:
        channel_group = await async_client.channel_groups.delete(
            "channel_group_key",
        )
        assert channel_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.channel_groups.with_raw_response.delete(
            "channel_group_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = await response.parse()
        assert channel_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.channel_groups.with_streaming_response.delete(
            "channel_group_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = await response.parse()
            assert channel_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_group_key` but received ''"):
            await async_client.channel_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        channel_group = await async_client.channel_groups.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
            },
        )
        assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        channel_group = await async_client.channel_groups.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
                "channel_rules": [
                    {
                        "channel_key": "push-fcm",
                        "rule_type": "always",
                        "argument": "argument",
                        "index": 0,
                        "operator": "equal_to",
                        "variable": "variable",
                    }
                ],
                "operator": "any",
                "visible_in": ["workflow"],
            },
        )
        assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.channel_groups.with_raw_response.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_group = await response.parse()
        assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.channel_groups.with_streaming_response.upsert(
            channel_group_key="channel_group_key",
            channel_group={
                "channel_type": "push",
                "name": "Push Notification Group",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_group = await response.parse()
            assert_matches_type(ChannelGroupUpsertResponse, channel_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_group_key` but received ''"):
            await async_client.channel_groups.with_raw_response.upsert(
                channel_group_key="",
                channel_group={
                    "channel_type": "push",
                    "name": "Push Notification Group",
                },
            )

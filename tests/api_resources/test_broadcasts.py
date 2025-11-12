# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Broadcast,
    BroadcastSendResponse,
    BroadcastCancelResponse,
    BroadcastUpsertResponse,
    BroadcastValidateResponse,
)
from knock_mapi._utils import parse_datetime
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBroadcasts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.broadcasts.with_raw_response.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.broadcasts.with_streaming_response.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            client.broadcasts.with_raw_response.retrieve(
                broadcast_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.broadcasts.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(SyncEntriesCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.broadcasts.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(SyncEntriesCursor[Broadcast], broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_cancel(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.cancel(
            broadcast_key="broadcast_key",
            environment="development",
        )
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_cancel_with_all_params(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.cancel(
            broadcast_key="broadcast_key",
            environment="development",
            branch="feature-branch",
        )
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_cancel(self, client: KnockMgmt) -> None:
        response = client.broadcasts.with_raw_response.cancel(
            broadcast_key="broadcast_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_cancel(self, client: KnockMgmt) -> None:
        with client.broadcasts.with_streaming_response.cancel(
            broadcast_key="broadcast_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_cancel(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            client.broadcasts.with_raw_response.cancel(
                broadcast_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_send(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.send(
            broadcast_key="broadcast_key",
            environment="development",
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_send_with_all_params(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.send(
            broadcast_key="broadcast_key",
            environment="development",
            branch="feature-branch",
            send_at=parse_datetime("2024-03-20T10:00:00Z"),
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_send(self, client: KnockMgmt) -> None:
        response = client.broadcasts.with_raw_response.send(
            broadcast_key="broadcast_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_send(self, client: KnockMgmt) -> None:
        with client.broadcasts.with_streaming_response.send(
            broadcast_key="broadcast_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_send(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            client.broadcasts.with_raw_response.send(
                broadcast_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["announcement"],
                "description": "A broadcast to all users",
                "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "settings": {
                    "is_commercial": True,
                    "override_preferences": False,
                },
                "target_audience_key": "all-users",
            },
            annotate=True,
            branch="feature-branch",
        )
        assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.broadcasts.with_raw_response.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.broadcasts.with_streaming_response.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            client.broadcasts.with_raw_response.upsert(
                broadcast_key="",
                environment="development",
                broadcast={
                    "name": "My Broadcast",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        broadcast = client.broadcasts.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["announcement"],
                "description": "A broadcast to all users",
                "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "settings": {
                    "is_commercial": True,
                    "override_preferences": False,
                },
                "target_audience_key": "all-users",
            },
            branch="feature-branch",
        )
        assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.broadcasts.with_raw_response.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.broadcasts.with_streaming_response.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            client.broadcasts.with_raw_response.validate(
                broadcast_key="",
                environment="development",
                broadcast={
                    "name": "My Broadcast",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )


class TestAsyncBroadcasts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.broadcasts.with_raw_response.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.broadcasts.with_streaming_response.retrieve(
            broadcast_key="broadcast_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            await async_client.broadcasts.with_raw_response.retrieve(
                broadcast_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.broadcasts.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Broadcast], broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.broadcasts.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Broadcast], broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.cancel(
            broadcast_key="broadcast_key",
            environment="development",
        )
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.cancel(
            broadcast_key="broadcast_key",
            environment="development",
            branch="feature-branch",
        )
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.broadcasts.with_raw_response.cancel(
            broadcast_key="broadcast_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.broadcasts.with_streaming_response.cancel(
            broadcast_key="broadcast_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastCancelResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            await async_client.broadcasts.with_raw_response.cancel(
                broadcast_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_send(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.send(
            broadcast_key="broadcast_key",
            environment="development",
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.send(
            broadcast_key="broadcast_key",
            environment="development",
            branch="feature-branch",
            send_at=parse_datetime("2024-03-20T10:00:00Z"),
        )
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.broadcasts.with_raw_response.send(
            broadcast_key="broadcast_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.broadcasts.with_streaming_response.send(
            broadcast_key="broadcast_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastSendResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            await async_client.broadcasts.with_raw_response.send(
                broadcast_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["announcement"],
                "description": "A broadcast to all users",
                "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "settings": {
                    "is_commercial": True,
                    "override_preferences": False,
                },
                "target_audience_key": "all-users",
            },
            annotate=True,
            branch="feature-branch",
        )
        assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.broadcasts.with_raw_response.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.broadcasts.with_streaming_response.upsert(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastUpsertResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            await async_client.broadcasts.with_raw_response.upsert(
                broadcast_key="",
                environment="development",
                broadcast={
                    "name": "My Broadcast",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        broadcast = await async_client.broadcasts.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["announcement"],
                "description": "A broadcast to all users",
                "scheduled_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "settings": {
                    "is_commercial": True,
                    "override_preferences": False,
                },
                "target_audience_key": "all-users",
            },
            branch="feature-branch",
        )
        assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.broadcasts.with_raw_response.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.broadcasts.with_streaming_response.validate(
            broadcast_key="broadcast_key",
            environment="development",
            broadcast={
                "name": "My Broadcast",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastValidateResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_key` but received ''"):
            await async_client.broadcasts.with_raw_response.validate(
                broadcast_key="",
                environment="development",
                broadcast={
                    "name": "My Broadcast",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    PreferenceCenterResetResponse,
    PreferenceCenterUpsertResponse,
    PreferenceCenterRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferenceCenter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        preference_center = client.preference_center.retrieve()
        assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        preference_center = client.preference_center.retrieve(
            environment="development",
        )
        assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.preference_center.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = response.parse()
        assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.preference_center.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = response.parse()
            assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset(self, client: KnockMgmt) -> None:
        preference_center = client.preference_center.reset()
        assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_with_all_params(self, client: KnockMgmt) -> None:
        preference_center = client.preference_center.reset(
            environment="development",
        )
        assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset(self, client: KnockMgmt) -> None:
        response = client.preference_center.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = response.parse()
        assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset(self, client: KnockMgmt) -> None:
        with client.preference_center.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = response.parse()
            assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        preference_center = client.preference_center.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
        )
        assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        preference_center = client.preference_center.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
            environment="development",
            enabled=True,
        )
        assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.preference_center.with_raw_response.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = response.parse()
        assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.preference_center.with_streaming_response.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = response.parse()
            assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreferenceCenter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        preference_center = await async_client.preference_center.retrieve()
        assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        preference_center = await async_client.preference_center.retrieve(
            environment="development",
        )
        assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.preference_center.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = await response.parse()
        assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.preference_center.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = await response.parse()
            assert_matches_type(PreferenceCenterRetrieveResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset(self, async_client: AsyncKnockMgmt) -> None:
        preference_center = await async_client.preference_center.reset()
        assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        preference_center = await async_client.preference_center.reset(
            environment="development",
        )
        assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.preference_center.with_raw_response.reset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = await response.parse()
        assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.preference_center.with_streaming_response.reset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = await response.parse()
            assert_matches_type(PreferenceCenterResetResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        preference_center = await async_client.preference_center.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
        )
        assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        preference_center = await async_client.preference_center.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
            environment="development",
            enabled=True,
        )
        assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.preference_center.with_raw_response.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = await response.parse()
        assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.preference_center.with_streaming_response.upsert(
            config={
                "body": "Select which communications you’d like to receive from us.",
                "rows": [
                    {
                        "description": "Receive promotional and non-essential notifications.",
                        "name": "Commercial messages",
                        "type": "commercial_subscribed",
                    }
                ],
                "show_account_name": True,
                "title": "Manage preferences",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = await response.parse()
            assert_matches_type(PreferenceCenterUpsertResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

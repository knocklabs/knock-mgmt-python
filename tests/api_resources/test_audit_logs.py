# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import AuditLogListResponse
from knock_mapi._utils import parse_datetime
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        audit_log = client.audit_logs.list()
        assert_matches_type(SyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        audit_log = client.audit_logs.list(
            action="string",
            actor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            environment="development",
            limit=0,
            resource_type="account",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        audit_log = await async_client.audit_logs.list()
        assert_matches_type(AsyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        audit_log = await async_client.audit_logs.list(
            action="string",
            actor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            before="before",
            environment="development",
            limit=0,
            resource_type="account",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncEntriesCursor[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

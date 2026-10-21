# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    ReusableRequest,
    ReusableRequestUpsertResponse,
    ReusableRequestArchiveResponse,
    ReusableRequestValidateResponse,
    ReusableRequestUpdateUnarchiveResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReusableRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.retrieve(
            reusable_request_key="fetch-user",
        )
        assert_matches_type(ReusableRequest, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.retrieve(
            reusable_request_key="fetch-user",
            annotate=True,
            branch="feature-branch",
            environment="development",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(ReusableRequest, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.reusable_requests.with_raw_response.retrieve(
            reusable_request_key="fetch-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = response.parse()
        assert_matches_type(ReusableRequest, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.reusable_requests.with_streaming_response.retrieve(
            reusable_request_key="fetch-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = response.parse()
            assert_matches_type(ReusableRequest, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            client.reusable_requests.with_raw_response.retrieve(
                reusable_request_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.list()
        assert_matches_type(SyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.list(
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            environment="development",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.reusable_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = response.parse()
        assert_matches_type(SyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.reusable_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = response.parse()
            assert_matches_type(SyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.archive(
            reusable_request_key="fetch-user",
        )
        assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.archive(
            reusable_request_key="fetch-user",
            environment="development",
        )
        assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: KnockMgmt) -> None:
        response = client.reusable_requests.with_raw_response.archive(
            reusable_request_key="fetch-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = response.parse()
        assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: KnockMgmt) -> None:
        with client.reusable_requests.with_streaming_response.archive(
            reusable_request_key="fetch-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = response.parse()
            assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            client.reusable_requests.with_raw_response.archive(
                reusable_request_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_unarchive(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.update_unarchive(
            reusable_request_key="fetch-user",
        )
        assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_unarchive_with_all_params(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.update_unarchive(
            reusable_request_key="fetch-user",
            environment="development",
        )
        assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_unarchive(self, client: KnockMgmt) -> None:
        response = client.reusable_requests.with_raw_response.update_unarchive(
            reusable_request_key="fetch-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = response.parse()
        assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_unarchive(self, client: KnockMgmt) -> None:
        with client.reusable_requests.with_streaming_response.update_unarchive(
            reusable_request_key="fetch-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = response.parse()
            assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_unarchive(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            client.reusable_requests.with_raw_response.update_unarchive(
                reusable_request_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )
        assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {
                    "method": "get",
                    "body": None,
                    "data_input_schema": {"foo": "bar"},
                    "data_input_values_str": "data_input_values_str",
                    "headers": [
                        {
                            "key": "X-API-Key",
                            "value": "1234567890",
                        }
                    ],
                    "query_params": [
                        {
                            "key": "key",
                            "value": "value",
                        }
                    ],
                    "response_path": None,
                    "signing_key": None,
                    "url": "https://example.com",
                },
                "type": "http_fetch",
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "Loads a user from the API.",
                "name": "Fetch user",
            },
            allow_empty=True,
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            environment="development",
            force=True,
        )
        assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.reusable_requests.with_raw_response.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = response.parse()
        assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.reusable_requests.with_streaming_response.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = response.parse()
            assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            client.reusable_requests.with_raw_response.upsert(
                reusable_request_key="",
                reusable_request={
                    "settings": {"method": "get"},
                    "type": "http_fetch",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )
        assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        reusable_request = client.reusable_requests.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {
                    "method": "get",
                    "body": None,
                    "data_input_schema": {"foo": "bar"},
                    "data_input_values_str": "data_input_values_str",
                    "headers": [
                        {
                            "key": "X-API-Key",
                            "value": "1234567890",
                        }
                    ],
                    "query_params": [
                        {
                            "key": "key",
                            "value": "value",
                        }
                    ],
                    "response_path": None,
                    "signing_key": None,
                    "url": "https://example.com",
                },
                "type": "http_fetch",
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "Loads a user from the API.",
                "name": "Fetch user",
            },
            branch="feature-branch",
            environment="development",
        )
        assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.reusable_requests.with_raw_response.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = response.parse()
        assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.reusable_requests.with_streaming_response.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = response.parse()
            assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            client.reusable_requests.with_raw_response.validate(
                reusable_request_key="",
                reusable_request={
                    "settings": {"method": "get"},
                    "type": "http_fetch",
                },
            )


class TestAsyncReusableRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.retrieve(
            reusable_request_key="fetch-user",
        )
        assert_matches_type(ReusableRequest, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.retrieve(
            reusable_request_key="fetch-user",
            annotate=True,
            branch="feature-branch",
            environment="development",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(ReusableRequest, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.reusable_requests.with_raw_response.retrieve(
            reusable_request_key="fetch-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = await response.parse()
        assert_matches_type(ReusableRequest, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.reusable_requests.with_streaming_response.retrieve(
            reusable_request_key="fetch-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = await response.parse()
            assert_matches_type(ReusableRequest, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            await async_client.reusable_requests.with_raw_response.retrieve(
                reusable_request_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.list()
        assert_matches_type(AsyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.list(
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            environment="development",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.reusable_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = await response.parse()
        assert_matches_type(AsyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.reusable_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = await response.parse()
            assert_matches_type(AsyncEntriesCursor[ReusableRequest], reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.archive(
            reusable_request_key="fetch-user",
        )
        assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.archive(
            reusable_request_key="fetch-user",
            environment="development",
        )
        assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.reusable_requests.with_raw_response.archive(
            reusable_request_key="fetch-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = await response.parse()
        assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.reusable_requests.with_streaming_response.archive(
            reusable_request_key="fetch-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = await response.parse()
            assert_matches_type(ReusableRequestArchiveResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            await async_client.reusable_requests.with_raw_response.archive(
                reusable_request_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_unarchive(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.update_unarchive(
            reusable_request_key="fetch-user",
        )
        assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_unarchive_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.update_unarchive(
            reusable_request_key="fetch-user",
            environment="development",
        )
        assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_unarchive(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.reusable_requests.with_raw_response.update_unarchive(
            reusable_request_key="fetch-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = await response.parse()
        assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_unarchive(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.reusable_requests.with_streaming_response.update_unarchive(
            reusable_request_key="fetch-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = await response.parse()
            assert_matches_type(ReusableRequestUpdateUnarchiveResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_unarchive(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            await async_client.reusable_requests.with_raw_response.update_unarchive(
                reusable_request_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )
        assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {
                    "method": "get",
                    "body": None,
                    "data_input_schema": {"foo": "bar"},
                    "data_input_values_str": "data_input_values_str",
                    "headers": [
                        {
                            "key": "X-API-Key",
                            "value": "1234567890",
                        }
                    ],
                    "query_params": [
                        {
                            "key": "key",
                            "value": "value",
                        }
                    ],
                    "response_path": None,
                    "signing_key": None,
                    "url": "https://example.com",
                },
                "type": "http_fetch",
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "Loads a user from the API.",
                "name": "Fetch user",
            },
            allow_empty=True,
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            environment="development",
            force=True,
        )
        assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.reusable_requests.with_raw_response.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = await response.parse()
        assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.reusable_requests.with_streaming_response.upsert(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = await response.parse()
            assert_matches_type(ReusableRequestUpsertResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            await async_client.reusable_requests.with_raw_response.upsert(
                reusable_request_key="",
                reusable_request={
                    "settings": {"method": "get"},
                    "type": "http_fetch",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )
        assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        reusable_request = await async_client.reusable_requests.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {
                    "method": "get",
                    "body": None,
                    "data_input_schema": {"foo": "bar"},
                    "data_input_values_str": "data_input_values_str",
                    "headers": [
                        {
                            "key": "X-API-Key",
                            "value": "1234567890",
                        }
                    ],
                    "query_params": [
                        {
                            "key": "key",
                            "value": "value",
                        }
                    ],
                    "response_path": None,
                    "signing_key": None,
                    "url": "https://example.com",
                },
                "type": "http_fetch",
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "Loads a user from the API.",
                "name": "Fetch user",
            },
            branch="feature-branch",
            environment="development",
        )
        assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.reusable_requests.with_raw_response.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reusable_request = await response.parse()
        assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.reusable_requests.with_streaming_response.validate(
            reusable_request_key="fetch-user",
            reusable_request={
                "settings": {"method": "get"},
                "type": "http_fetch",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reusable_request = await response.parse()
            assert_matches_type(ReusableRequestValidateResponse, reusable_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reusable_request_key` but received ''"):
            await async_client.reusable_requests.with_raw_response.validate(
                reusable_request_key="",
                reusable_request={
                    "settings": {"method": "get"},
                    "type": "http_fetch",
                },
            )

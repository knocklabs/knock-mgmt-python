# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    WarehouseSync,
    WarehouseSyncUpdateResponse,
    WarehouseSyncUpdateRunResponse,
    WarehouseSyncRetrieveRunsResponse,
    WarehouseSyncUpdateSettingsResponse,
    WarehouseSyncUpdateValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWarehouseSyncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.retrieve(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.retrieve(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.retrieve(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.retrieve(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            client.warehouse_syncs.with_raw_response.retrieve(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )
        assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={
                "change_tracking": {
                    "is_deleted_column": "is_deleted",
                    "last_modified_column": "updated_at",
                },
                "description": "description",
                "mappings": [
                    {
                        "source_column": "id",
                        "target_field": "id",
                        "on_null": "set_null",
                    },
                    {
                        "source_column": "email",
                        "target_field": "email",
                        "on_null": "set_null",
                    },
                ],
                "name": "Users",
                "primary_key_column": "id",
                "source": {
                    "mode": "sql",
                    "name": "name",
                    "query": "SELECT id, email, name, updated_at FROM analytics.users",
                    "schema": "schema",
                },
                "target": {
                    "audience_key": "audience_key",
                    "collection": "projects",
                },
                "target_type": "user",
                "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "warehouse_key": "analytics",
            },
            commit=True,
            commit_message="commit_message",
            environment="development",
        )
        assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            client.warehouse_syncs.with_raw_response.update(
                warehouse_sync_key="",
                warehouse_sync={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.list()
        assert_matches_type(SyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.list(
            after="after",
            before="before",
            environment="development",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(SyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(SyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_runs(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_runs_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
        )
        assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_runs(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_runs(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_runs(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            client.warehouse_syncs.with_raw_response.retrieve_runs(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_run(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update_run(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_run_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update_run(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
        )
        assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_run(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.update_run(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_run(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.update_run(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_run(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            client.warehouse_syncs.with_raw_response.update_run(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update_settings(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update_settings(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
            enabled=False,
            frequency_minutes=1440,
        )
        assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.update_settings(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.update_settings(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_settings(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            client.warehouse_syncs.with_raw_response.update_settings(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_validate(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )
        assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_validate_with_all_params(self, client: KnockMgmt) -> None:
        warehouse_sync = client.warehouse_syncs.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={
                "change_tracking": {
                    "is_deleted_column": "is_deleted",
                    "last_modified_column": "updated_at",
                },
                "description": "description",
                "mappings": [
                    {
                        "source_column": "id",
                        "target_field": "id",
                        "on_null": "set_null",
                    },
                    {
                        "source_column": "email",
                        "target_field": "email",
                        "on_null": "set_null",
                    },
                ],
                "name": "Users",
                "primary_key_column": "id",
                "source": {
                    "mode": "sql",
                    "name": "name",
                    "query": "SELECT id, email, name, updated_at FROM analytics.users",
                    "schema": "schema",
                },
                "target": {
                    "audience_key": "audience_key",
                    "collection": "projects",
                },
                "target_type": "user",
                "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "warehouse_key": "analytics",
            },
            environment="development",
        )
        assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_validate(self, client: KnockMgmt) -> None:
        response = client.warehouse_syncs.with_raw_response.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = response.parse()
        assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_validate(self, client: KnockMgmt) -> None:
        with client.warehouse_syncs.with_streaming_response.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = response.parse()
            assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            client.warehouse_syncs.with_raw_response.update_validate(
                warehouse_sync_key="",
                warehouse_sync={},
            )


class TestAsyncWarehouseSyncs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.retrieve(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.retrieve(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.retrieve(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.retrieve(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(WarehouseSync, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            await async_client.warehouse_syncs.with_raw_response.retrieve(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )
        assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={
                "change_tracking": {
                    "is_deleted_column": "is_deleted",
                    "last_modified_column": "updated_at",
                },
                "description": "description",
                "mappings": [
                    {
                        "source_column": "id",
                        "target_field": "id",
                        "on_null": "set_null",
                    },
                    {
                        "source_column": "email",
                        "target_field": "email",
                        "on_null": "set_null",
                    },
                ],
                "name": "Users",
                "primary_key_column": "id",
                "source": {
                    "mode": "sql",
                    "name": "name",
                    "query": "SELECT id, email, name, updated_at FROM analytics.users",
                    "schema": "schema",
                },
                "target": {
                    "audience_key": "audience_key",
                    "collection": "projects",
                },
                "target_type": "user",
                "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "warehouse_key": "analytics",
            },
            commit=True,
            commit_message="commit_message",
            environment="development",
        )
        assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.update(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(WarehouseSyncUpdateResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            await async_client.warehouse_syncs.with_raw_response.update(
                warehouse_sync_key="",
                warehouse_sync={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.list()
        assert_matches_type(AsyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.list(
            after="after",
            before="before",
            environment="development",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(AsyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(AsyncEntriesCursor[WarehouseSync], warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_runs(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_runs_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
        )
        assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_runs(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_runs(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.retrieve_runs(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(WarehouseSyncRetrieveRunsResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_runs(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            await async_client.warehouse_syncs.with_raw_response.retrieve_runs(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_run(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update_run(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_run_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update_run(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
        )
        assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_run(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.update_run(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_run(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.update_run(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(WarehouseSyncUpdateRunResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_run(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            await async_client.warehouse_syncs.with_raw_response.update_run(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update_settings(
            warehouse_sync_key="warehouse_sync_key",
        )
        assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update_settings(
            warehouse_sync_key="warehouse_sync_key",
            environment="development",
            enabled=False,
            frequency_minutes=1440,
        )
        assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.update_settings(
            warehouse_sync_key="warehouse_sync_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.update_settings(
            warehouse_sync_key="warehouse_sync_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(WarehouseSyncUpdateSettingsResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            await async_client.warehouse_syncs.with_raw_response.update_settings(
                warehouse_sync_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_validate(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )
        assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        warehouse_sync = await async_client.warehouse_syncs.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={
                "change_tracking": {
                    "is_deleted_column": "is_deleted",
                    "last_modified_column": "updated_at",
                },
                "description": "description",
                "mappings": [
                    {
                        "source_column": "id",
                        "target_field": "id",
                        "on_null": "set_null",
                    },
                    {
                        "source_column": "email",
                        "target_field": "email",
                        "on_null": "set_null",
                    },
                ],
                "name": "Users",
                "primary_key_column": "id",
                "source": {
                    "mode": "sql",
                    "name": "name",
                    "query": "SELECT id, email, name, updated_at FROM analytics.users",
                    "schema": "schema",
                },
                "target": {
                    "audience_key": "audience_key",
                    "collection": "projects",
                },
                "target_type": "user",
                "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "warehouse_key": "analytics",
            },
            environment="development",
        )
        assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.warehouse_syncs.with_raw_response.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warehouse_sync = await response.parse()
        assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.warehouse_syncs.with_streaming_response.update_validate(
            warehouse_sync_key="warehouse_sync_key",
            warehouse_sync={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warehouse_sync = await response.parse()
            assert_matches_type(WarehouseSyncUpdateValidateResponse, warehouse_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `warehouse_sync_key` but received ''"):
            await async_client.warehouse_syncs.with_raw_response.update_validate(
                warehouse_sync_key="",
                warehouse_sync={},
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Source,
    SourceLog,
    SourcesResponse,
    SourceEventsResponse,
    SourceStatusResponse,
    SourceProviderResponse,
    SourceRehearseResponse,
    SourceProvidersResponse,
    DataSourceUpsertResponse,
)
from knock_mapi._utils import parse_datetime
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.retrieve(
            key="key",
            environment="development",
        )
        assert_matches_type(Source, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.retrieve(
            key="key",
            environment="development",
            annotate=True,
        )
        assert_matches_type(Source, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.retrieve(
            key="key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(Source, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.retrieve(
            key="key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(Source, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.retrieve(
                key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_events(
            key="key",
        )
        assert_matches_type(SourceEventsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_events(
            key="key",
            environment="development",
        )
        assert_matches_type(SourceEventsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.list_events(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SourceEventsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.list_events(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SourceEventsResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_events(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.list_events(
                key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_logs(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_logs(
            key="key",
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[SourceLog], data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_logs_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_logs(
            key="key",
            environment="development",
            id="id",
            after="after",
            before="before",
            date="date",
            ending_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            event="event",
            includes=["actions"],
            limit=0,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncEntriesCursor[SourceLog], data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_logs(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.list_logs(
            key="key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SyncEntriesCursor[SourceLog], data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_logs(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.list_logs(
            key="key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SyncEntriesCursor[SourceLog], data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_logs(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.list_logs(
                key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_providers(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_providers()
        assert_matches_type(SourceProvidersResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_providers(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SourceProvidersResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_providers(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SourceProvidersResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_sources(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_sources()
        assert_matches_type(SourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_sources_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.list_sources(
            environment="development",
        )
        assert_matches_type(SourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_sources(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.list_sources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_sources(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.list_sources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SourcesResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rehearse(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.rehearse(
            key="key",
            environment="development",
            payload={
                "body": "bar",
                "headers": "bar",
            },
        )
        assert_matches_type(SourceRehearseResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rehearse(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.rehearse(
            key="key",
            environment="development",
            payload={
                "body": "bar",
                "headers": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SourceRehearseResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rehearse(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.rehearse(
            key="key",
            environment="development",
            payload={
                "body": "bar",
                "headers": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SourceRehearseResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rehearse(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.rehearse(
                key="",
                environment="development",
                payload={
                    "body": "bar",
                    "headers": "bar",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_provider(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.retrieve_provider(
            key="key",
        )
        assert_matches_type(SourceProviderResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_provider_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.retrieve_provider(
            key="key",
            includes=["branding"],
        )
        assert_matches_type(SourceProviderResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_provider(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.retrieve_provider(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SourceProviderResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_provider(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.retrieve_provider(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SourceProviderResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_provider(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.retrieve_provider(
                key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.retrieve_status(
            key="key",
        )
        assert_matches_type(SourceStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.retrieve_status(
            key="key",
            environment="development",
        )
        assert_matches_type(SourceStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.retrieve_status(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SourceStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.retrieve_status(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SourceStatusResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.retrieve_status(
                key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.upsert(
            key="key",
            environment="development",
            source={"name": "Universal HTTP Source"},
        )
        assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        data_source = client.data_sources.upsert(
            key="key",
            environment="development",
            source={
                "name": "Universal HTTP Source",
                "custom_image_url": None,
                "description": "Receives events over HTTP.",
                "environment_settings": {
                    "development": {
                        "mappings": [
                            {
                                "action_type": "workflows_trigger",
                                "event_type": "event_type",
                                "action_parameters": {"foo": "bar"},
                                "inactive_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "is_deleted": True,
                            }
                        ],
                        "settings": {
                            "enforce_verification": False,
                            "event_type_path": "body.event",
                            "idempotency_key_path": "body.messageId",
                            "preprocess_script": {
                                "language": "javascript",
                                "source": "return event;",
                            },
                            "timestamp_path": "body.timestamp",
                        },
                    }
                },
                "preconfigured_provider": "preconfigured_provider",
            },
            annotate=True,
        )
        assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.data_sources.with_raw_response.upsert(
            key="key",
            environment="development",
            source={"name": "Universal HTTP Source"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.data_sources.with_streaming_response.upsert(
            key="key",
            environment="development",
            source={"name": "Universal HTTP Source"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.data_sources.with_raw_response.upsert(
                key="",
                environment="development",
                source={"name": "Universal HTTP Source"},
            )


class TestAsyncDataSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.retrieve(
            key="key",
            environment="development",
        )
        assert_matches_type(Source, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.retrieve(
            key="key",
            environment="development",
            annotate=True,
        )
        assert_matches_type(Source, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.retrieve(
            key="key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(Source, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.retrieve(
            key="key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(Source, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.retrieve(
                key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_events(
            key="key",
        )
        assert_matches_type(SourceEventsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_events(
            key="key",
            environment="development",
        )
        assert_matches_type(SourceEventsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.list_events(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(SourceEventsResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.list_events(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(SourceEventsResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.list_events(
                key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_logs(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_logs(
            key="key",
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[SourceLog], data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_logs_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_logs(
            key="key",
            environment="development",
            id="id",
            after="after",
            before="before",
            date="date",
            ending_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            event="event",
            includes=["actions"],
            limit=0,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncEntriesCursor[SourceLog], data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_logs(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.list_logs(
            key="key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(AsyncEntriesCursor[SourceLog], data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_logs(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.list_logs(
            key="key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(AsyncEntriesCursor[SourceLog], data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_logs(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.list_logs(
                key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_providers(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_providers()
        assert_matches_type(SourceProvidersResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(SourceProvidersResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(SourceProvidersResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_sources(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_sources()
        assert_matches_type(SourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_sources_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.list_sources(
            environment="development",
        )
        assert_matches_type(SourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_sources(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.list_sources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(SourcesResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_sources(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.list_sources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(SourcesResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rehearse(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.rehearse(
            key="key",
            environment="development",
            payload={
                "body": "bar",
                "headers": "bar",
            },
        )
        assert_matches_type(SourceRehearseResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rehearse(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.rehearse(
            key="key",
            environment="development",
            payload={
                "body": "bar",
                "headers": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(SourceRehearseResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rehearse(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.rehearse(
            key="key",
            environment="development",
            payload={
                "body": "bar",
                "headers": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(SourceRehearseResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rehearse(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.rehearse(
                key="",
                environment="development",
                payload={
                    "body": "bar",
                    "headers": "bar",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_provider(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.retrieve_provider(
            key="key",
        )
        assert_matches_type(SourceProviderResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_provider_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.retrieve_provider(
            key="key",
            includes=["branding"],
        )
        assert_matches_type(SourceProviderResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_provider(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.retrieve_provider(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(SourceProviderResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_provider(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.retrieve_provider(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(SourceProviderResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_provider(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.retrieve_provider(
                key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.retrieve_status(
            key="key",
        )
        assert_matches_type(SourceStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.retrieve_status(
            key="key",
            environment="development",
        )
        assert_matches_type(SourceStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.retrieve_status(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(SourceStatusResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.retrieve_status(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(SourceStatusResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.retrieve_status(
                key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.upsert(
            key="key",
            environment="development",
            source={"name": "Universal HTTP Source"},
        )
        assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        data_source = await async_client.data_sources.upsert(
            key="key",
            environment="development",
            source={
                "name": "Universal HTTP Source",
                "custom_image_url": None,
                "description": "Receives events over HTTP.",
                "environment_settings": {
                    "development": {
                        "mappings": [
                            {
                                "action_type": "workflows_trigger",
                                "event_type": "event_type",
                                "action_parameters": {"foo": "bar"},
                                "inactive_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "is_deleted": True,
                            }
                        ],
                        "settings": {
                            "enforce_verification": False,
                            "event_type_path": "body.event",
                            "idempotency_key_path": "body.messageId",
                            "preprocess_script": {
                                "language": "javascript",
                                "source": "return event;",
                            },
                            "timestamp_path": "body.timestamp",
                        },
                    }
                },
                "preconfigured_provider": "preconfigured_provider",
            },
            annotate=True,
        )
        assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.data_sources.with_raw_response.upsert(
            key="key",
            environment="development",
            source={"name": "Universal HTTP Source"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.data_sources.with_streaming_response.upsert(
            key="key",
            environment="development",
            source={"name": "Universal HTTP Source"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceUpsertResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.data_sources.with_raw_response.upsert(
                key="",
                environment="development",
                source={"name": "Universal HTTP Source"},
            )

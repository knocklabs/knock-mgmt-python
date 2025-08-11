# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Guide,
    GuideUpsertResponse,
    GuideActivateResponse,
    GuideValidateResponse,
)
from knock_mapi._utils import parse_datetime
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGuides:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        guide = client.guides.retrieve(
            guide_key="guide_key",
            environment="development",
        )
        assert_matches_type(Guide, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        guide = client.guides.retrieve(
            guide_key="guide_key",
            environment="development",
            annotate=True,
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Guide, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.guides.with_raw_response.retrieve(
            guide_key="guide_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(Guide, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.guides.with_streaming_response.retrieve(
            guide_key="guide_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(Guide, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            client.guides.with_raw_response.retrieve(
                guide_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        guide = client.guides.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Guide], guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        guide = client.guides.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Guide], guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.guides.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(SyncEntriesCursor[Guide], guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.guides.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(SyncEntriesCursor[Guide], guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_activate_overload_1(self, client: KnockMgmt) -> None:
        guide = client.guides.activate(
            guide_key="guide_key",
            environment="development",
            status=True,
        )
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_activate_overload_1(self, client: KnockMgmt) -> None:
        response = client.guides.with_raw_response.activate(
            guide_key="guide_key",
            environment="development",
            status=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_activate_overload_1(self, client: KnockMgmt) -> None:
        with client.guides.with_streaming_response.activate(
            guide_key="guide_key",
            environment="development",
            status=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideActivateResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_activate_overload_1(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            client.guides.with_raw_response.activate(
                guide_key="",
                environment="development",
                status=True,
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_activate_overload_2(self, client: KnockMgmt) -> None:
        guide = client.guides.activate(
            guide_key="guide_key",
            environment="development",
        )
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_activate_with_all_params_overload_2(self, client: KnockMgmt) -> None:
        guide = client.guides.activate(
            guide_key="guide_key",
            environment="development",
            from_=parse_datetime("2024-03-20T10:00:00Z"),
            until=parse_datetime("2024-03-21T10:00:00Z"),
        )
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_activate_overload_2(self, client: KnockMgmt) -> None:
        response = client.guides.with_raw_response.activate(
            guide_key="guide_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_activate_overload_2(self, client: KnockMgmt) -> None:
        with client.guides.with_streaming_response.activate(
            guide_key="guide_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideActivateResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_activate_overload_2(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            client.guides.with_raw_response.activate(
                guide_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        guide = client.guides.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )
        assert_matches_type(GuideUpsertResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        guide = client.guides.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                        "name": "Welcome to the App",
                        "values": {"text_field": "bar"},
                    }
                ],
                "activation_location_rules": [
                    {
                        "directive": "allow",
                        "pathname": "/dashboard/*",
                    }
                ],
                "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "A guide to help users get started with the application",
                "target_audience_id": None,
                "target_property_conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
            },
            annotate=True,
            commit=True,
            commit_message="commit_message",
        )
        assert_matches_type(GuideUpsertResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.guides.with_raw_response.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideUpsertResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.guides.with_streaming_response.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideUpsertResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            client.guides.with_raw_response.upsert(
                guide_key="",
                environment="development",
                guide={
                    "channel_key": "in-app-guide",
                    "name": "Getting Started Guide",
                    "steps": [
                        {
                            "ref": "welcome-step",
                            "schema_key": "tooltip",
                            "schema_semver": "1.0.0",
                            "schema_variant_key": "default",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        guide = client.guides.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )
        assert_matches_type(GuideValidateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        guide = client.guides.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                        "name": "Welcome to the App",
                        "values": {"text_field": "bar"},
                    }
                ],
                "activation_location_rules": [
                    {
                        "directive": "allow",
                        "pathname": "/dashboard/*",
                    }
                ],
                "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "A guide to help users get started with the application",
                "target_audience_id": None,
                "target_property_conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
            },
        )
        assert_matches_type(GuideValidateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.guides.with_raw_response.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideValidateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.guides.with_streaming_response.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideValidateResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            client.guides.with_raw_response.validate(
                guide_key="",
                environment="development",
                guide={
                    "channel_key": "in-app-guide",
                    "name": "Getting Started Guide",
                    "steps": [
                        {
                            "ref": "welcome-step",
                            "schema_key": "tooltip",
                            "schema_semver": "1.0.0",
                            "schema_variant_key": "default",
                        }
                    ],
                },
            )


class TestAsyncGuides:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.retrieve(
            guide_key="guide_key",
            environment="development",
        )
        assert_matches_type(Guide, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.retrieve(
            guide_key="guide_key",
            environment="development",
            annotate=True,
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Guide, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.guides.with_raw_response.retrieve(
            guide_key="guide_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(Guide, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.guides.with_streaming_response.retrieve(
            guide_key="guide_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(Guide, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            await async_client.guides.with_raw_response.retrieve(
                guide_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Guide], guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Guide], guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.guides.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Guide], guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.guides.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Guide], guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_activate_overload_1(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.activate(
            guide_key="guide_key",
            environment="development",
            status=True,
        )
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_activate_overload_1(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.guides.with_raw_response.activate(
            guide_key="guide_key",
            environment="development",
            status=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_activate_overload_1(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.guides.with_streaming_response.activate(
            guide_key="guide_key",
            environment="development",
            status=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideActivateResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_activate_overload_1(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            await async_client.guides.with_raw_response.activate(
                guide_key="",
                environment="development",
                status=True,
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_activate_overload_2(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.activate(
            guide_key="guide_key",
            environment="development",
        )
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_activate_with_all_params_overload_2(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.activate(
            guide_key="guide_key",
            environment="development",
            from_=parse_datetime("2024-03-20T10:00:00Z"),
            until=parse_datetime("2024-03-21T10:00:00Z"),
        )
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_activate_overload_2(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.guides.with_raw_response.activate(
            guide_key="guide_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideActivateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_activate_overload_2(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.guides.with_streaming_response.activate(
            guide_key="guide_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideActivateResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_activate_overload_2(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            await async_client.guides.with_raw_response.activate(
                guide_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )
        assert_matches_type(GuideUpsertResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                        "name": "Welcome to the App",
                        "values": {"text_field": "bar"},
                    }
                ],
                "activation_location_rules": [
                    {
                        "directive": "allow",
                        "pathname": "/dashboard/*",
                    }
                ],
                "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "A guide to help users get started with the application",
                "target_audience_id": None,
                "target_property_conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
            },
            annotate=True,
            commit=True,
            commit_message="commit_message",
        )
        assert_matches_type(GuideUpsertResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.guides.with_raw_response.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideUpsertResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.guides.with_streaming_response.upsert(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideUpsertResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            await async_client.guides.with_raw_response.upsert(
                guide_key="",
                environment="development",
                guide={
                    "channel_key": "in-app-guide",
                    "name": "Getting Started Guide",
                    "steps": [
                        {
                            "ref": "welcome-step",
                            "schema_key": "tooltip",
                            "schema_semver": "1.0.0",
                            "schema_variant_key": "default",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )
        assert_matches_type(GuideValidateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        guide = await async_client.guides.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                        "name": "Welcome to the App",
                        "values": {"text_field": "bar"},
                    }
                ],
                "activation_location_rules": [
                    {
                        "directive": "allow",
                        "pathname": "/dashboard/*",
                    }
                ],
                "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "description": "A guide to help users get started with the application",
                "target_audience_id": None,
                "target_property_conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
            },
        )
        assert_matches_type(GuideValidateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.guides.with_raw_response.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideValidateResponse, guide, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.guides.with_streaming_response.validate(
            guide_key="guide_key",
            environment="development",
            guide={
                "channel_key": "in-app-guide",
                "name": "Getting Started Guide",
                "steps": [
                    {
                        "ref": "welcome-step",
                        "schema_key": "tooltip",
                        "schema_semver": "1.0.0",
                        "schema_variant_key": "default",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideValidateResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guide_key` but received ''"):
            await async_client.guides.with_raw_response.validate(
                guide_key="",
                environment="development",
                guide={
                    "channel_key": "in-app-guide",
                    "name": "Getting Started Guide",
                    "steps": [
                        {
                            "ref": "welcome-step",
                            "schema_key": "tooltip",
                            "schema_semver": "1.0.0",
                            "schema_variant_key": "default",
                        }
                    ],
                },
            )

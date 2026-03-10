# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Audience,
    AudienceUpsertResponse,
    AudienceArchiveResponse,
    AudienceValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        audience = client.audiences.retrieve(
            audience_key="audience_key",
            environment="development",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        audience = client.audiences.retrieve(
            audience_key="audience_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.audiences.with_raw_response.retrieve(
            audience_key="audience_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.audiences.with_streaming_response.retrieve(
            audience_key="audience_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            client.audiences.with_raw_response.retrieve(
                audience_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        audience = client.audiences.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        audience = client.audiences.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.audiences.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(SyncEntriesCursor[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.audiences.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(SyncEntriesCursor[Audience], audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: KnockMgmt) -> None:
        audience = client.audiences.archive(
            audience_key="audience_key",
            environment="development",
        )
        assert_matches_type(AudienceArchiveResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: KnockMgmt) -> None:
        response = client.audiences.with_raw_response.archive(
            audience_key="audience_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceArchiveResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: KnockMgmt) -> None:
        with client.audiences.with_streaming_response.archive(
            audience_key="audience_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceArchiveResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            client.audiences.with_raw_response.archive(
                audience_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        audience = client.audiences.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )
        assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        audience = client.audiences.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
                "description": "Users on the premium plan",
                "segments": [
                    {
                        "conditions": [
                            {
                                "operator": "equal_to",
                                "property": "recipient.plan",
                                "argument": "premium",
                            }
                        ]
                    }
                ],
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
        )
        assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.audiences.with_raw_response.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.audiences.with_streaming_response.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            client.audiences.with_raw_response.upsert(
                audience_key="",
                environment="development",
                audience={
                    "name": "Premium users",
                    "type": "dynamic",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        audience = client.audiences.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )
        assert_matches_type(AudienceValidateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        audience = client.audiences.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
                "description": "Users on the premium plan",
                "segments": [
                    {
                        "conditions": [
                            {
                                "operator": "equal_to",
                                "property": "recipient.plan",
                                "argument": "premium",
                            }
                        ]
                    }
                ],
            },
            branch="feature-branch",
        )
        assert_matches_type(AudienceValidateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.audiences.with_raw_response.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceValidateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.audiences.with_streaming_response.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceValidateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            client.audiences.with_raw_response.validate(
                audience_key="",
                environment="development",
                audience={
                    "name": "Premium users",
                    "type": "dynamic",
                },
            )


class TestAsyncAudiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.retrieve(
            audience_key="audience_key",
            environment="development",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.retrieve(
            audience_key="audience_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.audiences.with_raw_response.retrieve(
            audience_key="audience_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.audiences.with_streaming_response.retrieve(
            audience_key="audience_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            await async_client.audiences.with_raw_response.retrieve(
                audience_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.audiences.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Audience], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.audiences.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Audience], audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.archive(
            audience_key="audience_key",
            environment="development",
        )
        assert_matches_type(AudienceArchiveResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.audiences.with_raw_response.archive(
            audience_key="audience_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceArchiveResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.audiences.with_streaming_response.archive(
            audience_key="audience_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceArchiveResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            await async_client.audiences.with_raw_response.archive(
                audience_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )
        assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
                "description": "Users on the premium plan",
                "segments": [
                    {
                        "conditions": [
                            {
                                "operator": "equal_to",
                                "property": "recipient.plan",
                                "argument": "premium",
                            }
                        ]
                    }
                ],
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
        )
        assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.audiences.with_raw_response.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.audiences.with_streaming_response.upsert(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceUpsertResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            await async_client.audiences.with_raw_response.upsert(
                audience_key="",
                environment="development",
                audience={
                    "name": "Premium users",
                    "type": "dynamic",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )
        assert_matches_type(AudienceValidateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        audience = await async_client.audiences.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
                "description": "Users on the premium plan",
                "segments": [
                    {
                        "conditions": [
                            {
                                "operator": "equal_to",
                                "property": "recipient.plan",
                                "argument": "premium",
                            }
                        ]
                    }
                ],
            },
            branch="feature-branch",
        )
        assert_matches_type(AudienceValidateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.audiences.with_raw_response.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceValidateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.audiences.with_streaming_response.validate(
            audience_key="audience_key",
            environment="development",
            audience={
                "name": "Premium users",
                "type": "dynamic",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceValidateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_key` but received ''"):
            await async_client.audiences.with_raw_response.validate(
                audience_key="",
                environment="development",
                audience={
                    "name": "Premium users",
                    "type": "dynamic",
                },
            )

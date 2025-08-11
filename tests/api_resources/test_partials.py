# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Partial,
    PartialUpsertResponse,
    PartialValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPartials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        partial = client.partials.retrieve(
            partial_key="partial_key",
            environment="development",
        )
        assert_matches_type(Partial, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        partial = client.partials.retrieve(
            partial_key="partial_key",
            environment="development",
            annotate=True,
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Partial, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.partials.with_raw_response.retrieve(
            partial_key="partial_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = response.parse()
        assert_matches_type(Partial, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.partials.with_streaming_response.retrieve(
            partial_key="partial_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = response.parse()
            assert_matches_type(Partial, partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partial_key` but received ''"):
            client.partials.with_raw_response.retrieve(
                partial_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        partial = client.partials.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Partial], partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        partial = client.partials.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Partial], partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.partials.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = response.parse()
        assert_matches_type(SyncEntriesCursor[Partial], partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.partials.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = response.parse()
            assert_matches_type(SyncEntriesCursor[Partial], partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        partial = client.partials.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )
        assert_matches_type(PartialUpsertResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        partial = client.partials.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
                "description": "description",
                "icon_name": "icon_name",
                "visual_block_enabled": False,
            },
            annotate=True,
            commit=True,
            commit_message="commit_message",
        )
        assert_matches_type(PartialUpsertResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.partials.with_raw_response.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = response.parse()
        assert_matches_type(PartialUpsertResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.partials.with_streaming_response.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = response.parse()
            assert_matches_type(PartialUpsertResponse, partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partial_key` but received ''"):
            client.partials.with_raw_response.upsert(
                partial_key="",
                environment="development",
                partial={
                    "content": "<p>Hello, world!</p>",
                    "name": "My Partial",
                    "type": "html",
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        partial = client.partials.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )
        assert_matches_type(PartialValidateResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        partial = client.partials.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
                "description": "description",
                "icon_name": "icon_name",
                "visual_block_enabled": False,
            },
        )
        assert_matches_type(PartialValidateResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.partials.with_raw_response.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = response.parse()
        assert_matches_type(PartialValidateResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.partials.with_streaming_response.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = response.parse()
            assert_matches_type(PartialValidateResponse, partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partial_key` but received ''"):
            client.partials.with_raw_response.validate(
                partial_key="",
                environment="development",
                partial={
                    "content": "<p>Hello, world!</p>",
                    "name": "My Partial",
                    "type": "html",
                },
            )


class TestAsyncPartials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.retrieve(
            partial_key="partial_key",
            environment="development",
        )
        assert_matches_type(Partial, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.retrieve(
            partial_key="partial_key",
            environment="development",
            annotate=True,
            hide_uncommitted_changes=True,
        )
        assert_matches_type(Partial, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.partials.with_raw_response.retrieve(
            partial_key="partial_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = await response.parse()
        assert_matches_type(Partial, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.partials.with_streaming_response.retrieve(
            partial_key="partial_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = await response.parse()
            assert_matches_type(Partial, partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partial_key` but received ''"):
            await async_client.partials.with_raw_response.retrieve(
                partial_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Partial], partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Partial], partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.partials.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Partial], partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.partials.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Partial], partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )
        assert_matches_type(PartialUpsertResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
                "description": "description",
                "icon_name": "icon_name",
                "visual_block_enabled": False,
            },
            annotate=True,
            commit=True,
            commit_message="commit_message",
        )
        assert_matches_type(PartialUpsertResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.partials.with_raw_response.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = await response.parse()
        assert_matches_type(PartialUpsertResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.partials.with_streaming_response.upsert(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = await response.parse()
            assert_matches_type(PartialUpsertResponse, partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partial_key` but received ''"):
            await async_client.partials.with_raw_response.upsert(
                partial_key="",
                environment="development",
                partial={
                    "content": "<p>Hello, world!</p>",
                    "name": "My Partial",
                    "type": "html",
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )
        assert_matches_type(PartialValidateResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        partial = await async_client.partials.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
                "description": "description",
                "icon_name": "icon_name",
                "visual_block_enabled": False,
            },
        )
        assert_matches_type(PartialValidateResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.partials.with_raw_response.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partial = await response.parse()
        assert_matches_type(PartialValidateResponse, partial, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.partials.with_streaming_response.validate(
            partial_key="partial_key",
            environment="development",
            partial={
                "content": "<p>Hello, world!</p>",
                "name": "My Partial",
                "type": "html",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partial = await response.parse()
            assert_matches_type(PartialValidateResponse, partial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partial_key` but received ''"):
            await async_client.partials.with_raw_response.validate(
                partial_key="",
                environment="development",
                partial={
                    "content": "<p>Hello, world!</p>",
                    "name": "My Partial",
                    "type": "html",
                },
            )

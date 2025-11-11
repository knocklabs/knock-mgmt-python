# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Translation,
    TranslationUpsertResponse,
    TranslationRetrieveResponse,
    TranslationValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranslations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        translation = client.translations.retrieve(
            locale_code="locale_code",
            environment="development",
        )
        assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        translation = client.translations.retrieve(
            locale_code="locale_code",
            environment="development",
            annotate=True,
            branch="feature-branch",
            format="json",
            hide_uncommitted_changes=True,
            namespace="namespace",
        )
        assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.translations.with_raw_response.retrieve(
            locale_code="locale_code",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.translations.with_streaming_response.retrieve(
            locale_code="locale_code",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_code` but received ''"):
            client.translations.with_raw_response.retrieve(
                locale_code="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        translation = client.translations.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Translation], translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        translation = client.translations.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            format="json",
            hide_uncommitted_changes=True,
            limit=0,
            locale_code="locale_code",
            namespace="namespace",
        )
        assert_matches_type(SyncEntriesCursor[Translation], translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.translations.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(SyncEntriesCursor[Translation], translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.translations.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(SyncEntriesCursor[Translation], translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        translation = client.translations.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )
        assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        translation = client.translations.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            format="json",
        )
        assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.translations.with_raw_response.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.translations.with_streaming_response.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_code` but received ''"):
            client.translations.with_raw_response.upsert(
                locale_code="",
                environment="development",
                namespace="namespace",
                translation={
                    "content": '{"hello":"Hello, world!"}',
                    "format": "json",
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        translation = client.translations.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )
        assert_matches_type(TranslationValidateResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        translation = client.translations.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
            branch="feature-branch",
        )
        assert_matches_type(TranslationValidateResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.translations.with_raw_response.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationValidateResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.translations.with_streaming_response.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(TranslationValidateResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_code` but received ''"):
            client.translations.with_raw_response.validate(
                locale_code="",
                environment="development",
                translation={
                    "content": '{"hello":"Hello, world!"}',
                    "format": "json",
                },
            )


class TestAsyncTranslations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.retrieve(
            locale_code="locale_code",
            environment="development",
        )
        assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.retrieve(
            locale_code="locale_code",
            environment="development",
            annotate=True,
            branch="feature-branch",
            format="json",
            hide_uncommitted_changes=True,
            namespace="namespace",
        )
        assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.translations.with_raw_response.retrieve(
            locale_code="locale_code",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.translations.with_streaming_response.retrieve(
            locale_code="locale_code",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(TranslationRetrieveResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_code` but received ''"):
            await async_client.translations.with_raw_response.retrieve(
                locale_code="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Translation], translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            format="json",
            hide_uncommitted_changes=True,
            limit=0,
            locale_code="locale_code",
            namespace="namespace",
        )
        assert_matches_type(AsyncEntriesCursor[Translation], translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.translations.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Translation], translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.translations.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Translation], translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )
        assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            format="json",
        )
        assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.translations.with_raw_response.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.translations.with_streaming_response.upsert(
            locale_code="locale_code",
            environment="development",
            namespace="namespace",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(TranslationUpsertResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_code` but received ''"):
            await async_client.translations.with_raw_response.upsert(
                locale_code="",
                environment="development",
                namespace="namespace",
                translation={
                    "content": '{"hello":"Hello, world!"}',
                    "format": "json",
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )
        assert_matches_type(TranslationValidateResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        translation = await async_client.translations.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
            branch="feature-branch",
        )
        assert_matches_type(TranslationValidateResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.translations.with_raw_response.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(TranslationValidateResponse, translation, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.translations.with_streaming_response.validate(
            locale_code="locale_code",
            environment="development",
            translation={
                "content": '{"hello":"Hello, world!"}',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(TranslationValidateResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_code` but received ''"):
            await async_client.translations.with_raw_response.validate(
                locale_code="",
                environment="development",
                translation={
                    "content": '{"hello":"Hello, world!"}',
                    "format": "json",
                },
            )

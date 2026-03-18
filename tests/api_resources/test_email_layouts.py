# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    EmailLayout,
    EmailLayoutUpsertResponse,
    EmailLayoutValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailLayouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
        )
        assert_matches_type(EmailLayout, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(EmailLayout, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.email_layouts.with_raw_response.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = response.parse()
        assert_matches_type(EmailLayout, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.email_layouts.with_streaming_response.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = response.parse()
            assert_matches_type(EmailLayout, email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_layout_key` but received ''"):
            client.email_layouts.with_raw_response.retrieve(
                email_layout_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[EmailLayout], email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[EmailLayout], email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.email_layouts.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = response.parse()
        assert_matches_type(SyncEntriesCursor[EmailLayout], email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.email_layouts.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = response.parse()
            assert_matches_type(SyncEntriesCursor[EmailLayout], email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )
        assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
                "footer_links": [
                    {
                        "text": "Example",
                        "url": "http://example.com",
                    }
                ],
                "is_mjml": True,
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            force=True,
        )
        assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.email_layouts.with_raw_response.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = response.parse()
        assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.email_layouts.with_streaming_response.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = response.parse()
            assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_layout_key` but received ''"):
            client.email_layouts.with_raw_response.upsert(
                email_layout_key="",
                environment="development",
                email_layout={
                    "html_layout": "<html><body>Hello, world!</body></html>",
                    "name": "Transactional",
                    "text_layout": "Hello, world!",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )
        assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        email_layout = client.email_layouts.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
                "footer_links": [
                    {
                        "text": "Example",
                        "url": "http://example.com",
                    }
                ],
                "is_mjml": True,
            },
            branch="feature-branch",
        )
        assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.email_layouts.with_raw_response.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = response.parse()
        assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.email_layouts.with_streaming_response.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = response.parse()
            assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_layout_key` but received ''"):
            client.email_layouts.with_raw_response.validate(
                email_layout_key="",
                environment="development",
                email_layout={
                    "html_layout": "<html><body>Hello, world!</body></html>",
                    "name": "Transactional",
                    "text_layout": "Hello, world!",
                },
            )


class TestAsyncEmailLayouts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
        )
        assert_matches_type(EmailLayout, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(EmailLayout, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.email_layouts.with_raw_response.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = await response.parse()
        assert_matches_type(EmailLayout, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.email_layouts.with_streaming_response.retrieve(
            email_layout_key="email_layout_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = await response.parse()
            assert_matches_type(EmailLayout, email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_layout_key` but received ''"):
            await async_client.email_layouts.with_raw_response.retrieve(
                email_layout_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[EmailLayout], email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[EmailLayout], email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.email_layouts.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = await response.parse()
        assert_matches_type(AsyncEntriesCursor[EmailLayout], email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.email_layouts.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = await response.parse()
            assert_matches_type(AsyncEntriesCursor[EmailLayout], email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )
        assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
                "footer_links": [
                    {
                        "text": "Example",
                        "url": "http://example.com",
                    }
                ],
                "is_mjml": True,
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            force=True,
        )
        assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.email_layouts.with_raw_response.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = await response.parse()
        assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.email_layouts.with_streaming_response.upsert(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = await response.parse()
            assert_matches_type(EmailLayoutUpsertResponse, email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_layout_key` but received ''"):
            await async_client.email_layouts.with_raw_response.upsert(
                email_layout_key="",
                environment="development",
                email_layout={
                    "html_layout": "<html><body>Hello, world!</body></html>",
                    "name": "Transactional",
                    "text_layout": "Hello, world!",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )
        assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        email_layout = await async_client.email_layouts.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
                "footer_links": [
                    {
                        "text": "Example",
                        "url": "http://example.com",
                    }
                ],
                "is_mjml": True,
            },
            branch="feature-branch",
        )
        assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.email_layouts.with_raw_response.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_layout = await response.parse()
        assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.email_layouts.with_streaming_response.validate(
            email_layout_key="email_layout_key",
            environment="development",
            email_layout={
                "html_layout": "<html><body>Hello, world!</body></html>",
                "name": "Transactional",
                "text_layout": "Hello, world!",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_layout = await response.parse()
            assert_matches_type(EmailLayoutValidateResponse, email_layout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_layout_key` but received ''"):
            await async_client.email_layouts.with_raw_response.validate(
                email_layout_key="",
                environment="development",
                email_layout={
                    "html_layout": "<html><body>Hello, world!</body></html>",
                    "name": "Transactional",
                    "text_layout": "Hello, world!",
                },
            )

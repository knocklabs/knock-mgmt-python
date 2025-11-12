# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Branch,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBranches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_create(self, client: KnockMgmt) -> None:
        branch = client.branches.create(
            branch_slug="feature-branch",
            environment="development",
        )
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_create(self, client: KnockMgmt) -> None:
        response = client.branches.with_raw_response.create(
            branch_slug="feature-branch",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_create(self, client: KnockMgmt) -> None:
        with client.branches.with_streaming_response.create(
            branch_slug="feature-branch",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert_matches_type(Branch, branch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_create(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_slug` but received ''"):
            client.branches.with_raw_response.create(
                branch_slug="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        branch = client.branches.retrieve(
            branch_slug="feature-branch",
            environment="development",
        )
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.branches.with_raw_response.retrieve(
            branch_slug="feature-branch",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.branches.with_streaming_response.retrieve(
            branch_slug="feature-branch",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert_matches_type(Branch, branch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_slug` but received ''"):
            client.branches.with_raw_response.retrieve(
                branch_slug="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        branch = client.branches.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Branch], branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        branch = client.branches.list(
            environment="development",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Branch], branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.branches.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert_matches_type(SyncEntriesCursor[Branch], branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.branches.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert_matches_type(SyncEntriesCursor[Branch], branch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_delete(self, client: KnockMgmt) -> None:
        branch = client.branches.delete(
            branch_slug="feature-branch",
            environment="development",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_delete(self, client: KnockMgmt) -> None:
        response = client.branches.with_raw_response.delete(
            branch_slug="feature-branch",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert branch is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_delete(self, client: KnockMgmt) -> None:
        with client.branches.with_streaming_response.delete(
            branch_slug="feature-branch",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert branch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_delete(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_slug` but received ''"):
            client.branches.with_raw_response.delete(
                branch_slug="",
                environment="development",
            )


class TestAsyncBranches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_create(self, async_client: AsyncKnockMgmt) -> None:
        branch = await async_client.branches.create(
            branch_slug="feature-branch",
            environment="development",
        )
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.branches.with_raw_response.create(
            branch_slug="feature-branch",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.branches.with_streaming_response.create(
            branch_slug="feature-branch",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert_matches_type(Branch, branch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_slug` but received ''"):
            await async_client.branches.with_raw_response.create(
                branch_slug="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        branch = await async_client.branches.retrieve(
            branch_slug="feature-branch",
            environment="development",
        )
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.branches.with_raw_response.retrieve(
            branch_slug="feature-branch",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert_matches_type(Branch, branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.branches.with_streaming_response.retrieve(
            branch_slug="feature-branch",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert_matches_type(Branch, branch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_slug` but received ''"):
            await async_client.branches.with_raw_response.retrieve(
                branch_slug="",
                environment="development",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        branch = await async_client.branches.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Branch], branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        branch = await async_client.branches.list(
            environment="development",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Branch], branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.branches.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Branch], branch, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.branches.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Branch], branch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnockMgmt) -> None:
        branch = await async_client.branches.delete(
            branch_slug="feature-branch",
            environment="development",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.branches.with_raw_response.delete(
            branch_slug="feature-branch",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert branch is None

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.branches.with_streaming_response.delete(
            branch_slug="feature-branch",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert branch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `branch_slug` but received ''"):
            await async_client.branches.with_raw_response.delete(
                branch_slug="",
                environment="development",
            )

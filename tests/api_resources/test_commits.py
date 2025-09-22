# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Commit,
    CommitCommitAllResponse,
    CommitPromoteAllResponse,
    CommitPromoteOneResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        commit = client.commits.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Commit, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.commits.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(Commit, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.commits.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(Commit, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.commits.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        commit = client.commits.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Commit], commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        commit = client.commits.list(
            environment="development",
            after="after",
            before="before",
            limit=0,
            promoted=True,
            resource_id="resource_id",
            resource_type="dynamic_audience",
        )
        assert_matches_type(SyncEntriesCursor[Commit], commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.commits.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(SyncEntriesCursor[Commit], commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.commits.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(SyncEntriesCursor[Commit], commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_commit_all(self, client: KnockMgmt) -> None:
        commit = client.commits.commit_all(
            environment="development",
        )
        assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_commit_all_with_all_params(self, client: KnockMgmt) -> None:
        commit = client.commits.commit_all(
            environment="development",
            commit_message="commit_message",
        )
        assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_commit_all(self, client: KnockMgmt) -> None:
        response = client.commits.with_raw_response.commit_all(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_commit_all(self, client: KnockMgmt) -> None:
        with client.commits.with_streaming_response.commit_all(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_promote_all(self, client: KnockMgmt) -> None:
        commit = client.commits.promote_all(
            to_environment="to_environment",
        )
        assert_matches_type(CommitPromoteAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_promote_all(self, client: KnockMgmt) -> None:
        response = client.commits.with_raw_response.promote_all(
            to_environment="to_environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitPromoteAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_promote_all(self, client: KnockMgmt) -> None:
        with client.commits.with_streaming_response.promote_all(
            to_environment="to_environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitPromoteAllResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_promote_one(self, client: KnockMgmt) -> None:
        commit = client.commits.promote_one(
            "id",
        )
        assert_matches_type(CommitPromoteOneResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_promote_one(self, client: KnockMgmt) -> None:
        response = client.commits.with_raw_response.promote_one(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitPromoteOneResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_promote_one(self, client: KnockMgmt) -> None:
        with client.commits.with_streaming_response.promote_one(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitPromoteOneResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_promote_one(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.commits.with_raw_response.promote_one(
                "",
            )


class TestAsyncCommits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Commit, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.commits.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(Commit, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.commits.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(Commit, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.commits.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Commit], commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.list(
            environment="development",
            after="after",
            before="before",
            limit=0,
            promoted=True,
            resource_id="resource_id",
            resource_type="dynamic_audience",
        )
        assert_matches_type(AsyncEntriesCursor[Commit], commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.commits.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Commit], commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.commits.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Commit], commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_commit_all(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.commit_all(
            environment="development",
        )
        assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_commit_all_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.commit_all(
            environment="development",
            commit_message="commit_message",
        )
        assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_commit_all(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.commits.with_raw_response.commit_all(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_commit_all(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.commits.with_streaming_response.commit_all(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitCommitAllResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_promote_all(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.promote_all(
            to_environment="to_environment",
        )
        assert_matches_type(CommitPromoteAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_promote_all(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.commits.with_raw_response.promote_all(
            to_environment="to_environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitPromoteAllResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_promote_all(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.commits.with_streaming_response.promote_all(
            to_environment="to_environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitPromoteAllResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_promote_one(self, async_client: AsyncKnockMgmt) -> None:
        commit = await async_client.commits.promote_one(
            "id",
        )
        assert_matches_type(CommitPromoteOneResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_promote_one(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.commits.with_raw_response.promote_one(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitPromoteOneResponse, commit, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_promote_one(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.commits.with_streaming_response.promote_one(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitPromoteOneResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_promote_one(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.commits.with_raw_response.promote_one(
                "",
            )

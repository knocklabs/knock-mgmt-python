# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Goal,
    GoalCloneResponse,
    GoalUpsertResponse,
    GoalArchiveResponse,
    GoalValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGoals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        goal = client.goals.retrieve(
            goal_key="goal_key",
            environment="development",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        goal = client.goals.retrieve(
            goal_key="goal_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.goals.with_raw_response.retrieve(
            goal_key="goal_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.goals.with_streaming_response.retrieve(
            goal_key="goal_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.with_raw_response.retrieve(
                goal_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        goal = client.goals.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Goal], goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        goal = client.goals.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Goal], goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.goals.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(SyncEntriesCursor[Goal], goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.goals.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(SyncEntriesCursor[Goal], goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: KnockMgmt) -> None:
        goal = client.goals.archive(
            goal_key="goal_key",
            environment="development",
        )
        assert_matches_type(GoalArchiveResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: KnockMgmt) -> None:
        response = client.goals.with_raw_response.archive(
            goal_key="goal_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(GoalArchiveResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: KnockMgmt) -> None:
        with client.goals.with_streaming_response.archive(
            goal_key="goal_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(GoalArchiveResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.with_raw_response.archive(
                goal_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: KnockMgmt) -> None:
        goal = client.goals.clone(
            goal_key="goal_key",
            environment="development",
            clone={
                "environment": "production",
                "key": "trial-conversion-copy",
                "name": "Trial Conversion Copy",
            },
        )
        assert_matches_type(GoalCloneResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: KnockMgmt) -> None:
        response = client.goals.with_raw_response.clone(
            goal_key="goal_key",
            environment="development",
            clone={
                "environment": "production",
                "key": "trial-conversion-copy",
                "name": "Trial Conversion Copy",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(GoalCloneResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: KnockMgmt) -> None:
        with client.goals.with_streaming_response.clone(
            goal_key="goal_key",
            environment="development",
            clone={
                "environment": "production",
                "key": "trial-conversion-copy",
                "name": "Trial Conversion Copy",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(GoalCloneResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.with_raw_response.clone(
                goal_key="",
                environment="development",
                clone={
                    "environment": "production",
                    "key": "trial-conversion-copy",
                    "name": "Trial Conversion Copy",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        goal = client.goals.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )
        assert_matches_type(GoalUpsertResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        goal = client.goals.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {
                    "event": {
                        "event_type": "recipient",
                        "event_key": "updated",
                    },
                    "match_conditions": [
                        {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        }
                    ],
                },
                "name": "Trial Conversion",
                "description": "Tracks when a trial user converts to paid",
            },
            annotate=True,
        )
        assert_matches_type(GoalUpsertResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.goals.with_raw_response.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(GoalUpsertResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.goals.with_streaming_response.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(GoalUpsertResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.with_raw_response.upsert(
                goal_key="",
                environment="development",
                goal={
                    "condition": {"event": {"event_type": "recipient"}},
                    "name": "Trial Conversion",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        goal = client.goals.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )
        assert_matches_type(GoalValidateResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        goal = client.goals.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {
                    "event": {
                        "event_type": "recipient",
                        "event_key": "updated",
                    },
                    "match_conditions": [
                        {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        }
                    ],
                },
                "name": "Trial Conversion",
                "description": "Tracks when a trial user converts to paid",
            },
            branch="feature-branch",
        )
        assert_matches_type(GoalValidateResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.goals.with_raw_response.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(GoalValidateResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.goals.with_streaming_response.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(GoalValidateResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.with_raw_response.validate(
                goal_key="",
                environment="development",
                goal={
                    "condition": {"event": {"event_type": "recipient"}},
                    "name": "Trial Conversion",
                },
            )


class TestAsyncGoals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.retrieve(
            goal_key="goal_key",
            environment="development",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.retrieve(
            goal_key="goal_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
        )
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.with_raw_response.retrieve(
            goal_key="goal_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(Goal, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.with_streaming_response.retrieve(
            goal_key="goal_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(Goal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.with_raw_response.retrieve(
                goal_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Goal], goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Goal], goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Goal], goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Goal], goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.archive(
            goal_key="goal_key",
            environment="development",
        )
        assert_matches_type(GoalArchiveResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.with_raw_response.archive(
            goal_key="goal_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(GoalArchiveResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.with_streaming_response.archive(
            goal_key="goal_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(GoalArchiveResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.with_raw_response.archive(
                goal_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.clone(
            goal_key="goal_key",
            environment="development",
            clone={
                "environment": "production",
                "key": "trial-conversion-copy",
                "name": "Trial Conversion Copy",
            },
        )
        assert_matches_type(GoalCloneResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.with_raw_response.clone(
            goal_key="goal_key",
            environment="development",
            clone={
                "environment": "production",
                "key": "trial-conversion-copy",
                "name": "Trial Conversion Copy",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(GoalCloneResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.with_streaming_response.clone(
            goal_key="goal_key",
            environment="development",
            clone={
                "environment": "production",
                "key": "trial-conversion-copy",
                "name": "Trial Conversion Copy",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(GoalCloneResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.with_raw_response.clone(
                goal_key="",
                environment="development",
                clone={
                    "environment": "production",
                    "key": "trial-conversion-copy",
                    "name": "Trial Conversion Copy",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )
        assert_matches_type(GoalUpsertResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {
                    "event": {
                        "event_type": "recipient",
                        "event_key": "updated",
                    },
                    "match_conditions": [
                        {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        }
                    ],
                },
                "name": "Trial Conversion",
                "description": "Tracks when a trial user converts to paid",
            },
            annotate=True,
        )
        assert_matches_type(GoalUpsertResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.with_raw_response.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(GoalUpsertResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.with_streaming_response.upsert(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(GoalUpsertResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.with_raw_response.upsert(
                goal_key="",
                environment="development",
                goal={
                    "condition": {"event": {"event_type": "recipient"}},
                    "name": "Trial Conversion",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )
        assert_matches_type(GoalValidateResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        goal = await async_client.goals.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {
                    "event": {
                        "event_type": "recipient",
                        "event_key": "updated",
                    },
                    "match_conditions": [
                        {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        }
                    ],
                },
                "name": "Trial Conversion",
                "description": "Tracks when a trial user converts to paid",
            },
            branch="feature-branch",
        )
        assert_matches_type(GoalValidateResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.with_raw_response.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(GoalValidateResponse, goal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.with_streaming_response.validate(
            goal_key="goal_key",
            environment="development",
            goal={
                "condition": {"event": {"event_type": "recipient"}},
                "name": "Trial Conversion",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(GoalValidateResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.with_raw_response.validate(
                goal_key="",
                environment="development",
                goal={
                    "condition": {"event": {"event_type": "recipient"}},
                    "name": "Trial Conversion",
                },
            )

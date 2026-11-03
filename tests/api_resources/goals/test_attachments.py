# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types.goals import (
    AttachmentListResponse,
    AttachmentDeleteResponse,
    AttachmentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: KnockMgmt) -> None:
        attachment = client.goals.attachments.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={},
        )
        assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: KnockMgmt) -> None:
        attachment = client.goals.attachments.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={"attribution_window_days": 7},
            environment="development",
        )
        assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: KnockMgmt) -> None:
        response = client.goals.attachments.with_raw_response.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: KnockMgmt) -> None:
        with client.goals.attachments.with_streaming_response.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.attachments.with_raw_response.update(
                resource_key="resource_key",
                goal_key="",
                resource_type="workflow",
                attachment={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_key` but received ''"):
            client.goals.attachments.with_raw_response.update(
                resource_key="",
                goal_key="goal_key",
                resource_type="workflow",
                attachment={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        attachment = client.goals.attachments.list(
            goal_key="goal_key",
        )
        assert_matches_type(AttachmentListResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        attachment = client.goals.attachments.list(
            goal_key="goal_key",
            environment="development",
        )
        assert_matches_type(AttachmentListResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.goals.attachments.with_raw_response.list(
            goal_key="goal_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentListResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.goals.attachments.with_streaming_response.list(
            goal_key="goal_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentListResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.attachments.with_raw_response.list(
                goal_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: KnockMgmt) -> None:
        attachment = client.goals.attachments.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: KnockMgmt) -> None:
        attachment = client.goals.attachments.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            environment="development",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: KnockMgmt) -> None:
        response = client.goals.attachments.with_raw_response.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: KnockMgmt) -> None:
        with client.goals.attachments.with_streaming_response.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            client.goals.attachments.with_raw_response.delete(
                resource_key="resource_key",
                goal_key="",
                resource_type="workflow",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_key` but received ''"):
            client.goals.attachments.with_raw_response.delete(
                resource_key="",
                goal_key="goal_key",
                resource_type="workflow",
            )


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKnockMgmt) -> None:
        attachment = await async_client.goals.attachments.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={},
        )
        assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        attachment = await async_client.goals.attachments.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={"attribution_window_days": 7},
            environment="development",
        )
        assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.attachments.with_raw_response.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.attachments.with_streaming_response.update(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            attachment={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentUpdateResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.attachments.with_raw_response.update(
                resource_key="resource_key",
                goal_key="",
                resource_type="workflow",
                attachment={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_key` but received ''"):
            await async_client.goals.attachments.with_raw_response.update(
                resource_key="",
                goal_key="goal_key",
                resource_type="workflow",
                attachment={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        attachment = await async_client.goals.attachments.list(
            goal_key="goal_key",
        )
        assert_matches_type(AttachmentListResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        attachment = await async_client.goals.attachments.list(
            goal_key="goal_key",
            environment="development",
        )
        assert_matches_type(AttachmentListResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.attachments.with_raw_response.list(
            goal_key="goal_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentListResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.attachments.with_streaming_response.list(
            goal_key="goal_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentListResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.attachments.with_raw_response.list(
                goal_key="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnockMgmt) -> None:
        attachment = await async_client.goals.attachments.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        attachment = await async_client.goals.attachments.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
            environment="development",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.goals.attachments.with_raw_response.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.goals.attachments.with_streaming_response.delete(
            resource_key="resource_key",
            goal_key="goal_key",
            resource_type="workflow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `goal_key` but received ''"):
            await async_client.goals.attachments.with_raw_response.delete(
                resource_key="resource_key",
                goal_key="",
                resource_type="workflow",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_key` but received ''"):
            await async_client.goals.attachments.with_raw_response.delete(
                resource_key="",
                goal_key="goal_key",
                resource_type="workflow",
            )

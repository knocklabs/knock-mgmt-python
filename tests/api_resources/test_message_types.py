# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    MessageType,
    MessageTypeUpsertResponse,
    MessageTypeValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessageTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        message_type = client.message_types.retrieve(
            message_type_key="email",
            environment="development",
        )
        assert_matches_type(MessageType, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        message_type = client.message_types.retrieve(
            message_type_key="email",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(MessageType, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.message_types.with_raw_response.retrieve(
            message_type_key="email",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = response.parse()
        assert_matches_type(MessageType, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.message_types.with_streaming_response.retrieve(
            message_type_key="email",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = response.parse()
            assert_matches_type(MessageType, message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_type_key` but received ''"):
            client.message_types.with_raw_response.retrieve(
                message_type_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        message_type = client.message_types.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[MessageType], message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        message_type = client.message_types.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[MessageType], message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.message_types.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = response.parse()
        assert_matches_type(SyncEntriesCursor[MessageType], message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.message_types.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = response.parse()
            assert_matches_type(SyncEntriesCursor[MessageType], message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        message_type = client.message_types.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )
        assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        message_type = client.message_types.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
                "icon_name": "icon_name",
                "semver": "1.0.0",
                "variants": [
                    {
                        "fields": [
                            {
                                "key": "text_field",
                                "label": "My text field",
                                "type": "text",
                                "settings": {
                                    "default": "A placeholder",
                                    "description": "A description of the text field",
                                    "max_length": 100,
                                    "min_length": 10,
                                    "placeholder": "A placeholder for the field.",
                                    "required": True,
                                },
                            }
                        ],
                        "key": "default",
                        "name": "Default",
                    }
                ],
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            force=True,
        )
        assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.message_types.with_raw_response.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = response.parse()
        assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.message_types.with_streaming_response.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = response.parse()
            assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_type_key` but received ''"):
            client.message_types.with_raw_response.upsert(
                message_type_key="",
                environment="development",
                message_type={
                    "description": "This is a message type",
                    "name": "My Message Type",
                    "preview": "<div>Hello, world!</div>",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        message_type = client.message_types.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )
        assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        message_type = client.message_types.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
                "icon_name": "icon_name",
                "semver": "1.0.0",
                "variants": [
                    {
                        "fields": [
                            {
                                "key": "text_field",
                                "label": "My text field",
                                "type": "text",
                                "settings": {
                                    "default": "A placeholder",
                                    "description": "A description of the text field",
                                    "max_length": 100,
                                    "min_length": 10,
                                    "placeholder": "A placeholder for the field.",
                                    "required": True,
                                },
                            }
                        ],
                        "key": "default",
                        "name": "Default",
                    }
                ],
            },
            branch="feature-branch",
        )
        assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.message_types.with_raw_response.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = response.parse()
        assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.message_types.with_streaming_response.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = response.parse()
            assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_type_key` but received ''"):
            client.message_types.with_raw_response.validate(
                message_type_key="",
                environment="development",
                message_type={
                    "description": "This is a message type",
                    "name": "My Message Type",
                    "preview": "<div>Hello, world!</div>",
                },
            )


class TestAsyncMessageTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.retrieve(
            message_type_key="email",
            environment="development",
        )
        assert_matches_type(MessageType, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.retrieve(
            message_type_key="email",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(MessageType, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.message_types.with_raw_response.retrieve(
            message_type_key="email",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = await response.parse()
        assert_matches_type(MessageType, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.message_types.with_streaming_response.retrieve(
            message_type_key="email",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = await response.parse()
            assert_matches_type(MessageType, message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_type_key` but received ''"):
            await async_client.message_types.with_raw_response.retrieve(
                message_type_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[MessageType], message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[MessageType], message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.message_types.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = await response.parse()
        assert_matches_type(AsyncEntriesCursor[MessageType], message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.message_types.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = await response.parse()
            assert_matches_type(AsyncEntriesCursor[MessageType], message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )
        assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
                "icon_name": "icon_name",
                "semver": "1.0.0",
                "variants": [
                    {
                        "fields": [
                            {
                                "key": "text_field",
                                "label": "My text field",
                                "type": "text",
                                "settings": {
                                    "default": "A placeholder",
                                    "description": "A description of the text field",
                                    "max_length": 100,
                                    "min_length": 10,
                                    "placeholder": "A placeholder for the field.",
                                    "required": True,
                                },
                            }
                        ],
                        "key": "default",
                        "name": "Default",
                    }
                ],
            },
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            force=True,
        )
        assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.message_types.with_raw_response.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = await response.parse()
        assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.message_types.with_streaming_response.upsert(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = await response.parse()
            assert_matches_type(MessageTypeUpsertResponse, message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_type_key` but received ''"):
            await async_client.message_types.with_raw_response.upsert(
                message_type_key="",
                environment="development",
                message_type={
                    "description": "This is a message type",
                    "name": "My Message Type",
                    "preview": "<div>Hello, world!</div>",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )
        assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        message_type = await async_client.message_types.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
                "icon_name": "icon_name",
                "semver": "1.0.0",
                "variants": [
                    {
                        "fields": [
                            {
                                "key": "text_field",
                                "label": "My text field",
                                "type": "text",
                                "settings": {
                                    "default": "A placeholder",
                                    "description": "A description of the text field",
                                    "max_length": 100,
                                    "min_length": 10,
                                    "placeholder": "A placeholder for the field.",
                                    "required": True,
                                },
                            }
                        ],
                        "key": "default",
                        "name": "Default",
                    }
                ],
            },
            branch="feature-branch",
        )
        assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.message_types.with_raw_response.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_type = await response.parse()
        assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.message_types.with_streaming_response.validate(
            message_type_key="email",
            environment="development",
            message_type={
                "description": "This is a message type",
                "name": "My Message Type",
                "preview": "<div>Hello, world!</div>",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_type = await response.parse()
            assert_matches_type(MessageTypeValidateResponse, message_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_type_key` but received ''"):
            await async_client.message_types.with_raw_response.validate(
                message_type_key="",
                environment="development",
                message_type={
                    "description": "This is a message type",
                    "name": "My Message Type",
                    "preview": "<div>Hello, world!</div>",
                },
            )

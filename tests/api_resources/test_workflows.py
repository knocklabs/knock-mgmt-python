# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import (
    Workflow,
    WorkflowRunResponse,
    WorkflowUpsertResponse,
    WorkflowActivateResponse,
    WorkflowRetrieveResponse,
    WorkflowValidateResponse,
)
from knock_mapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KnockMgmt) -> None:
        workflow = client.workflows.retrieve(
            workflow_key="workflow_key",
            environment="development",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: KnockMgmt) -> None:
        workflow = client.workflows.retrieve(
            workflow_key="workflow_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KnockMgmt) -> None:
        response = client.workflows.with_raw_response.retrieve(
            workflow_key="workflow_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KnockMgmt) -> None:
        with client.workflows.with_streaming_response.retrieve(
            workflow_key="workflow_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            client.workflows.with_raw_response.retrieve(
                workflow_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: KnockMgmt) -> None:
        workflow = client.workflows.list(
            environment="development",
        )
        assert_matches_type(SyncEntriesCursor[Workflow], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: KnockMgmt) -> None:
        workflow = client.workflows.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(SyncEntriesCursor[Workflow], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KnockMgmt) -> None:
        response = client.workflows.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(SyncEntriesCursor[Workflow], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KnockMgmt) -> None:
        with client.workflows.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(SyncEntriesCursor[Workflow], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate(self, client: KnockMgmt) -> None:
        workflow = client.workflows.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
        )
        assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate_with_all_params(self, client: KnockMgmt) -> None:
        workflow = client.workflows.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
            branch="feature-branch",
        )
        assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activate(self, client: KnockMgmt) -> None:
        response = client.workflows.with_raw_response.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activate(self, client: KnockMgmt) -> None:
        with client.workflows.with_streaming_response.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_activate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            client.workflows.with_raw_response.activate(
                workflow_key="",
                environment="development",
                status=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: KnockMgmt) -> None:
        workflow = client.workflows.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: KnockMgmt) -> None:
        workflow = client.workflows.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
            branch="feature-branch",
            actor={
                "id": "project_1",
                "collection": "projects",
            },
            cancellation_key="cancellation_key",
            data={"park_id": "bar"},
            tenant="tenant",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: KnockMgmt) -> None:
        response = client.workflows.with_raw_response.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: KnockMgmt) -> None:
        with client.workflows.with_streaming_response.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            client.workflows.with_raw_response.run(
                workflow_key="",
                environment="development",
                recipients=["dnedry"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: KnockMgmt) -> None:
        workflow = client.workflows.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: KnockMgmt) -> None:
        workflow = client.workflows.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["string"],
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "description",
                "settings": {
                    "is_commercial": False,
                    "override_preferences": False,
                },
                "tags": ["string"],
                "trigger_data_json_schema": {"foo": "bar"},
                "trigger_frequency": "every_trigger",
            },
            allow_empty=True,
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            force=True,
        )
        assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: KnockMgmt) -> None:
        response = client.workflows.with_raw_response.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: KnockMgmt) -> None:
        with client.workflows.with_streaming_response.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            client.workflows.with_raw_response.upsert(
                workflow_key="",
                environment="development",
                workflow={
                    "name": "My Workflow",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: KnockMgmt) -> None:
        workflow = client.workflows.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: KnockMgmt) -> None:
        workflow = client.workflows.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["string"],
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "description",
                "settings": {
                    "is_commercial": False,
                    "override_preferences": False,
                },
                "tags": ["string"],
                "trigger_data_json_schema": {"foo": "bar"},
                "trigger_frequency": "every_trigger",
            },
            branch="feature-branch",
        )
        assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: KnockMgmt) -> None:
        response = client.workflows.with_raw_response.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: KnockMgmt) -> None:
        with client.workflows.with_streaming_response.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            client.workflows.with_raw_response.validate(
                workflow_key="",
                environment="development",
                workflow={
                    "name": "My Workflow",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.retrieve(
            workflow_key="workflow_key",
            environment="development",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.retrieve(
            workflow_key="workflow_key",
            environment="development",
            annotate=True,
            branch="feature-branch",
            hide_uncommitted_changes=True,
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.with_raw_response.retrieve(
            workflow_key="workflow_key",
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.with_streaming_response.retrieve(
            workflow_key="workflow_key",
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            await async_client.workflows.with_raw_response.retrieve(
                workflow_key="",
                environment="development",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.list(
            environment="development",
        )
        assert_matches_type(AsyncEntriesCursor[Workflow], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.list(
            environment="development",
            after="after",
            annotate=True,
            before="before",
            branch="feature-branch",
            hide_uncommitted_changes=True,
            limit=0,
        )
        assert_matches_type(AsyncEntriesCursor[Workflow], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.with_raw_response.list(
            environment="development",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Workflow], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.with_streaming_response.list(
            environment="development",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Workflow], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
        )
        assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
            branch="feature-branch",
        )
        assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.with_raw_response.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.with_streaming_response.activate(
            workflow_key="workflow_key",
            environment="development",
            status=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowActivateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_activate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            await async_client.workflows.with_raw_response.activate(
                workflow_key="",
                environment="development",
                status=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
            branch="feature-branch",
            actor={
                "id": "project_1",
                "collection": "projects",
            },
            cancellation_key="cancellation_key",
            data={"park_id": "bar"},
            tenant="tenant",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.with_raw_response.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.with_streaming_response.run(
            workflow_key="workflow_key",
            environment="development",
            recipients=["dnedry"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            await async_client.workflows.with_raw_response.run(
                workflow_key="",
                environment="development",
                recipients=["dnedry"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["string"],
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "description",
                "settings": {
                    "is_commercial": False,
                    "override_preferences": False,
                },
                "tags": ["string"],
                "trigger_data_json_schema": {"foo": "bar"},
                "trigger_frequency": "every_trigger",
            },
            allow_empty=True,
            annotate=True,
            branch="feature-branch",
            commit=True,
            commit_message="commit_message",
            force=True,
        )
        assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.with_raw_response.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.with_streaming_response.upsert(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowUpsertResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            await async_client.workflows.with_raw_response.upsert(
                workflow_key="",
                environment="development",
                workflow={
                    "name": "My Workflow",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )
        assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        workflow = await async_client.workflows.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {
                            "markdown_body": "Hello **{{ recipient.name }}**",
                            "action_buttons": [
                                {
                                    "action": "https://example.com",
                                    "label": "Button 1",
                                }
                            ],
                            "action_url": "{{ vars.app_url }}",
                        },
                        "type": "channel",
                        "channel_group_key": None,
                        "channel_key": "in-app-feed",
                        "channel_overrides": {"link_tracking": True},
                        "channel_type": "in_app_feed",
                        "conditions": {
                            "all": [
                                {
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                    "argument": "some_property",
                                }
                            ]
                        },
                        "description": "This is a description of the channel step",
                        "name": "Channel 1",
                        "send_windows": [
                            {
                                "day": "monday",
                                "type": "send",
                                "from": "18:11:19.117Z",
                                "until": "18:11:19.117Z",
                            }
                        ],
                    }
                ],
                "categories": ["string"],
                "conditions": {
                    "all": [
                        {
                            "operator": "equal_to",
                            "variable": "recipient.property",
                            "argument": "some_property",
                        }
                    ]
                },
                "description": "description",
                "settings": {
                    "is_commercial": False,
                    "override_preferences": False,
                },
                "tags": ["string"],
                "trigger_data_json_schema": {"foo": "bar"},
                "trigger_frequency": "every_trigger",
            },
            branch="feature-branch",
        )
        assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.with_raw_response.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.with_streaming_response.validate(
            workflow_key="workflow_key",
            environment="development",
            workflow={
                "name": "My Workflow",
                "steps": [
                    {
                        "ref": "channel_1",
                        "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                        "type": "channel",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowValidateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            await async_client.workflows.with_raw_response.validate(
                workflow_key="",
                environment="development",
                workflow={
                    "name": "My Workflow",
                    "steps": [
                        {
                            "ref": "channel_1",
                            "template": {"markdown_body": "Hello **{{ recipient.name }}**"},
                            "type": "channel",
                        }
                    ],
                },
            )

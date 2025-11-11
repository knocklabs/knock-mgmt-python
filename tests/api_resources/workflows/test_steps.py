# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types.workflows import StepPreviewTemplateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_preview_template(self, client: KnockMgmt) -> None:
        step = client.workflows.steps.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
        )
        assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_preview_template_with_all_params(self, client: KnockMgmt) -> None:
        step = client.workflows.steps.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
            branch="feature-branch",
            actor="dnedry",
            data={"park_id": "bar"},
            tenant="acme-corp",
        )
        assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_preview_template(self, client: KnockMgmt) -> None:
        response = client.workflows.steps.with_raw_response.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_preview_template(self, client: KnockMgmt) -> None:
        with client.workflows.steps.with_streaming_response.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_path_params_preview_template(self, client: KnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            client.workflows.steps.with_raw_response.preview_template(
                step_ref="step_ref",
                workflow_key="",
                environment="development",
                recipient="dnedry",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_ref` but received ''"):
            client.workflows.steps.with_raw_response.preview_template(
                step_ref="",
                workflow_key="workflow_key",
                environment="development",
                recipient="dnedry",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_preview_template(self, async_client: AsyncKnockMgmt) -> None:
        step = await async_client.workflows.steps.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
        )
        assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_preview_template_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        step = await async_client.workflows.steps.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
            branch="feature-branch",
            actor="dnedry",
            data={"park_id": "bar"},
            tenant="acme-corp",
        )
        assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_preview_template(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.workflows.steps.with_raw_response.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_preview_template(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.workflows.steps.with_streaming_response.preview_template(
            step_ref="step_ref",
            workflow_key="workflow_key",
            environment="development",
            recipient="dnedry",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(StepPreviewTemplateResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_path_params_preview_template(self, async_client: AsyncKnockMgmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_key` but received ''"):
            await async_client.workflows.steps.with_raw_response.preview_template(
                step_ref="step_ref",
                workflow_key="",
                environment="development",
                recipient="dnedry",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_ref` but received ''"):
            await async_client.workflows.steps.with_raw_response.preview_template(
                step_ref="",
                workflow_key="workflow_key",
                environment="development",
                recipient="dnedry",
            )

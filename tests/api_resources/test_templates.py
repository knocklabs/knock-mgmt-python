# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock_mapi import KnockMgmt, AsyncKnockMgmt
from tests.utils import assert_matches_type
from knock_mapi.types import TemplatePreviewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview(self, client: KnockMgmt) -> None:
        template = client.templates.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {},
                "subject": "Hello {{ recipient.name }}",
            },
        )
        assert_matches_type(TemplatePreviewResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview_with_all_params(self, client: KnockMgmt) -> None:
        template = client.templates.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {
                    "attachment_key": "attachments",
                    "layout_key": "default",
                    "pre_content": "pre_content",
                },
                "subject": "Hello {{ recipient.name }}",
                "html_body": "<p>Welcome!</p>",
                "is_mjml": True,
                "text_body": "Hello, {{ recipient.name }}! Welcome to {{ vars.app_name }} Get started here: {{ data.sign_in_url }}.",
                "visual_blocks": [
                    {
                        "content": "# Hello, {{ recipient.name }}!\n\nWelcome to **{{ vars.app_name }}**. [Get started here]({{ data.sign_in_url }}).",
                        "type": "markdown",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "variant": "default",
                        "version": 1,
                    },
                    {
                        "content": "<p>Hello, {{ recipient.name }}!</p><p>Welcome to <strong>{{ vars.app_name }}</strong>. <a href='{{ data.sign_in_url }}'>Get started here</a>.</p>",
                        "type": "html",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                    {
                        "type": "divider",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                    {
                        "attrs": {"foo": "bar"},
                        "key": "my-partial",
                        "name": "My partial",
                        "type": "partial",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                    {
                        "type": "image",
                        "url": "https://example.com/image.png",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "action": "action",
                        "alt": "Example image",
                        "layout_attrs": {
                            "horizontal_align": "center",
                            "padding_bottom": 4,
                            "padding_left": 0,
                            "padding_right": 0,
                            "padding_top": 4,
                        },
                        "style_attrs": {"width": "25%"},
                        "version": 1,
                    },
                    {
                        "buttons": [
                            {
                                "action": "https://example.com/button-action",
                                "label": "Click me",
                                "variant": "solid",
                                "size_attrs": {
                                    "is_fullwidth": False,
                                    "size": "sm",
                                },
                                "style_attrs": {
                                    "background_color": "#000000",
                                    "border_color": "#000000",
                                    "border_radius": 6,
                                    "border_width": 1,
                                    "text_color": "#FFFFFF",
                                },
                            }
                        ],
                        "type": "button_set",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "column_gap": 8,
                            "horizontal_align": "left",
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                ],
            },
            branch="feature-branch",
            actor={
                "id": "project_1",
                "collection": "projects",
            },
            data={"order_id": "bar"},
            layout={
                "html_content": "html_content",
                "key": "key",
                "text_content": "text_content",
            },
            tenant="tenant",
        )
        assert_matches_type(TemplatePreviewResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_preview(self, client: KnockMgmt) -> None:
        response = client.templates.with_raw_response.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {},
                "subject": "Hello {{ recipient.name }}",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplatePreviewResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_preview(self, client: KnockMgmt) -> None:
        with client.templates.with_streaming_response.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {},
                "subject": "Hello {{ recipient.name }}",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplatePreviewResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncKnockMgmt) -> None:
        template = await async_client.templates.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {},
                "subject": "Hello {{ recipient.name }}",
            },
        )
        assert_matches_type(TemplatePreviewResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncKnockMgmt) -> None:
        template = await async_client.templates.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {
                    "attachment_key": "attachments",
                    "layout_key": "default",
                    "pre_content": "pre_content",
                },
                "subject": "Hello {{ recipient.name }}",
                "html_body": "<p>Welcome!</p>",
                "is_mjml": True,
                "text_body": "Hello, {{ recipient.name }}! Welcome to {{ vars.app_name }} Get started here: {{ data.sign_in_url }}.",
                "visual_blocks": [
                    {
                        "content": "# Hello, {{ recipient.name }}!\n\nWelcome to **{{ vars.app_name }}**. [Get started here]({{ data.sign_in_url }}).",
                        "type": "markdown",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "variant": "default",
                        "version": 1,
                    },
                    {
                        "content": "<p>Hello, {{ recipient.name }}!</p><p>Welcome to <strong>{{ vars.app_name }}</strong>. <a href='{{ data.sign_in_url }}'>Get started here</a>.</p>",
                        "type": "html",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                    {
                        "type": "divider",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                    {
                        "attrs": {"foo": "bar"},
                        "key": "my-partial",
                        "name": "My partial",
                        "type": "partial",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                    {
                        "type": "image",
                        "url": "https://example.com/image.png",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "action": "action",
                        "alt": "Example image",
                        "layout_attrs": {
                            "horizontal_align": "center",
                            "padding_bottom": 4,
                            "padding_left": 0,
                            "padding_right": 0,
                            "padding_top": 4,
                        },
                        "style_attrs": {"width": "25%"},
                        "version": 1,
                    },
                    {
                        "buttons": [
                            {
                                "action": "https://example.com/button-action",
                                "label": "Click me",
                                "variant": "solid",
                                "size_attrs": {
                                    "is_fullwidth": False,
                                    "size": "sm",
                                },
                                "style_attrs": {
                                    "background_color": "#000000",
                                    "border_color": "#000000",
                                    "border_radius": 6,
                                    "border_width": 1,
                                    "text_color": "#FFFFFF",
                                },
                            }
                        ],
                        "type": "button_set",
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "layout_attrs": {
                            "column_gap": 8,
                            "horizontal_align": "left",
                            "padding_bottom": 8,
                            "padding_left": 4,
                            "padding_right": 4,
                            "padding_top": 8,
                        },
                        "version": 1,
                    },
                ],
            },
            branch="feature-branch",
            actor={
                "id": "project_1",
                "collection": "projects",
            },
            data={"order_id": "bar"},
            layout={
                "html_content": "html_content",
                "key": "key",
                "text_content": "text_content",
            },
            tenant="tenant",
        )
        assert_matches_type(TemplatePreviewResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncKnockMgmt) -> None:
        response = await async_client.templates.with_raw_response.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {},
                "subject": "Hello {{ recipient.name }}",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplatePreviewResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncKnockMgmt) -> None:
        async with async_client.templates.with_streaming_response.preview(
            environment="development",
            channel_type="email",
            recipient="user_123",
            template={
                "settings": {},
                "subject": "Hello {{ recipient.name }}",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplatePreviewResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "EmailTemplateParam",
    "Settings",
    "VisualBlock",
    "VisualBlockEmailButtonSetBlock",
    "VisualBlockEmailButtonSetBlockButton",
    "VisualBlockEmailButtonSetBlockButtonSizeAttrs",
    "VisualBlockEmailButtonSetBlockButtonStyleAttrs",
    "VisualBlockEmailButtonSetBlockLayoutAttrs",
    "VisualBlockEmailDividerBlock",
    "VisualBlockEmailDividerBlockLayoutAttrs",
    "VisualBlockEmailHTMLBlock",
    "VisualBlockEmailHTMLBlockLayoutAttrs",
    "VisualBlockEmailImageBlock",
    "VisualBlockEmailImageBlockLayoutAttrs",
    "VisualBlockEmailImageBlockStyleAttrs",
    "VisualBlockEmailMarkdownBlock",
    "VisualBlockEmailMarkdownBlockLayoutAttrs",
    "VisualBlockEmailPartialBlock",
    "VisualBlockEmailPartialBlockLayoutAttrs",
]


class Settings(TypedDict, total=False):
    """
    The [settings](https://docs.knock.app/integrations/email/settings) for the email template. Must be supplied with at least `layout_key`.
    """

    attachment_key: Optional[str]
    """
    The object path in the workflow trigger's `data` payload to resolve
    attachments.Defaults to `attachments`.
    """

    layout_key: Optional[str]
    """
    The `key` of the
    [email layout](https://docs.knock.app/integrations/email/layouts) that wraps the
    email template. When omitted, the email template will need to define the
    `<html>` structure.
    """

    pre_content: Optional[str]
    """
    A liquid template that will be injected into the email layout above the message
    template content. Useful for setting variables that should be available to the
    email layout.
    """


class VisualBlockEmailButtonSetBlockButtonSizeAttrs(TypedDict, total=False):
    """The size attributes of the button."""

    is_fullwidth: bool
    """Whether the button is full width."""

    size: Literal["sm", "md", "lg"]
    """The size of the button."""


class VisualBlockEmailButtonSetBlockButtonStyleAttrs(TypedDict, total=False):
    """The style attributes of the button."""

    background_color: str
    """The background color of the button."""

    border_color: str
    """The border color of the button."""

    border_radius: int
    """The border radius of the button."""

    border_width: int
    """The border width of the button."""

    text_color: str
    """The text color of the button."""


class VisualBlockEmailButtonSetBlockButton(TypedDict, total=False):
    """A button in a button set block."""

    action: Required[str]
    """The action of the button."""

    label: Required[str]
    """The label of the button."""

    variant: Required[Literal["solid", "outline"]]
    """The variant of the button."""

    size_attrs: VisualBlockEmailButtonSetBlockButtonSizeAttrs
    """The size attributes of the button."""

    style_attrs: VisualBlockEmailButtonSetBlockButtonStyleAttrs
    """The style attributes of the button."""


class VisualBlockEmailButtonSetBlockLayoutAttrs(TypedDict, total=False):
    """The layout attributes of the block."""

    column_gap: Required[int]
    """The column_gap layout attribute of the block."""

    horizontal_align: Required[Literal["left", "center", "right"]]
    """The horizontal alignment of the block."""

    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailButtonSetBlock(TypedDict, total=False):
    """A button set block in an email template."""

    buttons: Required[Iterable[VisualBlockEmailButtonSetBlockButton]]
    """A list of buttons in the button set."""

    type: Required[Literal["button_set"]]
    """The type of the block."""

    id: str
    """The ID of the block."""

    layout_attrs: VisualBlockEmailButtonSetBlockLayoutAttrs
    """The layout attributes of the block."""

    version: int
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailDividerBlockLayoutAttrs(TypedDict, total=False):
    """The layout attributes of the block."""

    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailDividerBlock(TypedDict, total=False):
    """A divider block in an email template."""

    type: Required[Literal["divider"]]
    """The type of the block."""

    id: str
    """The ID of the block."""

    layout_attrs: VisualBlockEmailDividerBlockLayoutAttrs
    """The layout attributes of the block."""

    version: int
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailHTMLBlockLayoutAttrs(TypedDict, total=False):
    """The layout attributes of the block."""

    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailHTMLBlock(TypedDict, total=False):
    """An HTML block in an email template."""

    content: Required[str]
    """The HTML content of the block.

    Supports Liquid templating with variables like `{{ recipient.name }}`,
    `{{ actor.name }}`, `{{ vars.app_name }}`, `{{ data.custom_field }}`, and
    `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    type: Required[Literal["html"]]
    """The type of the block."""

    id: str
    """The ID of the block."""

    layout_attrs: VisualBlockEmailHTMLBlockLayoutAttrs
    """The layout attributes of the block."""

    version: int
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailImageBlockLayoutAttrs(TypedDict, total=False):
    """The layout attributes of the block."""

    horizontal_align: Required[Literal["left", "center", "right"]]
    """The horizontal alignment of the block."""

    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailImageBlockStyleAttrs(TypedDict, total=False):
    """The style attributes of the image."""

    width: str
    """The width of the image."""


class VisualBlockEmailImageBlock(TypedDict, total=False):
    """An image block in an email template."""

    type: Required[Literal["image"]]
    """The type of the block."""

    url: Required[str]
    """The URL of the image to display."""

    id: str
    """The ID of the block."""

    action: Optional[str]
    """Optional action URL for the image."""

    alt: Optional[str]
    """Alt text for the image."""

    layout_attrs: VisualBlockEmailImageBlockLayoutAttrs
    """The layout attributes of the block."""

    style_attrs: VisualBlockEmailImageBlockStyleAttrs
    """The style attributes of the image."""

    version: int
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailMarkdownBlockLayoutAttrs(TypedDict, total=False):
    """The layout attributes of the block."""

    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailMarkdownBlock(TypedDict, total=False):
    """A markdown block in an email template."""

    content: Required[str]
    """The markdown content of the block.

    Supports Liquid templating with variables like `{{ recipient.name }}`,
    `{{ actor.name }}`, `{{ vars.app_name }}`, `{{ data.custom_field }}`, and
    `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    type: Required[Literal["markdown"]]
    """The type of the block."""

    id: str
    """The ID of the block."""

    layout_attrs: VisualBlockEmailMarkdownBlockLayoutAttrs
    """The layout attributes of the block."""

    variant: Literal["default"]
    """The flavor of markdown to use for the block."""

    version: int
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailPartialBlockLayoutAttrs(TypedDict, total=False):
    """The layout attributes of the block."""

    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailPartialBlock(TypedDict, total=False):
    """
    A partial block in an email template, used to render a reusable partial component.
    """

    attrs: Required[Dict[str, object]]
    """The attributes to pass to the partial block."""

    key: Required[str]
    """The key of the partial block to invoke."""

    name: Required[str]
    """The name of the partial block."""

    type: Required[Literal["partial"]]
    """The type of the block."""

    id: str
    """The ID of the block."""

    layout_attrs: VisualBlockEmailPartialBlockLayoutAttrs
    """The layout attributes of the block."""

    version: int
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


VisualBlock: TypeAlias = Union[
    VisualBlockEmailButtonSetBlock,
    VisualBlockEmailDividerBlock,
    VisualBlockEmailHTMLBlock,
    VisualBlockEmailImageBlock,
    VisualBlockEmailMarkdownBlock,
    VisualBlockEmailPartialBlock,
]


class EmailTemplateParam(TypedDict, total=False):
    """An email message template."""

    settings: Required[Settings]
    """
    The [settings](https://docs.knock.app/integrations/email/settings) for the email
    template. Must be supplied with at least `layout_key`.
    """

    subject: Required[str]
    """The subject of the email.

    Supports Liquid templating with variables like `{{ recipient.name }}`,
    `{{ actor.name }}`, `{{ vars.app_name }}`, `{{ data.custom_field }}`, and
    `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    html_body: Optional[str]
    """An HTML or MJML template for the email body.

    **Required** if `visual_blocks` is not provided. Only one of `html_body` or
    `visual_blocks` should be set. When `is_mjml` is true, this must contain MJML
    components. Supports Liquid templating with variables like
    `{{ recipient.name }}`, `{{ actor.name }}`, `{{ vars.app_name }}`,
    `{{ data.custom_field }}`, and `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    is_mjml: Optional[bool]
    """Whether this template uses MJML format.

    When true, the template content will be compiled from MJML to HTML. Only valid
    when the selected layout is also MJML or when no layout is selected.
    """

    text_body: Optional[str]
    """A text template for the email body.

    When omitted, the email template will be autogenerated from the `html_body` or
    `visual_blocks`.
    """

    visual_blocks: Optional[Iterable[VisualBlock]]
    """The visual blocks that make up the email template."""

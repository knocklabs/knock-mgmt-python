# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "EmailTemplate",
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


class Settings(BaseModel):
    """
    The [settings](https://docs.knock.app/integrations/email/settings) for the email template. Must be supplied with at least `layout_key`.
    """

    attachment_key: Optional[str] = None
    """
    The object path in the workflow trigger's `data` payload to resolve
    attachments.Defaults to `attachments`.
    """

    layout_key: Optional[str] = None
    """
    The `key` of the
    [email layout](https://docs.knock.app/integrations/email/layouts) that wraps the
    email template. When omitted, the email template will need to define the
    `<html>` structure.
    """

    pre_content: Optional[str] = None
    """
    A liquid template that will be injected into the email layout above the message
    template content. Useful for setting variables that should be available to the
    email layout.
    """


class VisualBlockEmailButtonSetBlockButtonSizeAttrs(BaseModel):
    """The size attributes of the button."""

    is_fullwidth: Optional[bool] = None
    """Whether the button is full width."""

    size: Optional[Literal["sm", "md", "lg"]] = None
    """The size of the button."""


class VisualBlockEmailButtonSetBlockButtonStyleAttrs(BaseModel):
    """The style attributes of the button."""

    background_color: Optional[str] = None
    """The background color of the button."""

    border_color: Optional[str] = None
    """The border color of the button."""

    border_radius: Optional[int] = None
    """The border radius of the button."""

    border_width: Optional[int] = None
    """The border width of the button."""

    text_color: Optional[str] = None
    """The text color of the button."""


class VisualBlockEmailButtonSetBlockButton(BaseModel):
    """A button in a button set block."""

    action: str
    """The action of the button."""

    label: str
    """The label of the button."""

    variant: Literal["solid", "outline"]
    """The variant of the button."""

    size_attrs: Optional[VisualBlockEmailButtonSetBlockButtonSizeAttrs] = None
    """The size attributes of the button."""

    style_attrs: Optional[VisualBlockEmailButtonSetBlockButtonStyleAttrs] = None
    """The style attributes of the button."""


class VisualBlockEmailButtonSetBlockLayoutAttrs(BaseModel):
    """The layout attributes of the block."""

    column_gap: int
    """The column_gap layout attribute of the block."""

    horizontal_align: Literal["left", "center", "right"]
    """The horizontal alignment of the block."""

    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailButtonSetBlock(BaseModel):
    """A button set block in an email template."""

    buttons: List[VisualBlockEmailButtonSetBlockButton]
    """A list of buttons in the button set."""

    type: Literal["button_set"]
    """The type of the block."""

    id: Optional[str] = None
    """The ID of the block."""

    layout_attrs: Optional[VisualBlockEmailButtonSetBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    version: Optional[int] = None
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailDividerBlockLayoutAttrs(BaseModel):
    """The layout attributes of the block."""

    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailDividerBlock(BaseModel):
    """A divider block in an email template."""

    type: Literal["divider"]
    """The type of the block."""

    id: Optional[str] = None
    """The ID of the block."""

    layout_attrs: Optional[VisualBlockEmailDividerBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    version: Optional[int] = None
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailHTMLBlockLayoutAttrs(BaseModel):
    """The layout attributes of the block."""

    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailHTMLBlock(BaseModel):
    """An HTML block in an email template."""

    content: str
    """The HTML content of the block.

    Supports Liquid templating with variables like `{{ recipient.name }}`,
    `{{ actor.name }}`, `{{ vars.app_name }}`, `{{ data.custom_field }}`, and
    `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    type: Literal["html"]
    """The type of the block."""

    id: Optional[str] = None
    """The ID of the block."""

    layout_attrs: Optional[VisualBlockEmailHTMLBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    version: Optional[int] = None
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailImageBlockLayoutAttrs(BaseModel):
    """The layout attributes of the block."""

    horizontal_align: Literal["left", "center", "right"]
    """The horizontal alignment of the block."""

    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailImageBlockStyleAttrs(BaseModel):
    """The style attributes of the image."""

    width: Optional[str] = None
    """The width of the image."""


class VisualBlockEmailImageBlock(BaseModel):
    """An image block in an email template."""

    type: Literal["image"]
    """The type of the block."""

    url: str
    """The URL of the image to display."""

    id: Optional[str] = None
    """The ID of the block."""

    action: Optional[str] = None
    """Optional action URL for the image."""

    alt: Optional[str] = None
    """Alt text for the image."""

    layout_attrs: Optional[VisualBlockEmailImageBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    style_attrs: Optional[VisualBlockEmailImageBlockStyleAttrs] = None
    """The style attributes of the image."""

    version: Optional[int] = None
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailMarkdownBlockLayoutAttrs(BaseModel):
    """The layout attributes of the block."""

    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailMarkdownBlock(BaseModel):
    """A markdown block in an email template."""

    content: str
    """The markdown content of the block.

    Supports Liquid templating with variables like `{{ recipient.name }}`,
    `{{ actor.name }}`, `{{ vars.app_name }}`, `{{ data.custom_field }}`, and
    `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    type: Literal["markdown"]
    """The type of the block."""

    id: Optional[str] = None
    """The ID of the block."""

    layout_attrs: Optional[VisualBlockEmailMarkdownBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    variant: Optional[Literal["default"]] = None
    """The flavor of markdown to use for the block."""

    version: Optional[int] = None
    """The version of the block schema.

    This is automatically managed by Knock and should not be set manually. Currently
    all blocks are at version 1.
    """


class VisualBlockEmailPartialBlockLayoutAttrs(BaseModel):
    """The layout attributes of the block."""

    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailPartialBlock(BaseModel):
    """
    A partial block in an email template, used to render a reusable partial component.
    """

    attrs: Dict[str, object]
    """The attributes to pass to the partial block."""

    key: str
    """The key of the partial block to invoke."""

    name: str
    """The name of the partial block."""

    type: Literal["partial"]
    """The type of the block."""

    id: Optional[str] = None
    """The ID of the block."""

    layout_attrs: Optional[VisualBlockEmailPartialBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    version: Optional[int] = None
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


class EmailTemplate(BaseModel):
    """An email message template."""

    settings: Settings
    """
    The [settings](https://docs.knock.app/integrations/email/settings) for the email
    template. Must be supplied with at least `layout_key`.
    """

    subject: str
    """The subject of the email.

    Supports Liquid templating with variables like `{{ recipient.name }}`,
    `{{ actor.name }}`, `{{ vars.app_name }}`, `{{ data.custom_field }}`, and
    `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    html_body: Optional[str] = None
    """An HTML template for the email body.

    **Required** if `visual_blocks` is not provided. Only one of `html_body` or
    `visual_blocks` should be set. Supports Liquid templating with variables like
    `{{ recipient.name }}`, `{{ actor.name }}`, `{{ vars.app_name }}`,
    `{{ data.custom_field }}`, and `{{ tenant.name }}`. See the
    [template variables reference](https://docs.knock.app/designing-workflows/template-editor/variables)
    for available variables.
    """

    text_body: Optional[str] = None
    """A text template for the email body.

    When omitted, the email template will be autogenerated from the `html_body` or
    `visual_blocks`.
    """

    visual_blocks: Optional[List[VisualBlock]] = None
    """The visual blocks that make up the email template."""

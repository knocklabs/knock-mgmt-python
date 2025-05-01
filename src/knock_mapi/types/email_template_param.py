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
    "VisualBlockEmailImageBlock",
    "VisualBlockEmailImageBlockLayoutAttrs",
    "VisualBlockEmailImageBlockStyleAttrs",
    "VisualBlockEmailMarkdownBlock",
    "VisualBlockEmailMarkdownBlockLayoutAttrs",
    "VisualBlockEmailPartialBlock",
    "VisualBlockEmailPartialBlockLayoutAttrs",
]


class Settings(TypedDict, total=False):
    attachment_key: Optional[str]
    """
    The object path in the data payload (of the workflow trigger call) to resolve
    attachments.
    """

    layout_key: Optional[str]
    """The key of the email layout which the step is using."""

    pre_content: Optional[str]
    """
    A liquid template that will be injected into the layout above the message
    template content.
    """


class VisualBlockEmailButtonSetBlockButtonSizeAttrs(TypedDict, total=False):
    is_fullwidth: bool
    """Whether the button is full width."""

    size: Literal["sm", "md", "lg"]
    """The size of the button."""


class VisualBlockEmailButtonSetBlockButtonStyleAttrs(TypedDict, total=False):
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
    action: Required[str]
    """The action of the button."""

    label: Required[str]
    """The label of the button."""

    variant: Required[str]
    """The variant of the button."""

    size_attrs: VisualBlockEmailButtonSetBlockButtonSizeAttrs
    """The size attributes of the button."""

    style_attrs: VisualBlockEmailButtonSetBlockButtonStyleAttrs
    """The style attributes of the button."""


class VisualBlockEmailButtonSetBlockLayoutAttrs(TypedDict, total=False):
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
    id: Required[str]
    """The ID of the block."""

    buttons: Required[Iterable[VisualBlockEmailButtonSetBlockButton]]
    """A list of buttons in the button set."""

    type: Required[str]
    """The type of the block."""

    version: Required[int]
    """The version of the block."""

    layout_attrs: VisualBlockEmailButtonSetBlockLayoutAttrs
    """The layout attributes of the block."""


class VisualBlockEmailDividerBlockLayoutAttrs(TypedDict, total=False):
    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailDividerBlock(TypedDict, total=False):
    id: Required[str]
    """The ID of the block."""

    type: Required[str]
    """The type of the block."""

    version: Required[int]
    """The version of the block."""

    layout_attrs: VisualBlockEmailDividerBlockLayoutAttrs
    """The layout attributes of the block."""


class VisualBlockEmailHTMLBlock(TypedDict, total=False):
    id: Required[str]
    """The ID of the block."""

    content: Required[str]
    """The HTML content of the block."""

    type: Required[str]
    """The type of the block."""

    version: Required[int]
    """The version of the block."""


class VisualBlockEmailImageBlockLayoutAttrs(TypedDict, total=False):
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
    width: str
    """The width of the image."""


class VisualBlockEmailImageBlock(TypedDict, total=False):
    id: Required[str]
    """The ID of the block."""

    type: Required[str]
    """The type of the block."""

    url: Required[str]
    """The URL of the image to display."""

    version: Required[int]
    """The version of the block."""

    action: Optional[str]
    """Optional action URL for the image."""

    alt: Optional[str]
    """Alt text for the image."""

    layout_attrs: VisualBlockEmailImageBlockLayoutAttrs
    """The layout attributes of the block."""

    style_attrs: VisualBlockEmailImageBlockStyleAttrs
    """The style attributes of the image."""


class VisualBlockEmailMarkdownBlockLayoutAttrs(TypedDict, total=False):
    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailMarkdownBlock(TypedDict, total=False):
    id: Required[str]
    """The ID of the block."""

    content: Required[str]
    """The markdown content of the block."""

    type: Required[str]
    """The type of the block."""

    variant: Required[str]
    """The flavor of markdown to use for the block."""

    version: Required[int]
    """The version of the block."""

    layout_attrs: VisualBlockEmailMarkdownBlockLayoutAttrs
    """The layout attributes of the block."""


class VisualBlockEmailPartialBlockLayoutAttrs(TypedDict, total=False):
    padding_bottom: Required[int]
    """The padding_bottom layout attribute of the block."""

    padding_left: Required[int]
    """The padding_left layout attribute of the block."""

    padding_right: Required[int]
    """The padding_right layout attribute of the block."""

    padding_top: Required[int]
    """The padding_top layout attribute of the block."""


class VisualBlockEmailPartialBlock(TypedDict, total=False):
    id: Required[str]
    """The ID of the block."""

    attrs: Required[Dict[str, object]]
    """The attributes to pass to the partial block."""

    key: Required[str]
    """The key of the partial block to invoke."""

    name: Required[str]
    """The name of the partial block."""

    type: Required[str]
    """The type of the block."""

    version: Required[int]
    """The version of the block."""

    layout_attrs: VisualBlockEmailPartialBlockLayoutAttrs
    """The layout attributes of the block."""


VisualBlock: TypeAlias = Union[
    VisualBlockEmailButtonSetBlock,
    VisualBlockEmailDividerBlock,
    VisualBlockEmailHTMLBlock,
    VisualBlockEmailImageBlock,
    VisualBlockEmailMarkdownBlock,
    VisualBlockEmailPartialBlock,
]


class EmailTemplateParam(TypedDict, total=False):
    subject: Required[str]
    """The subject of the email."""

    html_body: str
    """An HTML template for the email body.

    Either `html_body` or `visual_blocks` must be provided.
    """

    settings: Optional[Settings]
    """
    The [settings](https://docs.knock.app/integrations/email/settings) for the email
    template.
    """

    text_body: Optional[str]
    """A text template for the email body.

    Only present if opted out from autogenerating it from the HTML template.
    """

    visual_blocks: Iterable[VisualBlock]
    """The visual blocks of the email.

    Either `html_body` or `visual_blocks` must be provided.
    """

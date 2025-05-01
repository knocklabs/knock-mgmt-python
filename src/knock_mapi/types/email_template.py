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
    "VisualBlockEmailImageBlock",
    "VisualBlockEmailImageBlockLayoutAttrs",
    "VisualBlockEmailImageBlockStyleAttrs",
    "VisualBlockEmailMarkdownBlock",
    "VisualBlockEmailMarkdownBlockLayoutAttrs",
    "VisualBlockEmailPartialBlock",
    "VisualBlockEmailPartialBlockLayoutAttrs",
]


class Settings(BaseModel):
    attachment_key: Optional[str] = None
    """
    The object path in the data payload (of the workflow trigger call) to resolve
    attachments.
    """

    layout_key: Optional[str] = None
    """The key of the email layout which the step is using."""

    pre_content: Optional[str] = None
    """
    A liquid template that will be injected into the layout above the message
    template content.
    """


class VisualBlockEmailButtonSetBlockButtonSizeAttrs(BaseModel):
    is_fullwidth: Optional[bool] = None
    """Whether the button is full width."""

    size: Optional[Literal["sm", "md", "lg"]] = None
    """The size of the button."""


class VisualBlockEmailButtonSetBlockButtonStyleAttrs(BaseModel):
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
    action: str
    """The action of the button."""

    label: str
    """The label of the button."""

    variant: str
    """The variant of the button."""

    size_attrs: Optional[VisualBlockEmailButtonSetBlockButtonSizeAttrs] = None
    """The size attributes of the button."""

    style_attrs: Optional[VisualBlockEmailButtonSetBlockButtonStyleAttrs] = None
    """The style attributes of the button."""


class VisualBlockEmailButtonSetBlockLayoutAttrs(BaseModel):
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
    id: str
    """The ID of the block."""

    buttons: List[VisualBlockEmailButtonSetBlockButton]
    """A list of buttons in the button set."""

    type: str
    """The type of the block."""

    version: int
    """The version of the block."""

    layout_attrs: Optional[VisualBlockEmailButtonSetBlockLayoutAttrs] = None
    """The layout attributes of the block."""


class VisualBlockEmailDividerBlockLayoutAttrs(BaseModel):
    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailDividerBlock(BaseModel):
    id: str
    """The ID of the block."""

    type: str
    """The type of the block."""

    version: int
    """The version of the block."""

    layout_attrs: Optional[VisualBlockEmailDividerBlockLayoutAttrs] = None
    """The layout attributes of the block."""


class VisualBlockEmailHTMLBlock(BaseModel):
    id: str
    """The ID of the block."""

    content: str
    """The HTML content of the block."""

    type: str
    """The type of the block."""

    version: int
    """The version of the block."""


class VisualBlockEmailImageBlockLayoutAttrs(BaseModel):
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
    width: Optional[str] = None
    """The width of the image."""


class VisualBlockEmailImageBlock(BaseModel):
    id: str
    """The ID of the block."""

    type: str
    """The type of the block."""

    url: str
    """The URL of the image to display."""

    version: int
    """The version of the block."""

    action: Optional[str] = None
    """Optional action URL for the image."""

    alt: Optional[str] = None
    """Alt text for the image."""

    layout_attrs: Optional[VisualBlockEmailImageBlockLayoutAttrs] = None
    """The layout attributes of the block."""

    style_attrs: Optional[VisualBlockEmailImageBlockStyleAttrs] = None
    """The style attributes of the image."""


class VisualBlockEmailMarkdownBlockLayoutAttrs(BaseModel):
    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailMarkdownBlock(BaseModel):
    id: str
    """The ID of the block."""

    content: str
    """The markdown content of the block."""

    type: str
    """The type of the block."""

    variant: str
    """The flavor of markdown to use for the block."""

    version: int
    """The version of the block."""

    layout_attrs: Optional[VisualBlockEmailMarkdownBlockLayoutAttrs] = None
    """The layout attributes of the block."""


class VisualBlockEmailPartialBlockLayoutAttrs(BaseModel):
    padding_bottom: int
    """The padding_bottom layout attribute of the block."""

    padding_left: int
    """The padding_left layout attribute of the block."""

    padding_right: int
    """The padding_right layout attribute of the block."""

    padding_top: int
    """The padding_top layout attribute of the block."""


class VisualBlockEmailPartialBlock(BaseModel):
    id: str
    """The ID of the block."""

    attrs: Dict[str, object]
    """The attributes to pass to the partial block."""

    key: str
    """The key of the partial block to invoke."""

    name: str
    """The name of the partial block."""

    type: str
    """The type of the block."""

    version: int
    """The version of the block."""

    layout_attrs: Optional[VisualBlockEmailPartialBlockLayoutAttrs] = None
    """The layout attributes of the block."""


VisualBlock: TypeAlias = Union[
    VisualBlockEmailButtonSetBlock,
    VisualBlockEmailDividerBlock,
    VisualBlockEmailHTMLBlock,
    VisualBlockEmailImageBlock,
    VisualBlockEmailMarkdownBlock,
    VisualBlockEmailPartialBlock,
]


class EmailTemplate(BaseModel):
    subject: str
    """The subject of the email."""

    html_body: Optional[str] = None
    """An HTML template for the email body.

    Either `html_body` or `visual_blocks` must be provided.
    """

    settings: Optional[Settings] = None
    """
    The [settings](https://docs.knock.app/integrations/email/settings) for the email
    template.
    """

    text_body: Optional[str] = None
    """A text template for the email body.

    Only present if opted out from autogenerating it from the HTML template.
    """

    visual_blocks: Optional[List[VisualBlock]] = None
    """The visual blocks of the email.

    Either `html_body` or `visual_blocks` must be provided.
    """

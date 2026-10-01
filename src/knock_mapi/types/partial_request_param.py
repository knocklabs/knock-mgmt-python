# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.message_type_url_field import MessageTypeURLField
from .shared_params.message_type_json_field import MessageTypeJsonField
from .shared_params.message_type_list_field import MessageTypeListField
from .shared_params.message_type_text_field import MessageTypeTextField
from .shared_params.message_type_color_field import MessageTypeColorField
from .shared_params.message_type_image_field import MessageTypeImageField
from .shared_params.message_type_button_field import MessageTypeButtonField
from .shared_params.message_type_number_field import MessageTypeNumberField
from .shared_params.message_type_select_field import MessageTypeSelectField
from .shared_params.message_type_boolean_field import MessageTypeBooleanField
from .shared_params.message_type_markdown_field import MessageTypeMarkdownField
from .shared_params.message_type_textarea_field import MessageTypeTextareaField
from .shared_params.message_type_multi_select_field import MessageTypeMultiSelectField

__all__ = ["PartialRequestParam", "InputSchema"]

InputSchema: TypeAlias = Union[
    MessageTypeListField,
    MessageTypeSelectField,
    MessageTypeBooleanField,
    MessageTypeJsonField,
    MessageTypeNumberField,
    MessageTypeTextField,
    MessageTypeImageField,
    MessageTypeColorField,
    MessageTypeURLField,
    MessageTypeMarkdownField,
    MessageTypeMultiSelectField,
    MessageTypeButtonField,
    MessageTypeTextareaField,
]


class PartialRequestParam(TypedDict, total=False):
    """A partial object with attributes to update or create a partial."""

    content: Required[str]
    """The partial content."""

    name: Required[str]
    """A name for the partial. Must be at maximum 255 characters in length."""

    type: Required[Literal["html", "text", "json", "markdown"]]
    """The partial type. One of 'html', 'json', 'markdown', 'text'."""

    description: str
    """An arbitrary string attached to a partial object.

    Useful for adding notes about the partial for internal purposes. Maximum of 280
    characters allowed.
    """

    icon_name: str
    """The name of the icon to be used in the visual editor."""

    input_schema: Iterable[InputSchema]
    """The field types available for the partial."""

    visual_block_enabled: bool
    """Indicates whether the partial can be used in the visual editor.

    Only applies to HTML partials.
    """

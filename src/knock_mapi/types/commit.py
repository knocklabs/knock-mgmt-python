# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Commit", "Author", "Resource"]


class Author(BaseModel):
    """The author of the commit."""

    email: str
    """The email address of the commit author."""

    name: Optional[str] = None
    """The name of the commit author."""


class Resource(BaseModel):
    """The resource object associated with the commit."""

    identifier: str
    """The unique identifier for the resource."""

    type: Literal[
        "audience", "email_layout", "guide", "message_type", "partial", "reusable_request", "translation", "workflow"
    ]
    """The type of the resource object."""


class Commit(BaseModel):
    """A commit is a change to a resource within an environment, made by an author."""

    id: str
    """The unique identifier for the commit."""

    author: Author
    """The author of the commit."""

    created_at: datetime
    """The timestamp of when the commit was created."""

    environment: str
    """The environment of the commit."""

    promote_group_id: Optional[str] = None
    """
    The identifier of the promote that created this commit, shared by every commit
    copied into the environment by the same promote. Null if the commit was not
    created by a promote.
    """

    promoted_from_commit_id: Optional[str] = None
    """The ID of the commit this commit was promoted from.

    Null if the commit was not created by a promote.
    """

    resource: Resource
    """The resource object associated with the commit."""

    commit_message: Optional[str] = None
    """The optional message about the commit."""

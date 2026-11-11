# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Warehouse"]


class Warehouse(BaseModel):
    """A warehouse is one database in your data warehouse that Knock reads from.

    Warehouses belong to the project and are shared by every environment.
    """

    connection_status: Literal["not_configured", "key_not_installed", "failed", "connecting", "untested", "connected"]
    """The status of the warehouse's connection."""

    created_at: datetime
    """When the warehouse was created."""

    key: str
    """The unique key of the warehouse."""

    name: str
    """The name of the warehouse."""

    type: Literal["redshift", "snowflake", "postgres", "bigquery"]
    """The type of data warehouse."""

    updated_at: datetime
    """When the warehouse was last updated."""

    connection_error: Optional[Dict[str, object]] = None
    """The error from the last connection test, with a `code` and a `message`.

    Null when the last test passed.
    """

    connection_settings: Optional[Dict[str, object]] = None
    """How Knock connects to the warehouse.

    The fields depend on the warehouse type, such as `host`, `port`, `database`, and
    `username`, or `project_id`, `region`, and `service_account_email` for BigQuery.
    Credentials such as passwords are never returned.
    """

    last_tested_at: Optional[datetime] = None
    """When the connection was last tested."""

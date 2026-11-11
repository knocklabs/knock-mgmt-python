# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .warehouse_sync_request_param import WarehouseSyncRequestParam

__all__ = ["WarehouseSyncUpsertParams"]


class WarehouseSyncUpsertParams(TypedDict, total=False):
    warehouse_sync: Required[WarehouseSyncRequestParam]
    """A warehouse sync payload for upsert or validate.

    Fields left out keep their current values. `warehouse_key`, `target_type`, and
    `target` are required to create a sync and can't change after. Change `enabled`
    and `frequency_minutes` with the settings endpoint.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

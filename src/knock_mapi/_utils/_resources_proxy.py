from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `knock_mapi.resources` module.

    This is used so that we can lazily import `knock_mapi.resources` only when
    needed *and* so that users can just import `knock_mapi` and reference `knock_mapi.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("knock_mapi.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()

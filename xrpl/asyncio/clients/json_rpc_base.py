"""A common interface for JsonRpc requests."""
from __future__ import annotations

from typing import Any, Dict, cast

from httpx import AsyncClient
from typing_extensions import Final

from xrpl.asyncio.clients.client import Client

_TIMEOUT: Final[float] = 10.0


class JsonRpcBase(Client):
    """
    A common interface for JsonRpc requests.

    :meta private:
    """

    async def request_json_impl(
        self: JsonRpcBase, request: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Base ``request_json_impl`` implementation for JSON RPC.

        Arguments:
            request: An object representing information about a rippled request.

        Returns:
            The response from the server, as a Response object.

        :meta private:
        """
        async with AsyncClient(timeout=_TIMEOUT) as http_client:
            response = await http_client.post(
                self.url,
                json=request,
            )
            return cast(Dict[str, Any], response.json())

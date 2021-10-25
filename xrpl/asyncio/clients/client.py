"""Interface for all network clients to follow."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict

from xrpl.asyncio.clients.utils import json_to_response, request_to_json_rpc
from xrpl.models.requests.request import Request
from xrpl.models.response import Response


class Client(ABC):
    """
    Interface for all network clients to follow.

    :meta private:
    """

    def __init__(self: Client, url: str) -> None:
        """
        Initializes a client.

        Arguments:
            url: The url to which this client will connect
        """
        self.url = url

    @abstractmethod
    async def request_impl(self: Client, request: Request) -> Response:
        """
        This is the main driver for a given Client's request. It must be
        async because all of the helper functions in this library are
        async-first.

        Arguments:
            request: An object representing information about a rippled request.

        Returns:
            The response from the server, as a Response object.

        :meta private:
        """
        json_request = request_to_json_rpc(request)
        return json_to_response(await self.request_json_impl(json_request))

    async def request_json_impl(
        self: Client, request: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        This is the actual driver for a given Client's request. It must be
        async because all of the helper functions in this library are
        async-first. Implement this in a given Client.

        Arguments:
            request: An object representing information about a rippled request.

        :meta private:
        """
        pass

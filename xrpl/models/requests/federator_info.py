"""
The federator_info command asks the server for a
human-readable version of various information
about the federator server being queried.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class FederatorInfo(Request):
    """
    The federator_info command asks the server for a
    human-readable version of various information
    about the federator server being queried.
    """

    method: RequestMethod = field(default=RequestMethod.FEDERATOR_INFO, init=False)

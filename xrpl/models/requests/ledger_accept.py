"""The ledger_accept command advances the ledger when in standalone mode."""

from __future__ import annotations

from dataclasses import dataclass, field

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class LedgerAccept(Request):
    """The ledger_accept command advances the ledger when in standalone mode."""

    method: RequestMethod = field(default=RequestMethod.LEDGER_ACCEPT, init=False)

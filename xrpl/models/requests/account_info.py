"""Model for an AccountInfo request."""

from dataclasses import dataclass, field
from typing import Optional, Union

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.required import REQUIRED
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class AccountInfo(Request):
    """
    Represents an `account_info <https://xrpl.org/account_info.html>`_
    request, which retrieves information about an account, including its
    activity and XRP balance.

    All information retrieved is relative to a particular version of the ledger.
    """

    #: This field is required.
    account: str = REQUIRED  # type: ignore
    ledger_hash: Optional[str] = None
    ledger_index: Optional[Union[str, int]] = None
    method: RequestMethod = field(default=RequestMethod.ACCOUNT_INFO, init=False)
    queue: bool = False
    signer_lists: bool = False
    strict: bool = False

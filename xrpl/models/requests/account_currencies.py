"""Model for an AccountCurrencies request."""

from dataclasses import dataclass, field
from typing import Optional, Union

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.required import REQUIRED
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class AccountCurrencies(Request):
    """
    Represents an `account_currencies <https://xrpl.org/account_currencies.html>`_,
    request, which retrieves a list of currencies that an account can send or receive,
    based on the account's `trust lines
    <https://xrpl.org/trust-lines-and-issuing.html#trust-lines-and-issuing>`_.

    The list is not thoroughly confirmed, but you can use it to populate user
    interfaces.
    """

    #: This field is required.
    account: str = REQUIRED  # type: ignore
    ledger_hash: Optional[str] = None
    ledger_index: Optional[Union[str, int]] = None
    method: RequestMethod = field(default=RequestMethod.ACCOUNT_CURRENCIES, init=False)
    strict: bool = False

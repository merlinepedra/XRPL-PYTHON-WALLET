"""Model for an AccountChannels request."""

from dataclasses import dataclass, field
from typing import Any, Optional, Union

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.required import REQUIRED
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class AccountChannels(Request):
    """
    Represents an `account_channels <https://xrpl.org/account_channels.html>`_ request,
    which retrieves information about an account's `payment channels
    <https://xrpl.org/payment-channels.html>`_.

    The response only includes payment channels where the specified account is the
    channel's source, not the destination. (A channel's "source" and "owner" are the
    same.)

    All information retrieved is relative to a particular version of the ledger.
    """

    method: RequestMethod = field(default=RequestMethod.ACCOUNT_CHANNELS, init=False)
    #: This field is required.
    account: str = REQUIRED  # type: ignore
    #: The destination account of the payment channel.
    #: If provided, filters results to payment channels
    #: whose destination is this account.
    destination_account: Optional[str] = None
    limit: int = 200
    # marker data shape is actually undefined in the spec, up to the
    # implementation of an individual server
    marker: Optional[Any] = None
    ledger_hash: Optional[str] = None
    ledger_index: Optional[Union[str, int]] = None

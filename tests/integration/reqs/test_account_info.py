from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from tests.integration.reusable_values import WALLET
from xrpl.asyncio.clients.json_rpc_base import JsonRpcBase
from xrpl.models.requests import AccountInfo


class TestAccountInfo(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_basic_functionality(self, client):
        response = await client.request(
            AccountInfo(
                account=WALLET.classic_address,
            )
        )
        self.assertTrue(response.is_successful())

    @test_async_and_sync(globals())
    async def test_basic_functionality_json(self, client):
        http = {
            "method": "account_info",
            "params": [
                {
                    "account": WALLET.classic_address,
                }
            ],
        }
        ws = {"command": "account_info", "account": WALLET.classic_address}
        if isinstance(client, JsonRpcBase):
            jsn = http
        else:
            jsn = ws
        response = await client.request_json(jsn)
        if isinstance(client, JsonRpcBase):
            self.assertEqual(response["result"]["status"], "success")
        else:
            self.assertEqual(response["status"], "success")

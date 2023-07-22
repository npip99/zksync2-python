from zksync2.module.zksync_module import ZkSync
from zksync2.module.zksync_provider import ZkSyncProvider
from zksync2.module.middleware import build_zksync_middleware

from typing import Union
from web3._utils.module import attach_modules
from eth_typing import URI
from web3 import Web3
from typing import Any


class ZkSyncBuilder:
    @classmethod
    def build(cls, url: Union[URI, str], session: Any = None) -> Web3:
        web3_module = Web3()
        zksync_provider = ZkSyncProvider(url, session=session)
        zksync_middleware = build_zksync_middleware(zksync_provider)
        web3_module.middleware_onion.add(zksync_middleware)
        attach_modules(web3_module, {"zksync": (ZkSync,)})
        return web3_module

from boa.lrudict import lrudict

class AccountDBFork(AccountDB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._getbalance_cache = lrudict(0x10000)
        self._gettxcount_cache = lrudict(0x10000)

    def _fetch_balance(self, address):
        if address in self._getbalance_cache:
            return self._getbalance_cache[address]
        ret = self._rpc.fetch("eth_getBalance", {"address": address})
        self._getbalance_cache[address] = ret
        return ret

    def _fetch_txcount(self, address):
        if address in self._gettxcount_cache:
            return self._gettxcount_cache[address]
        ret = self._rpc.fetch("eth_getBalance", {"address": address})
        self._gettxcount_cache[address] = ret
        return ret



    def account_exists(self, address):
        if super().account_exists(address):
            return True

        return self.get_balance(address) > 0 or self.get_nonce(address) > 0


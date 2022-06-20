import json
'''wallet api'''

class CanShu_04:
    def account_wallet(self):
        # 获取钱包账户信息
        self.method = 'GET'
        self.path = '/v1/api/account/wallet'
        self.body = ''
        return self.method, self.path, self.body

    def wallet_currency(self):
        # 获取钱包账户某币种详情
        self.method = 'GET'
        self.path = '/v1/api/account/wallet/currency?currency=USDT'
        self.body = ''
        return self.method, self.path, self.body

    def account_transfer(self):
        # 资金划转
        self.method = 'POST'
        self.path = '/v1/api/account/transfer'
        self.body = json.dumps({"currency": "USDT", "amount": "0.01", "from": "c2c", "to": "l2c", "toPair": "ETH_USDT"})
        # self.body = {"base": "EOS", "quote": "ETH", "buyType": 0, "price": "12.12", "count": "2.12"}
        return self.method, self.path, self.body

    def withdrawal_all(self):
        # 获取所有币种提币记录
        self.method = 'GET'
        self.path = '/v1/api/account/withdrawal/history?pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

    def withdrawal_one(self):
        # 获取单币种提币记录
        self.method = 'GET'
        self.path = '/v1/api/account/withdrawal/history/currency?currency=USDT&pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

    def deposit_address(self):
        # 获取充币地址
        self.method = 'GET'
        self.path = '/v1/api/account/deposit/address?coinType=USDT&chainType=ERC20'
        self.body = ''
        return self.method, self.path, self.body

    def account_deposit(self):
        # 获取所有币种充币记录
        self.method = 'GET'
        self.path = '/v1/api/account/deposit/histoty?pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

    def bill_flow(self):
        # 查询账单流水记录
        self.method = 'GET'
        self.path = '/v1/api/spot/bill_flow?pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

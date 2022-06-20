
#行情部分----------------------------------------------------------------


class CanShu_02:
    def ory_kline(self):  # 获取K线数据
        self.method = 'GET'
        self.path = '/v1/market/history/kline?pairName=BTC_USDT&granularity=60'
        self.body = ''
        return self.method, self.path, self.body


    def trade(self):  # 获取市场深度数据
        self.method = 'GET'
        self.path = '/v1/market/depth?pairName=BTC_USDT'
        self.body = ''
        return self.method, self.path, self.body


    def market_depth(self):  # 获取成交数据
        self.method = 'GET'
        self.path = '/v1/market/depth?pairName=BTC_USDT'
        self.body = ''
        return self.method, self.path, self.body


    def kline24h(self):
        # 获取某个ticker信息
        self.method = 'GET'
        self.path = '/v1/market/history/kline24h?pairName=BTC_USDT'
        self.body = ''
        return self.method, self.path, self.body


    def kline24h_all(self):  # 获取全部ticker信息
        self.method = 'GET'
        self.path = '/v1/market/history/kline24h/all'
        self.body = ''
        return self.method, self.path, self.body



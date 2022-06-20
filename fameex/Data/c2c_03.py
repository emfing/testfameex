import json


class CanShu_03:
    def spot_orders_buy(self):
        # 币币下单买入
        self.method = 'POST'
        self.path = '/v1/api/spot/orders'
        self.body = json.dumps({"base": "EOS", "quote": "ETH", "buyType": 0, "price": "12.12", "count": "2.12"})
        #self.body = {"base": "EOS", "quote": "ETH", "buyType": 0, "price": "12.12", "count": "2.12"}
        return self.method, self.path, self.body

    def spot_orders_sell(self):
        # 币币下单卖出
        self.method = 'POST'
        self.path = '/v1/api/spot/orders'
        self.body = '{"base":"EOS","quote":"ETH","buyType":1,"price":"12.12","count":"1.12"}'
        return self.method, self.path, self.body

    def cancel_orders_all(self):
        # 币币批量撤单
        self.method = 'POST'
        self.path = '/v1/api/spot/cancel_orders_all'
        self.body = '{"buyType":-1,"base":"EOS","quote":"ETH","startTime":0,"endTime":0}'
        return self.method, self.path, self.body

    def order_detail(self):
        # 获取委托单详情
        self.method = 'GET'
        self.path = '/v1/api/spot/orderdetail?orderId=10551081030480560128&pairName=EOS_ETH'
        self.body = ''
        return self.method, self.path, self.body

    def order_list(self):
        # 获取委托单列表
        self.method = 'GET'
        self.path = '/v1/api/spot/orderlist?type=0&buyType=-1&pairName=BTC_USDT&pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

    def spot_fills(self):
        # 获取成交明细
        self.method = 'GET'
        self.path = '/v1/api/spot/fills?pairName=BTC_USDT&orderId=10551158213064523776&buyType=0&pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

    def orders_pending(self):
        # 获取所有未完成的订单
        self.method = 'GET'
        self.path = '/v1/api/orders_pending?pairName=BTC_USDT&pageNum=1&pageSize=10'
        self.body = ''
        return self.method, self.path, self.body

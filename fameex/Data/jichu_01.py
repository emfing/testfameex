'''
所有的请求方式，类型。
'''
class CanShu_01:
    def timestamp(self):  # 获取当前系统时间
        self.method = 'GET'
        self.path = '/v1/common/timestamp'
        self.body = ''
        return self.method, self.path, self.body

    def symbols(self):  # 获取所有交易币对
        self.method = 'GET'
        self.path = '/v1/common/symbols'
        self.body = ''
        return self.method, self.path, self.body

    def currencys(self):  # 获取所有交易币种
        self.method = 'GET'
        self.path = '/v1/common/currencys'
        self.body = ''
        return self.method, self.path, self.body


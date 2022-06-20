import pytest
import requests

from fameex.Data.c2c_03 import CanShu_03
from fameex.HmacSHA.sha256 import JiaMi
from fameex.url.fameex_url import TEST


class Test_03():
    def test_spot_buy(self):
        '''币币下单买入'''
        ss = CanShu_03()
        method,path,body = ss.spot_orders_buy()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.post(url=TEST + path, headers=headers, data=body)
        print(res.json())
        assert res.status_code == 200

    def test_spot_sell(self):
        '''币币下单卖出'''
        ss = CanShu_03()
        method,path,body = ss.spot_orders_sell()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.post(url=TEST + path, headers=headers, data=body)
        print(res.json())
        assert res.status_code == 200


    def test_order_detail(self):
        '''获取委托单详情'''
        ss = CanShu_03()
        method,path,body = ss.order_detail()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_order_list(self):
        '''获取委托单列表'''
        ss = CanShu_03()
        method, path, body = ss.order_list()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200




    def test_spot_fills(self):
        '''获取成交明细'''
        ss = CanShu_03()
        method, path, body = ss.spot_fills()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200



    def test_orders_pending(self):
        '''获取所有未完成的订单aaaa'''
        ss = CanShu_03()
        method, path, body = ss.orders_pending()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


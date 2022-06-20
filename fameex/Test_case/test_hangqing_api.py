import pytest
import requests

from fameex.Data.hangqiang_02 import CanShu_02
from fameex.HmacSHA.sha256 import JiaMi
from fameex.url.fameex_url import TEST


class Test_02():
    def test_ory_kline(self):
        '''获取K线数据'''
        ss = CanShu_02()
        method, path, body = ss.ory_kline()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_trade(self):
        '''市场深度数据'''
        ss = CanShu_02()
        method, path, body = ss.trade()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_market_depth(self):
        '''获取成交数据'''
        ss = CanShu_02()
        method, path, body = ss.market_depth()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_kline24h(self):
        '''获取某个ticker信息'''
        ss = CanShu_02()
        method, path, body = ss.kline24h()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


    def test_kline24h_all(self):
        '''获取某个ticker信息'''
        ss = CanShu_02()
        method, path, body = ss.kline24h_all()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


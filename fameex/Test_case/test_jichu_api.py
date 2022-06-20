import pytest
import requests

from fameex.Data.jichu_01 import CanShu_01
from fameex.HmacSHA.sha256 import JiaMi
from fameex.url.fameex_url import TEST


class Test_01():
    def test_timestamp(self):
        '''获取当前系统时间'''
        ss = CanShu_01()
        method, path, body = ss.timestamp()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_symbols(self):
        '''获取所有交易币对'''
        ss = CanShu_01()
        method, path, body = ss.symbols()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_currencys(self):
        '''获取所有币种'''
        ss = CanShu_01()
        method, path, body = ss.currencys()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()
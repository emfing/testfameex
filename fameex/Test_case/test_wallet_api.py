import pytest
import requests

from fameex.Data.wallet_04 import CanShu_04
from fameex.HmacSHA.sha256 import JiaMi
from fameex.url.fameex_url import TEST


class Test_03():
    def test_account_wallet(self):
        ''' 获取钱包账户信息'''
        ss = CanShu_04()
        method, path, body = ss.account_wallet()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


    def test_wallet_currency(self):
        ''' 获取钱包账户某币种详情'''
        ss = CanShu_04()
        method, path, body = ss.wallet_currency()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


    def test_account_transfer(self):
        '''资金划转'''
        ss = CanShu_04()
        method,path,body = ss.account_transfer()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.post(url=TEST + path, headers=headers, data=body)
        print(res.json())
        assert res.status_code == 200

    def test_withdrawal_all(self):
        ''' 获取所有币种提币记录'''
        ss = CanShu_04()
        method, path, body = ss.withdrawal_all()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200

    def test_withdrawal_one(self):
        '''获取单币种提币记录'''
        ss = CanShu_04()
        method, path, body = ss.withdrawal_one()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200



    def test_deposit_address(self):
        '''获取充币地址'''
        ss = CanShu_04()
        method, path, body = ss.deposit_address()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


    def test_account_deposit(self):
        '''获取所有币种充币记录'''
        ss = CanShu_04()
        method, path, body = ss.account_deposit()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200


    def test_bill_flow(self):
        '''获取所有币种充币记录'''
        ss = CanShu_04()
        method, path, body = ss.bill_flow()
        hea = JiaMi(method, path, body)
        headers = hea.getHeader()
        res = requests.get(url=TEST + path, headers=headers, params=body)
        print(res.json())
        assert res.status_code == 200



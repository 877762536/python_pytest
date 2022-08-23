#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
import requests

from utils.http import http_client
import json
import yaml
import os

host = "https://dev-api.qipei-tong.com"


@pytest.fixture
def my_fixture():
    print("111")
    yield
    print("222")

def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    parent_path = os.path.abspath('.')
    with open(parent_path + test_data_path) as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters

cases, parameters = get_test_data("/data/login.yaml")
list_params=list(parameters)

class TestInTheaters(object):
    def test_in_theaters(self):
        http_rsp = http_client.send_get(host+list_params[0][1]["path"], list_params[0][1]["params"])
        print(http_rsp.json())
        assert http_rsp.json()["code"] == list_params[0][2]['response']['code']
        #assert http_rsp.json()["msg"] == "60s内不可重新发送。"

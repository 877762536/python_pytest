#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
import requests

from utils.http import http_client
import json
import yaml
import os

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
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self, dologin,env, case, http, expected):
        print(env["host"])
        http_rsp = http_client.send_get(env["host"]+http["path"], http["params"])
        print(http_rsp.json())
        assert http_rsp.json()["code"] == expected['response']['code']
        #assert http_rsp.json()["msg"] == "60s内不可重新发送。"

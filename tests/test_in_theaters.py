#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
import requests

from utils.http import http_client
import json

get_code_url = "https://dev-api.qipei-tong.com/User/v1/Login/GetVerificationCode"


@pytest.fixture
def my_fixture():
    print("111")
    yield
    print("222")


class TestInTheaters(object):
    def test_in_theaters(self):

        params = {"mobile": "18200000000",
                  "code_type": "VERIFICATION_CODE_LOGIN"}
        http_rsp = http_client.send_get(get_code_url, params)
        print(http_rsp.json())
        assert http_rsp.json()["code"] == "0"
        #assert http_rsp.json()["msg"] == "60s内不可重新发送。"

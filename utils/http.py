
import requests
 
class http_client:
    """
    根据传入的URL、请求方式和请求参数来发送请求，并返回requests.models.Response
    """
    def __init__(self):
        pass
 
    @staticmethod
    def send_post(url, params=None):
        # 传回的是json对象
        try:
            res = requests.post(url=url, data=params)
            return res
        except Exception as msg:
            return msg
 
    @staticmethod
    def send_get(url, params=None):
        try:
            res = requests.get(url=url, params=params)
            return res
        except Exception as msg:
            return msg
 
    def run_main(self, url, method, params=None):
        if method == 'GET':
            print('This is a get request')
            res = self.send_get(url, params)
        elif method == 'POST':
            print('This is a post request')
            res = self.send_post(url, params)
        # print('返回requests.models.Response：')
            return res
        else:
            print('请重新输入请求方式')
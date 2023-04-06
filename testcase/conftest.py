import os

from utils.RequestsUtil import Request
import pytest

request = Request()


# @pytest.fixture
# def login():
#     url = "https://passport.csdn.net/v1/register/pc/login/doLogin"
#     method = "post"
#     headers = {
#         "Accept": "application/json, text/plain, */*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
#     }
#     payload = {"userIdentification": "18576797850", "pwdOrVerifyCode": "lkjLKJ+2023", "loginType": "1",
#                "webUmidToken": "", "uaToken": ""}
#     res = request.requests_api(method=method, url=url, json=payload, headers=headers)
#     print(res.content)
#     print(res.status_code)


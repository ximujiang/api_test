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



@pytest.fixture(scope="session", autouse=True)
def login():
    url = "http://cce.org.uooconline.com/user/login"
    method = "post"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    payload = {"account": 18576797850,
               # "afs_appkey": "FFFF0N00000000006409",
               "afs_scene": "ic_register",
               # "afs_sessionId": "01X1369koYjXTki0b74FBYZDeTa2SUi3mFTriH831rss8fxaYBW-EJXTU5hEB650JyCFRuqe12ipXc5VtY4d-TrkPZQTDGW49ZVO_Un30M0RPAZGhKbxSymy3rZksIVZzCm-sTtpWZiubQ2qcBTOIznQ",
               # "afs_sig": "05XqrtZ0EaFgmmqIQes-s-CMWW5F8vT1x71dy8X_rceWt_fRbYqK7vXpJ75kZ_U6klKeTk3Y03N2usTUCm11UWlBbbyo5m8aQ40iKfH4SF1VkRrIz_5pkqsOCw_xp146j071LHdd3TMJlWtlGYUouJa2-IeenxB1tH5aJlRAe8YloXxi81f8sDbHkbrcHOPQMl2zEQBPdafynb0-1YOHnQR8pPDiQLa3hpzvMXXhIy8Jw5iLneT2ss1H668DxedgmwUo5hEevLO09YqQectGQ_rECqjGBEoOrKUEfj5OPBi7QM3O39Vctt7nStngHFUQ-ODjTUgzbtrQ2vXrf_K4lIRQWmDnTtOGBqDWgi7vwNzwzi7zpKy8dMG6lSZgFOKLto",
               # "afs_token": "1676644556861:0.15485453521557346",
               "encode": 1,
               "password": "bGtqMzgxNQ==",
               "remember": True}
    res = request.requests_api(method=method, url=url, data=payload, headers=headers)
    print(res.text)
    print(res.status_code)


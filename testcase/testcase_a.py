import requests
import pytest

sess = requests.session()


@pytest.fixture(scope=scope,
                params=params,
                autouse=autouse,
                ids=ids,
                name=name)
def login(request):
    respose = sess.request("get", f'{request.param}', verify=False)
    return respose.text


def test_a2(login):
    print("登录成功了")
    print(login)

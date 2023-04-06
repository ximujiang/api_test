import pytest
from requests.adapters import HTTPAdapter
from . import http_session

g = {}   # 全局 g 对象，获取项目配置


@pytest.fixture(scope="session")
def requests_session(request):
    """全局session 全部用例仅执行一次"""
    s = http_session.HttpSession()
    # max_retries=2 重试2次
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    proxies_ip = request.config.getoption("--proxies-ip") or request.config.getini("proxies_ip")
    if proxies_ip:
        # 添加全局代理
        s.proxies = {
            "http": f"http://{proxies_ip}",
            "https": f"https://{proxies_ip}"
        }
    # 添加全局base_url
    s.base_url = request.config.option.base_url
    yield s
    s.close()


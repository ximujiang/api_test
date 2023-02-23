from selenium import webdriver
import pytest



@pytest.fixture(scope="function")
def login():
    driver =  webdriver.Chrome()
    return driver


def test_a2(login):
    login.get("http://baidu.com")
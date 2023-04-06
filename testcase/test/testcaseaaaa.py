import json
import os

import allure
import pytest
import allure

from kw.casekw.casekw import CaseKw


class TestCaseClass(CaseKw):

    @allure.title("测试用例")
    @allure.id("10086")
    @allure.severity('normal')
    def test_case_title(self):
        self.get_case_step(selector='get_case_step')

    # @allure.title("测试用例1")
    # @allure.id("10087")
    # @allure.severity('normal')
    # def test_case_title_1(self):
    #     self.get_case_step(selector='get_case')


if __name__ == '__main__':
    pytest.main()

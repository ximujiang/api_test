import os

import allure
import pytest
import allure
from kw.learn.learn import Learn
from utils.yamlutil import YamlUtil

from common.get_file_path import FilePath


class TestLearn(FilePath, YamlUtil, Learn):

    @allure.story("测试用例")
    def test_learn(self):
        res = self.read_yaml(self.get_path(__file__))["test_learn"]
        res = self.video_learn(res)
        # print(f)
        # print(fp)
        print(res)

    def test_learn1(self):
        print(self.get_path(__file__))

        # print(Learn().video_learn())
    # def test_learn_1(self):
    #     print("xxxxxx")
    #     # print(Learn().video_learn())
    # def test_learn_2(self):
    #     print("xxxxxx")
    #     # print(Learn().video_learn())


if __name__ == '__main__':
    pytest.main()

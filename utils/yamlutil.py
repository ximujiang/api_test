import inspect

import yaml
import os
from jsonpath import jsonpath
from pytest_yaml_yoyo import extract

from common.get_file_path import FilePath
import pytest_yaml_yoyo
extract
class YamlUtil(FilePath):

    def read_yaml(self, path):
        """
        读取yaml文件数据
        :return:
        """
        with open(path, encoding='utf-8') as fp:
            value = yaml.load(stream=fp, Loader=yaml.FullLoader)
            return value

    def write_yaml(self, path, data):
        """
        写入数据
        :return:
        """
        with open(path, encoding='utf-8', mode='w') as fp:
            yaml.dump(data, stream=fp, allow_unicode=True)

    def updata_yaml(self, path, k, v):
        old_data = self.read_yaml(path)  # 读取文件数据
        old_data[k] = v  # 修改读取的数据（k存在就修改对应值，k不存在就新增一组键值对）
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(old_data, f)

    def get_data(self, selector):
        case = inspect.stack()[3][3]
        FilePath = self.get_path()
        data = self.read_yaml(FilePath)
        print(eval(data['test_case2']['get_xxx']['request']['keyword']))
        res = data[case][selector]
        res_copy = res.copy()
        return res

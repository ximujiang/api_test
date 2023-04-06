import inspect
import os
import sys


class FilePath:
    def get_path(self):
        # # #获取当前的文件路径
        cwd = os.getcwd()
        # 获取模块名称
        module_name = self.__module__.split('.')[-1]
        data_name = module_name + '.yaml'
        data_path = os.path.join(cwd, data_name)
        return data_path




import yaml
import os


class YamlUtil:

    def read_yaml(self, path, key=None):
        """
        读取yaml文件数据
        :return:
        """
        with open(path, encoding='utf-8') as fp:
            value = yaml.load(stream=fp, Loader=yaml.FullLoader)
            if key is None:
                return value
            else:
                return value['key']

    def write_yaml(self, path, data):
        """
        写入数据
        :return:
        """
        with open(path, encoding='utf-8', mode='w') as fp:
            yaml.dump(data, stream=fp, allow_unicode=True)

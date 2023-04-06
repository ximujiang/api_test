# API_TEST
接口自动化测试框架
python+pytest+allure+Jenkins

1、多环境的配置与切换
总的来说：url 绝对地址 > config 中的base_url > 命令行参数–base-url > pytest.ini 文件中的 base_url > config.py 的 BASE_UR
用例中引用配置参数可以用 ${env.配置参数} 取到配置中的值。
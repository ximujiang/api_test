# https://welink.huaweicloud.com/athenatenant/v1/findcontextawareevent?name=1&pageNumber=1&pageSize=10&startTime=2023-04-12&endTime=2023-05-12&n=0.6196937384807566&language=zh
# get
# ame=1&pageNumber=1&pageSize=10&startTime=2023-04-12&endTime=2023-05-12&n=0.6196937384807566&language=zh

# 查看详情
# https://welink.huaweicloud.com/athenatenant/v1/pushdetail?id=b584a2d1-874f-4a94-b723-dfebb47daee9&tick=1&n=0.6075089006199896&language=zh
# get
# id=b584a2d1-874f-4a94-b723-dfebb47daee9&tick=1&n=0.6075089006199896&language=zh
from utils import http_session


class push:
    def __init__(self):
        self.request = http_session.HttpSession

    def find_context_aware_event(self, parameters):
        """
        查看推送列表
        """
        path = '/athenatenant/v1/findcontextawareevent'
        method = 'get'
        res = self.request.send_request(method=method, url=path, params=parameters)
        return res

    def push_detail(self):
        """
        查看推送信息详情
        """
        pass

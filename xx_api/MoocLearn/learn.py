from utils.RequestsUtil import Request
import json

request = Request()


class Learns:
    def mark_video(self, payload):
        url = "http://cce.org.uooconline.com/home/learn/markVideoLearn"
        method = "POST"
        headers = {"Accept": "application/json, text/plain, */*"}
        print(payload)
        res = request.requests_api(method=method, url=url, data=payload, headers=headers)
        res1 = json.loads(res.text)
        return res1

from utils.RequestsUtil import Request
import json
request = Request()


# def test_work(login):
#     url = "http://cce.org.uooconline.com/league/school"
#     method = "get"
#     headers = {
#         "Accept": "application/json, text/plain, */*",
#
#     }
#     # payload = {"username": "u011640418"}
#     res = request.requests_api(method=method, url=url, headers=headers)
#     print(res.text)
#     print(res.status_code)
#     print(res.request.url)
#     print(res.content)

def test_finish(login):
    url = "http://cce.org.uooconline.com/home/course/list?keyword=&page=1&type=finish"
    method = "get"
    headers = {
        "Accept": "application/json, text/plain, */*",

    }
    # payload = {"username": "u011640418"}
    res = request.requests_api(method=method, url=url, headers=headers)
    print(res.request.url)
    print(res.text)
    res1 = json.loads(res.text)
    print(res1)
    print(res1["code"])


if __name__ == '__main__':
    test_finish()

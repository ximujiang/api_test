import requests


class Request:
    session = requests.session()

    def requests_api(self, method, url, **kwargs):
        res = Request.session.request(method, url, **kwargs)
        return res

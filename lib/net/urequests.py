import requests

Response = requests.Response

def request(method, url, params=None, cookies=None, data=None, json=None, headers={}, parse_headers=True, followRedirect=True):
    return requests.request(method, url, params=params, cookies=cookies, data=data, json=json, headers=headers, allow_redirects=followRedirect)


def head(url, **kw):
    return request("HEAD", url, **kw)

def get(url, **kw):
    return request("GET", url, **kw)

def post(url, **kw):
    return request("POST", url, **kw)

def put(url, **kw):
    return request("PUT", url, **kw)

def patch(url, **kw):
    return request("PATCH", url, **kw)

def delete(url, **kw):
    return request("DELETE", url, **kw)
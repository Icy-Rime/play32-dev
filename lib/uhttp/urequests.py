import requests

Response = requests.Response

def request(method, url, data=None, json=None, headers={}, stream=None):
    return requests.request(method, url, data=data, json=json, headers=headers, stream=stream)


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
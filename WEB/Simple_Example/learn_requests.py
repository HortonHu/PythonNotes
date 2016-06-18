#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

# Make a Request
r = requests.get('https://api.github.com/events')
print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
print r.json()

# HTTP methods
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')


# Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
# 得到 http://httpbin.org/get?key2=value2&key1=value1
# 如果value为None 那么这对key-value就不会被加入url

# 传入多个value
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
# 得到 http://httpbin.org/get?key1=value1&key2=value2&key2=value3

# Response Content
import requests
r = requests.get('https://api.github.com/events')
print r.text
print r.encoding
r.encoding = 'ISO-8859-1'
print r.text

# Binary Response Content
print r.content           # The gzip and deflate transfer-encodings are automatically decoded
# create an image from binary data returned by a request
from PIL import Image
from StringIO import StringIO
i = Image.open(StringIO(r.content))

# JSON Response Content
import requests
r = requests.get('https://api.github.com/events')
r.json()

# Raw Response Content
r = requests.get('https://api.github.com/events', stream=True)
print r.raw
r.raw.read(10)
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size):
#         fd.write(chunk)

# Custom Headers
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

# More complicated POST requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

# POST a Multipart-Encoded File
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
print r.text

# Response Status Codes
r = requests.get('http://httpbin.org/get')
print r.status_code
print r.status_code == requests.codes.ok

bad_r = requests.get('http://httpbin.org/status/404')
print bad_r.status_code
bad_r.raise_for_status()        # raise http_error

# Response Headers
print r.headers
print r.headers['Content-Type']
print r.headers.get('content-type')

# Cookies
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
# access cookies
print r.cookies['example_cookie_name']
# send cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text

# Redirection and History
r = requests.get('http://github.com')
print r.url
print r.status_code
print r.history
# disable redirection
r = requests.get('http://github.com', allow_redirects=False)
print r.status_code
print r.history
# enable redirection
r = requests.head('http://github.com', allow_redirects=True)
print r.status_code
print r.history

# Timeouts
requests.get('http://github.com', timeout=0.001)

# Errors and Exceptions

# Session Objects
# persist certain parameters across requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)



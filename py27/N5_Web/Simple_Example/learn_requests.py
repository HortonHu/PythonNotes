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

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

r = requests.get('https://api.github.com/events')
print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
print r.json()

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
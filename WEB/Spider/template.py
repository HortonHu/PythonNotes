#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests


url = r'http:\\'
proxies = {}
params = {}
post_data = {}
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Referer': 'itself',
}

req = requests.get(url, params=params, headers=headers, timeout=5)
soup = BeautifulSoup(req.content)

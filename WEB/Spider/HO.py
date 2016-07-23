# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5000/auth/login'
session = requests.session()
r = session.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
csrf_token = soup.find(id='csrf_token')['value']


post_data = {
    'csrf_token': str(csrf_token),
    'email': 'wcbieyuan@gmail.com',
    'password': '123456',
}


rr = session.post(url, post_data)

print rr.content

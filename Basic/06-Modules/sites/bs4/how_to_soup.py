# -*- coding:utf-8 -*-

"""
文档：
https://github.com/delongw/beautifulsoup/blob/master/docs/index.rst
"""

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 获取标准缩进格式输出
print soup.prettify()

# 浏览结构化数据的方法
print soup.title
print soup.title.name
print soup.title.string
print soup.title.parent.name
print soup.p
print soup.p['class']
print soup.find_all('a')
print soup.find(id="link3")

# 从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print link.get('href')

# 文档中获取所有文字内容:
print soup.get_text

#


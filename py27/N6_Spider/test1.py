#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
req = urllib2.Request('http://www.pythontab.com')
response = urllib2.urlopen(req)
the_page = response.read()

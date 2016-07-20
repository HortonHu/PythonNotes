# -*- coding:utf-8 -*-

# cd c:\redis
# redis-server.exe redis.windows.conf
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print r.get('foo')

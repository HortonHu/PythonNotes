# -*- coding:utf-8 -*-


import pymongo

# 连接服务器
client = pymongo.MongoClient('localhost', 27017)
# 连接到数据库 example, 不存在则创建 也可以用字典的形式访问client['example']
db = client.example

# 一个数据库可以有任意多个集合 集合就是放置文档的地方, 对MongoDB的大部分操作都是在集合对象上的
# 获得数据库中的集合列表
print db.collection_names()
# 如果没有添加任何集合则为空，添加文档的时候，会自动创建集合

# 获得代表集合widgets的对象 或者用 db['widgets']
widgets = db.widgets
# 插入文档
widgets.insert({"foo": "bar"})
# 此时集合列表不再为空
print db.collection_names()

# 插入文档 在插入任何文档的时候都会自动添加 _id域 它的值是一个ObjectID
widgets.insert({"name": "flibnip", "description": "grade-A industrial flibnip", "quantity": 3})
# 取出文档
doc = widgets.find_one({"name": "flibnip"})
print doc, doc['name'], doc['quantity']

# 字典的改变并不会自动保存到数据库中。如果你希望把字典的改变保存，需要调用集合的 save方法，
doc['quantity'] = 4
db.widgets.save(doc)
print db.widgets.find_one({"name": "flibnip"})

# 添加更多文档
widgets.insert({"name": "smorkeg", "description": "for external use only", "quantity": 4})
widgets.insert({"name": "clobbasker", "description": "properties available on request", "quantity": 2})
# 通过集合的find方法获取集合中所有文档的列表
for doc in widgets.find():
    print doc

# 使用集合的remove方法删除一个文档
widgets.remove({"name": "flibnip"})


# MongoDB 和 JSON
# 文档中因为含有 _id 键， 不能直接转化
# 可以从字典里简单地删除 _id 键的方法来解决
import json
del doc["_id"]
json.dumps(doc)

# 也可以使用PyMongoDB的 json_util库











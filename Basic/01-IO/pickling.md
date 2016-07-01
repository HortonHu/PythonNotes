## 序列化 
把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

1. Python提供两个模块来实现序列化：cPickle和pickle
区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理
用的时候，先尝试导入cPickle，如果失败，再导入pickle
```
try:
    import cPickle as pickle
except ImportError:
    import pickle
```
把一个对象序列化并写入文件：
```
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件
```    
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
```
f = open('dump.txt', 'wb')
pickle.dump(d, f)           # 将d给pickle之后写入文件f
f.close()
```
把对象从磁盘读到内存时，可以先把内容读到一个str 然后用pickle.loads()方法反序列化出对象
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
反序列化刚才保存的对象：
```
f = open('dump.txt', 'rb')
d = pickle.load(f)          # 从文件f中反序列化给d
f.close()
print d
```
这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

2. JSON（JavaScript Object Notation）
在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

|JSON类型	|   Python类型|
|:--:|:--:|
|{}|	        dict|
|[]|	        list|
|"string"|	    'str'或u'unicode'|
|1234.56|	    int或float|
|true/false|	True/False|
|null|	        None|
Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
把Python对象变成一个JSON：
```
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
```
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
```
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
```
反序列化得到的所有字符串对象默认都是unicode而不是str。
由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。

3. JSON进阶
Python的dict对象可以直接序列化为JSON的{}，
不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

```
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)      # 得到一个TypeError
print json.dumps(s)
```
报错是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
dumps()方法还提供了一大堆的可选参数
可选参数default就是把任意一个对象变成一个可序列为JSON的对象，


我们只需要为Student专门写一个转换函数，再把函数传进去即可
```
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print json.dumps(s, default=student2dict)   # 传入转化函数student2dict
Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
```
如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
```
print json.dumps(s, default=lambda obj: obj.__dict__)
```

同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例：
```
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
```
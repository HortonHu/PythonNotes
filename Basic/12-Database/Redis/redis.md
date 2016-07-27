
## Redis 有三个主要使其有别于其它很多竞争对手的特点：
- Redis是完全在内存中保存数据的数据库，使用磁盘只是为了持久性目的；
- Redis相比许多键值数据存储系统有相对丰富的数据类型；
- Redis可以将数据复制到任意数量的从服务器中；

## Redis优点
- 异常快速 : Redis是非常快的，每秒可以执行大约110000设置操作，81000个/每秒的读取操作。
- 支持丰富的数据类型 : Redis支持最大多数开发人员已经知道如列表，集合，可排序集合，哈希等数据类型。
这使得在应用中很容易解决的各种问题，因为我们知道哪些问题处理使用哪种数据类型更好解决。
- 操作都是原子的 : 所有 Redis 的操作都是原子，从而确保当两个客户同时访问 Redis 服务器得到的是更新后的值（最新值）。
- MultiUtility工具：Redis是一个多功能实用工具，可以在很多如：缓存，消息传递队列中使用（Redis原生支持发布/订阅），在应用程序中，如：Web应用程序会话，网站页面点击数等任何短暂的数据；


## 安装
Ubuntu ：
1. `sudo apt-get install redis`
2. `sudo pip install redis`

Windows:
1. 从https://github.com/ServiceStack/redis-windows下载
2. 安装服务`redis-server --service-install redis.windows.conf --loglevel verbose`
3. 启动`redis-server --service-start`

## Redis环境
要在 Ubuntu 上安装 Redis，打开终端，然后输入以下命令：
$sudo apt-get update
$sudo apt-get install redis-server
这将在您的计算机上安装Redis
启动 Redis

$redis-server
查看 redis 是否还在运行

$redis-cli
这将打开一个 Redis 提示符，如下图所示：
redis 127.0.0.1:6379>
在上面的提示信息中：127.0.0.1 是本机的IP地址，6379是 Redis 服务器运行的端口。现在输入 PING 命令，如下图所示：
redis 127.0.0.1:6379> ping
PONG
这说明现在你已经成功地在计算机上安装了 Redis。


## Redis数据类型
Redis 支持5种数据类型，字符串、哈希、列表、集合、集合排序

### 字符串
Redis 字符串是一个字节序列。在 Redis 中字符串是二进制安全的，这意味着它们没有任何特殊终端字符来确定长度，所以可以存储任何长度为 512 兆的字符串。
示例
redis 127.0.0.1:6379> SET name "yiibai"
OK
redis 127.0.0.1:6379> GET name
"yiibai"
在上面的例子中，SET 和 GET 是 Redis 命令，name 和 "yiibai" 是存储在 Redis 的键和字符串值。

### 哈希
Redis哈希是键值对的集合。 Redis哈希是字符串字段和字符串值之间的映射，所以它们用来表示对象。
示例
redis 127.0.0.1:6379> HMSET user:1 username yiibai password yiibai points 200
OK
redis 127.0.0.1:6379> HGETALL user:1

1) "username"
2) "yiibai"
3) "password"
4) "yiibai"
5) "points"
6) "200"
在上面的例子中，哈希数据类型用于存储包含用户基本信息的用户对象。这里 HSET，HEXTALL 是 Redis 命令同时 user:1 也是一个键。

### 列表
Redis 列表是简单的字符串列表，通过插入顺序排序。可以添加一个元素到 Redis 列表的头部或尾部。
示例
redis 127.0.0.1:6379> lpush tutoriallist redis
(integer) 1
redis 127.0.0.1:6379> lpush tutoriallist mongodb
(integer) 2
redis 127.0.0.1:6379> lpush tutoriallist rabitmq
(integer) 3
redis 127.0.0.1:6379> lrange tutoriallist 0 10

1) "rabitmq"
2) "mongodb"
3) "redis"
列表的最大长度为  2的32次方 - 1 个元素（4294967295，每个列表的元素超过四十亿）。

### 集合
Redis 集合是字符串的无序集合。在 Redis 可以添加，删除和测试成员存在的时间复杂度为 O（1）。
示例
redis 127.0.0.1:6379> sadd tutoriallist redis
(integer) 1
redis 127.0.0.1:6379> sadd tutoriallist mongodb
(integer) 1
redis 127.0.0.1:6379> sadd tutoriallist rabitmq
(integer) 1
redis 127.0.0.1:6379> sadd tutoriallist rabitmq
(integer) 0
redis 127.0.0.1:6379> smembers tutoriallist

1) "rabitmq"
2) "mongodb"
3) "redis"
注：在上面的例子中 rabitmq 被添加两次，但由于它是只集合具有唯一特性。集合中的成员最大数量为 2的32次方 - 1（4294967295，每个集合有超过四十亿条记录）。

### 集合排序
不同的是，一个有序集合的每个成员都可以排序，就是为了按有序集合排序获取它们，按权重分值从最小到最大排序。虽然成员都是独一无二的，按权重分数值可能会重复。
示例
redis 127.0.0.1:6379> zadd tutoriallist 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd tutoriallist 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd tutoriallist 0 rabitmq
(integer) 1
redis 127.0.0.1:6379> zadd tutoriallist 0 rabitmq
(integer) 0
redis 127.0.0.1:6379> ZRANGEBYSCORE tutoriallist 0 1000

1) "redis"
2) "mongodb"
3) "rabitmq"























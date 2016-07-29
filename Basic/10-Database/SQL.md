# SQL
结构化查询语言(Structured Query Language)，使我们有能力访问数据库，是一种 ANSI 的标准计算机语言。


# RDBMS
关系型数据库管理系统。
RDBMS 中的数据存储在被称为表（tables）的数据库对象中。

# SQL四种语言：DDL,DML,DCL,TCL
1.DDL（Data Definition Language）数据库定义语言statements are used to define the database structure or schema.

DDL是SQL语言的四大功能之一。
用于定义数据库的三级结构，包括外模式、概念模式、内模式及其相互之间的映像，定义数据的完整性、安全控制等约束
DDL不需要commit.
CREATE
ALTER
DROP
TRUNCATE
COMMENT
RENAME

2.DML（Data Manipulation Language）数据操纵语言statements are used for managing data within schema objects.

由DBMS提供，用于让用户或程序员使用，实现对数据库中数据的操作。
DML分成交互型DML和嵌入型DML两类。
依据语言的级别，DML又可分成过程性DML和非过程性DML两种。
需要commit.
SELECT
INSERT
UPDATE
DELETE
MERGE
CALL
EXPLAIN PLAN
LOCK TABLE

3.DCL（Data Control Language）数据库控制语言  授权，角色控制等
GRANT 授权
REVOKE 取消授权

4.TCL（Transaction Control Language）事务控制语言
SAVEPOINT 设置保存点
ROLLBACK  回滚
SET TRANSACTION

# SQL 中最重要的 DDL 语句- 创建新数据库
ALTER DATABASE  -    修改数据库  
CREATE TABLE    -    创建新表  
DROP TABLE      -    删除表  
ALTER TABLE     -    变更（改变）数据库表  
CREATE INDEX    -    创建索引（搜索键）  
DROP INDEX      -    删除索引  

# SQL语法
SELECT - 从数据库表中获取数据  
UPDATE - 更新数据库表中的数据  
DELETE - 从数据库表中删除数据  
INSERT INTO - 向数据库表中插入数据  


# SELECT 语句
SELECT 列名称 FROM 表名称
SELECT * FROM 表名称

# SELECT DISTINCT 语句
关键词 DISTINCT 用于返回唯一不同的值
SELECT DISTINCT 列名称 FROM 表名称

# WHERE 子句
有条件地从表中选取数据
SELECT 列名称 FROM 表名称 WHERE 列 运算符 值
SQL 使用单引号来环绕文本值（大部分数据库系统也接受双引号）。如果是数值，请不要使用引号。

下面的运算符可在 WHERE 子句中使用
操作符	描述
=	等于
<>	不等于
>	大于
<	小于
>=	大于等于
<=	小于等于
BETWEEN	在某个范围内
LIKE	搜索某种模式

# AND & OR 运算符
用于基于一个以上的条件对记录进行过滤.AND 和 OR 可在 WHERE 子语句中把两个或多个条件结合起来。
如果第一个条件和第二个条件都成立，则 AND 运算符显示一条记录。如果第一个条件和第二个条件中只要有一个成立，则 OR 运算符显示一条记录。
SELECT * FROM Persons WHERE FirstName='Thomas' AND LastName='Carter'
SELECT * FROM Persons WHERE firstname='Thomas' OR lastname='Carter'
SELECT * FROM Persons WHERE (FirstName='Thomas' OR FirstName='William')
AND LastName='Carter'

# ORDER BY 子句
用于对结果集进行排序。默认按照升序对记录进行排序。如果您希望按照降序对记录进行排序，可以使用 DESC 关键字。
SELECT Company, OrderNumber FROM Orders ORDER BY Company
SELECT Company, OrderNumber FROM Orders ORDER BY Company, OrderNumber
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC

# INSERT INTO 语句
用于向表格中插入新的行。
INSERT INTO table_name VALUES (值1, 值2,....)
指定所要插入数据的列：
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)

# UPDATE 语句
用于修改表中的数据。
UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值

# DELETE 语句
用于删除表中的行。
DELETE FROM 表名称 WHERE 列名称 = 值
在不删除表的情况下删除所有的行。这意味着表的结构、属性和索引都是完整的：
DELETE FROM table_name
DELETE * FROM table_name

# TOP 子句
用于规定要返回的记录的数目。并非所有的数据库系统都支持 TOP 子句。
SQL Server 的语法：
SELECT TOP number|percent column_name(s) FROM table_name
MySQL 和 Oracle 中的 SQL SELECT TOP 是等价的：
SELECT column_name(s) FROM table_name LIMIT number
TOP PERCENT 实例：
选取 50% 的记录。
SELECT TOP 50 PERCENT * FROM Persons

# LIKE 操作符
用于在 WHERE 子句中搜索列中的指定模式。
SELECT column_name(s) FROM table_name WHERE column_name LIKE pattern


# 通配符
在搜索数据库中的数据时，SQL 通配符可以替代一个或多个字符。
SQL 通配符必须与 LIKE 运算符一起使用。
在 SQL 中，可使用以下通配符：
%	                          替代一个或多个字符
_	                          仅替代一个字符
[charlist]	                  字符列中的任何单一字符
[^charlist]或[!charlist]      不在字符列中的任何单一字符

使用 NOT 关键字
SELECT * FROM Persons WHERE City NOT LIKE '%lon%'

# IN 操作符
允许我们在 WHERE 子句中规定多个值。
SELECT column_name(s) FROM table_name WHERE column_name IN (value1,value2,...)

# BETWEEN 操作符
在 WHERE 子句中使用，作用是选取介于两个值之间的数据范围。
操作符 BETWEEN ... AND 会选取介于两个值之间的数据范围。这些值可以是数值、文本或者日期。
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2
可以和NOT一起使用

# Alias（别名）
表的 SQL Alias 语法
SELECT column_name(s) FROM table_name AS alias_name
列的 SQL Alias 语法
SELECT column_name AS alias_name FROM table_name
假设我们有两个表分别是："Persons" 和 "Product_Orders"。我们分别为它们指定别名 "p" 和 "po"。
SELECT po.OrderID, p.LastName, p.FirstName FROM Persons AS p, Product_Orders AS po 
WHERE p.LastName='Adams' AND p.FirstName='John'

# JOIN
用于根据两个或多个表中的列之间的关系，从这些表中查询数据。
有时为了得到完整的结果，我们需要从两个或更多的表中获取结果。我们就需要执行 join。
JOIN: 如果表中有至少一个匹配，则返回行（INNER JOIN 与 JOIN 是相同的。）
LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
FULL JOIN: 只要其中一个表中存在匹配，就返回行
# INNER JOIN 关键字
在表中存在至少一个匹配时，INNER JOIN 关键字返回行。
SELECT column_name(s)
FROM table_name1
INNER JOIN table_name2 
ON table_name1.column_name=table_name2.column_name
# LEFT JOIN 关键字
从左表 (table_name1) 那里返回所有的行，即使在右表 (table_name2) 中没有匹配的行。
在某些数据库中， LEFT JOIN 称为 LEFT OUTER JOIN。
SELECT column_name(s)
FROM table_name1
LEFT JOIN table_name2 
ON table_name1.column_name=table_name2.column_name
# RIGHT JOIN 关键字
右表 (table_name2) 那里返回所有的行，即使在左表 (table_name1) 中没有匹配的行。
SELECT column_name(s)
FROM table_name1
RIGHT JOIN table_name2 
ON table_name1.column_name=table_name2.column_name
# FULL JOIN 关键字
只要其中某个表存在匹配，FULL JOIN 关键字就会返回行。
在某些数据库中， FULL JOIN 称为 FULL OUTER JOIN。
SELECT column_name(s)
FROM table_name1
FULL JOIN table_name2 
ON table_name1.column_name=table_name2.column_name
FULL JOIN 关键字会从左表 (Persons) 和右表 (Orders) 那里返回所有的行。
如果 "Persons" 中的行在表 "Orders" 中没有匹配，或者如果 "Orders" 中的行在表 "Persons" 中没有匹配，这些行同样会列出。

# UNION 和 UNION ALL 操作符
用于合并两个或多个 SELECT 语句的结果集。
UNION 操作符选取不同的值。如果允许重复的值，请使用 UNION ALL。
UNION 结果集中的列名总是等于 UNION 中第一个 SELECT 语句中的列名。
UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。
SELECT column_name(s) FROM table_name1
UNION
SELECT column_name(s) FROM table_name2

# SELECT INTO 语句可用于创建表的备份复件。
SELECT INTO 语句从一个表中选取数据，然后把数据插入另一个表中。
SELECT INTO 语句常用于创建表的备份复件或者用于对记录进行存档。
所有的列插入新表：
SELECT * INTO new_table_name [IN externaldatabase] FROM old_tablename
制作 "Persons" 表的备份复件：
SELECT *
INTO Persons_backup
FROM Persons
IN 子句可用于向另一个数据库中拷贝表：
SELECT *
INTO Persons IN 'Backup.mdb'
FROM Persons
如果我们希望拷贝某些域，可以在 SELECT 语句后列出这些域：
SELECT LastName,FirstName
INTO Persons_backup
FROM Persons
ELECT INTO 实例 - 带有 WHERE 子句
SELECT LastName,Firstname
INTO Persons_backup
FROM Persons
WHERE City='Beijing'

# CREATE DATABASE 语句
用于创建数据库。
CREATE DATABASE database_name
# CREATE TABLE 语句
用于创建数据库中的表。
CREATE TABLE 表名称
(
列名称1 数据类型,
列名称2 数据类型,
列名称3 数据类型,
....
)
数据类型（data_type）规定了列可容纳何种数据类型。下面包含了SQL中最常用的数据类型：
integer(size)、int(size)、smallint(size)、tinyint(size)        仅容纳整数。在括号内规定数字的最大位数。
decimal(size,d)、numeric(size,d)、容纳带有小数的数字。"size"    规定数字的最大位数。"d" 规定小数点右侧的最大位数。
char(size)	             容纳固定长度的字符串（可容纳字母、数字以及特殊字符）。在括号中规定字符串的长度。
varchar(size)	          容纳可变长度的字符串（可容纳字母、数字以及特殊的字符）。在括号中规定字符串的最大长度。
date(yyyymmdd)	         容纳日期。

CREATE TABLE 实例
CREATE TABLE Persons
(
Id_P int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)

# 约束 (Constraints)
约束用于限制加入表的数据的类型。
可以在创建表时规定约束（通过 CREATE TABLE 语句），或者在表创建之后也可以（通过 ALTER TABLE 语句）。
我们将主要探讨以下几种约束：

- NOT NULL      强制列不接受 NULL 值。
- UNIQUE        唯一标识数据库表中的每条记录。 
- PRIMARY KEY   约束唯一标识数据库表中的每条记录 拥有自动定义的 UNIQUE 约束。
- FOREIGN KEY   一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY。
- CHECK         约束用于限制列中的值的范围。
- DEFAULT       用于向列中插入默认值。

//TODO  
CREATE TABLE Persons
(
Id_P int NOT NULL UNIQUE CHECK (Id_P>0),
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255) DEFAULT 'Sandnes'
)

# CREATE INDEX 语句
用于在表中创建索引。
您可以在表中创建索引，以便更加快速高效地查询数据。
用户无法看到索引，它们只能被用来加速搜索/查询。
注释：更新一个包含索引的表需要比更新一个没有索引的表更多的时间，这是由于索引本身也需要更新。因此，理想的做法是仅仅在常常被搜索的列（以及表）上面创建索引。
CREATE INDEX index_name ON table_name (column_name)
在表上创建一个唯一的索引。唯一的索引意味着两个行不能拥有相同的索引值。
CREATE UNIQUE INDEX index_name
ON table_name (column_name)

# 撤销索引、表以及数据库
使用 DROP 语句，可以轻松地删除索引、表和数据库。
令删除表格中的索引。
ALTER TABLE table_name DROP INDEX index_name
DROP TABLE 表名称
DROP DATABASE 数据库名称
仅仅需要除去表内的数据，但并不删除表本身
TRUNCATE TABLE 表名称

# ALTER TABLE 语句
用于在已有的表中添加、修改或删除列。
# 建两张表：用户表和文章表，文章只存作者编号，不存作者名字
import sqlite3

conn = sqlite3.connect("join.db")
cur = conn.cursor()
# 先删旧表，保证这个脚本能反复运行，不会再报“表已存在”
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS posts")

cur.execute("CREATE TABLE users (id INTEGER, name TEXT, age INTEGER)")
cur.execute("INSERT INTO users VALUES (5, '阿哲', 27)")
cur.execute("INSERT INTO users VALUES (9, '梅梅', 24)")
cur.execute("INSERT INTO users VALUES (14, '大壮', 35)")
cur.execute("INSERT INTO users VALUES (21, '小雨', 29)")

cur.execute("CREATE TABLE posts (id INTEGER, title TEXT, user_id INTEGER)")
cur.execute("INSERT INTO posts VALUES (101, '今天学会了 FastAPI', 9)")
cur.execute("INSERT INTO posts VALUES (102, 'SQLite 真香', 5)")
cur.execute("INSERT INTO posts VALUES (103, '被 404 折磨的一天', 9)")
cur.execute("INSERT INTO posts VALUES (104, '周末去哪玩', 21)")
cur.execute("INSERT INTO posts VALUES (105, '数据库重启不丢了', 5)")
conn.commit()

# 题 1：查出每篇文章的标题和它的作者名字，按文章编号排序，这句你写
cur.execute("SELECT posts.title,users.name FROM users join posts ON posts.user_id = users.id GROUP BY posts.id ")
rows = cur.fetchall()
print("题1：", rows)

# 题 2：只查梅梅写的文章标题，这句你写
cur.execute("SELECT posts.title FROM users join posts ON posts.user_id = users.id WHERE users.name = '梅梅'")
rows = cur.fetchall()
print("题2：", rows)

#统计每个作者写了几篇文章，查出作者名和篇数。用上 COUNT(*) 和 GROUP BY，连接条件跟题 1 一样。预期三行：阿哲 2、梅梅 2、小雨 1。
cur.execute("SELECT users.name,COUNT(*) FROM users join posts ON posts.user_id = users.id GROUP BY users.id ")
rows = cur.fetchall()
print("题3：", rows)

# 看这个数据库里一共有哪几张表
cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
print("所有表：", cur.fetchall())

conn.close()
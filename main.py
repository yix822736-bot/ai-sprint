# 导入：这次多拿 sqlite3 操作数据库，原来的两个照旧
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 数据模板：交进来的用户数据必须长这样
class UserIn(BaseModel):
    name: str
    age: int

# 开连接的工具：每次办事前开一个，行设置成能当字典用
def get_conn():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn

# 启动先建表：表不存在才建，存在就跳过，所以反复启动不报错
conn = get_conn()
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
conn.commit()
conn.close()

# 大门：有人访问根地址，就回一句话
@app.get("/")
def home():
    return {"message": "我的店开门了"}

# 列表窗口：从数据库查年龄够大的用户
@app.get("/users")
def list_users(min_age: int = 0):
    conn = get_conn()
    rows = conn.execute("SELECT id, name, age FROM users WHERE age >= ? ORDER BY id", (min_age,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        result.append(dict(r))
    return result

# 查人窗口：按编号从数据库查，查不到回 404
@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_conn()
    row = conn.execute("SELECT id, name, age FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="没有这个用户")
    return dict(row)

# 收人窗口：新用户写进数据库，编号由数据库自动发，回 201
@app.post("/users", status_code=201)
def create_user(user: UserIn):
    conn = get_conn()
    cur = conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "name": user.name, "age": user.age}

# 改人窗口：按编号改数据库里那一行，一行没动就是没这个人
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserIn):
    conn = get_conn()
    cur = conn.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (user.name, user.age, user_id))
    conn.commit()
    changed = cur.rowcount
    conn.close()
    if changed == 0:
        raise HTTPException(status_code=404, detail="没有这个用户")
    return {"id": user_id, "name": user.name, "age": user.age}

# 删人窗口：按编号删数据库里那一行，一行没动就是没这个人
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    changed = cur.rowcount
    conn.close()
    if changed == 0:
        raise HTTPException(status_code=404, detail="没有这个用户")
    return {"message": "已删除"}
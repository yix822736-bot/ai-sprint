# 导入：这次多拿一个 HTTPException，专门用来回错误
from fastapi import FastAPI, HTTPException
# 导入多加一句：做数据模板的图纸
from pydantic import BaseModel

# 数据模板：交进来的用户数据必须长这样，少字段、类型错都会被挡
class UserIn(BaseModel):
    name: str
    age: int


app = FastAPI()

# 用户数据：只存这一份，两个窗口共用
users = [
    {"id": 3, "name": "阿哲", "age": 27},
    {"id": 7, "name": "梅梅", "age": 24},
    {"id": 12, "name": "大壮", "age": 35},
]

# 大门：有人访问根地址，就回一句话
@app.get("/")
def home():
    return {"message": "我的店开门了"}


# 列表窗口升级：可以带条件，只回年龄够大的用户
@app.get("/users")
def list_users(min_age: int = 0):
    result = []
    for u in users:
        if u["age"] >= min_age:
            result.append(u)
    return result


# 查人窗口：按编号在数据里真找，找到给人，找不到回 404
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="没有这个用户")

# 收人窗口：有人 POST 交一个新用户，就存进数据里，回 201
@app.post("/users", status_code=201)
def create_user(user: UserIn):
    max_id = 0
    for u in users:
        if u["id"] > max_id:
            max_id = u["id"]
    new_user = {"id": max_id + 1, "name": user.name, "age": user.age}
    users.append(new_user)
    return new_user

# 改人窗口：按编号找到人，把名字和年龄换成新交来的
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserIn):
    for u in users:
        if u["id"] == user_id:
            u["name"] = user.name
            u["age"] = user.age
            return u
    raise HTTPException(status_code=404, detail="没有这个用户")

# 删人窗口：按编号找到人，从数据里删掉
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            return {"message": "已删除"}
    raise HTTPException(status_code=404, detail="没有这个用户")

# 编写规范

## 内部模块

模块：可以使用 `_xxx.py` 表示

```py
# _format_user.py
def format_user(user: User):
  item: dict = {
    "id": user.id,
    "name": user.name,
    "email": user.email,
    "avatar": user.avatar,
    "created_at": user.created_at,
    "updated_at": user.updated_at,
  }
  return item
```

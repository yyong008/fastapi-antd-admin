# 通用

## 获取记录


```py
async def get_record(
    async_session: AsyncSession,  # 异步 session
    model: Type,  # 模型类型，例如 User, Department 等
    filters: List,  # 过滤条件列表
    options: Optional[List] = None,  # 加载选项 (如 joinedload)
    first: bool = False  # 是否只获取第一个结果
):
    query = select(model).filter(*filters)

    if options:
        query = query.options(*options)  

    result = await async_session.execute(query)

    if first:
        return result.scalars().first()  # 返回单个结果
    return result.scalars().all()  # 返回所有结果
```

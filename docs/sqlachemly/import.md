# import

本导入主要关注 SQLAlchemy 的异步相关

### sqlalchemy 表相关

```py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
```

### sqlalchemy.orm

```py
from sqlalchemy.orm import Session # 同步 Session
```

### sqlalchemy.ext

> 异步 AsyncSession

```py
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
```

### sqlalchemy.sql

```py
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy import and_
```

### sqlalchemy.exc

```py
from sqlalchemy.exc import SQLAlchemyError
```

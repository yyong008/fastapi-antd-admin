# FastAPI Ant Admin Backend

## 启动项目

### 1. 安装依赖

```bash
cd backend
poetry install
```

### 2. 配置环境变量

复制 `.env.example` 文件（如果存在）并重命名为 `.env`，然后根据需要修改配置。

### 3. 启动服务

```bash
poetry run uvicorn main_app:app --reload
```

### 4. 访问 API 文档

启动后访问：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

# fastapi-antd-admin

a full stack web framework for antd-admin (WIP)

## 技术栈

- ⚡ FastAPI
  - 🧰SQLAlchemy
  - 💾PostgreSQL
  - 🤖Uvicorn
  - 🔍Pydantic
- 🌐React
  - 💯TypeScript、Vite、Hooks and other modern features
  - 🎨antd/pro-component/tailwindcss
  - 🎯@tanstack/router
- 🔒 Secure
  - 🔑 JWT token authentication.

## install and run

```bash
# clone
git clone https://github.com/yyong008/fastapi-antd-admin

# backend
cd backend
poetry install

cp .env.example .env
# set env file

# frontend
cd frontend
pnpm i
pnpm run dev
```

- server dev use vscode debugger run server and server on `http://localhost:8000` and docs on `http://localhost:8000/docs`
- fontend dev use vscode debugger run server and server on `http://localhost:5173`

## todo

- [ ] tanstack-query 改造前端 api
- [ ] admin 页面有数
- [ ] 数据库优化相关操作优化
- [ ] 文档用 fumadocs 的内容
- [ ] 其它

# fastapi
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

# config
from app.config.config import settings as config

# db
from app.db.client import init_db

# middleware
from app.middlewares.count_requests import CountRequeset
from app.middlewares.demo_mode import DemoModeMiddleware

# exception handler
from app.exception import http_exception_handler

# router
from app.router import router
from app.router.metrics import router as metries_router
from app.router.health import router as health_check_router
from app.router.home import router as home_router

init_db()

app = FastAPI(title="Remix Antd Admin FastAPI", summary="Remix Antd admin",  description="一个管理系统 With Remix", debug=config.DEBUG)

app.mount("/static", StaticFiles(directory="static"), name="static")

# register middlewares
app.add_middleware(CountRequeset)
app.add_middleware(DemoModeMiddleware)

# register exception handler
app.add_exception_handler(HTTPException, http_exception_handler)

# register routers
app.include_router(router, prefix="/api")
app.include_router(metries_router)
app.include_router(health_check_router)
app.include_router(home_router)

if __name__ == "__main__":
   import uvicorn
   uvicorn.run("main:app", host=config.SERVER_HOST, port=int(config.SERVER_PORT), reload=True)

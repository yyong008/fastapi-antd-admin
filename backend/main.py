# fastapi
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# config
from app.config.config import get_settings

# db
from app.db.client import init_db

# middleware
from app.middlewares.count_requests import CountRequeset
from app.middlewares.demo_mode import DemoModeMiddleware

# exception handler
from app.exception import http_exception_handler, validation_exception_handler

# router
from app.api import router
from app.api.metrics import router as metries_router
from app.api.health import router as health_check_router
from app.api.home import router as home_router

init_db()
config = get_settings()

app = FastAPI(
    title="FastAPI Antd Admin FastAPI",
    summary="FastAPI Antd admin",
    description="一个管理系统 With FastAPI",
    debug=config.DEBUG,
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# register middlewares
app.add_middleware(CountRequeset)
app.add_middleware(DemoModeMiddleware)

# register exception handler
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(HTTPException, validation_exception_handler)

if config.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in config.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# register routers
app.include_router(router, prefix="/api")
app.include_router(metries_router)
app.include_router(health_check_router)
app.include_router(home_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", host=config.SERVER_HOST, port=int(config.SERVER_PORT), reload=True
    )

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.prometheus import REQUESTS_COUNT


class CountRequeset(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        REQUESTS_COUNT.inc()  # 增加计数器
        response = await call_next(request)
        return response

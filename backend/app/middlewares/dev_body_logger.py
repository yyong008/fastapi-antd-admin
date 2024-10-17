import json
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging

app = FastAPI()

class DebugMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 记录请求方法和路径
        logging.info(f"Request: {request.method} {request.url}")

        request_body = await request.body()

        # Determine Content-Type
        content_type = request.headers.get("Content-Type", "")

        if "application/json" in content_type:
            # Handle JSON
            if request_body:
                logging.info(f"Request body (bytes): {request_body}")
        
        elif "application/x-www-form-urlencoded" in content_type or "multipart/form-data" in content_type:
            # Handle form data
            # if request_body:
            #     logging.info(f"Request body (bytes): {request_body.decode('utf-8')}")
            pass

        # 调用下一个中间件或路由处理程序
        response = await call_next(request)

        # 读取响应内容
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        # 输出响应内容
        logging.info(f"Response status: {response.status_code}")
        # 返回新的 Response 对象，因为响应体已经被消费，需要重新创建
        return Response(content=response_body, status_code=response.status_code, headers=dict(response.headers))

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    message = exc.detail.split(": ", 1)[-1] if ": " in exc.detail else exc.detail
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": 1, "message": message, "data": {}},
    )

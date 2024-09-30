from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    message = exc.detail.split(": ", 1)[-1] if ": " in exc.detail else exc.detail
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": 1, "message": message, "data": {}},
    )

def validation_exception_handler(request, exc: RequestValidationError):
    messages = [f"{err['loc'][-1]}: {err['msg']}" for err in exc.errors()]
    return JSONResponse(
        status_code=422,
        content={
            "code": 1,
            "message": ", ".join(messages),
            "data": {}
        },
    )

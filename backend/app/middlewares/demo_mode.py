from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import app.config as config


class DemoModeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if int(config.PRESENTATION_MODE) == 1 and request.method in (
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
        ):
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={
                    "detail": "The application is in demo mode. All modifications are disabled."
                },
            )
        response = await call_next(request)
        return response

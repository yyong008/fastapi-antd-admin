from fastapi import APIRouter

from .loginlog import router as loginlog_router
from .serve import router as serve_router

router = APIRouter(prefix="/monitor")

router.include_router(loginlog_router, tags=["Admin System Minitor LoginLog"])
router.include_router(serve_router, tags=["Admin System Minitor Serve"])

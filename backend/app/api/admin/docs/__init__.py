from fastapi import APIRouter

from .changelog import router as changelog_router
from .feedback import router as feedback_router

router = APIRouter(prefix="/docs")

router.include_router(changelog_router)
router.include_router(feedback_router)

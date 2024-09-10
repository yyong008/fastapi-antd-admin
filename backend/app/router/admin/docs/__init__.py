from fastapi import APIRouter

from .changelog import router as changelog_router
from .feedback import router as feedback_router

router = APIRouter()

router.include_router(changelog_router, prefix="/news")
router.include_router(feedback_router, prefix="/news")

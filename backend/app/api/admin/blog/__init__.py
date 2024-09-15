from fastapi import APIRouter

from .main import router as main_router
from .category import router as category_router
from .tag import router as tag_router

router = APIRouter(prefix="/blog")

router.include_router(main_router)
router.include_router(category_router)
router.include_router(tag_router)

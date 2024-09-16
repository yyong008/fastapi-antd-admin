from fastapi import APIRouter

from .main import router as main_router
from .category import router as category_router

router = APIRouter(prefix="/news")

router.include_router(main_router)
router.include_router(category_router)

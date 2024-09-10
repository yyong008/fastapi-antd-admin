from fastapi import APIRouter

from .account import router as main_router
from .link_category import router as link_category_router
from .link import router as link_router

router = APIRouter()

router.include_router(main_router, prefix="/profile")
router.include_router(link_category_router, prefix="/profile")
router.include_router(link_router, prefix="/profile")

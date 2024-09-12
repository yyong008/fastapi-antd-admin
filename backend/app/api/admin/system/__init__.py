from fastapi import APIRouter

from .config import router as config_router
from .dept import router as dept_router
from .dict_item import router as dict_item_router
from .dict import router as dict_router
from .menu import router as menu_router
from .role import router as role_router
from .user import router as user_router
from .monitor import router as monitor_router


router = APIRouter(prefix="/system")

router.include_router(config_router)
router.include_router(dept_router)
router.include_router(dict_item_router)

router.include_router(dict_router)
router.include_router(menu_router)
router.include_router(role_router)
router.include_router(user_router)
router.include_router(monitor_router)

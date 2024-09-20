from fastapi import APIRouter, Depends

from .upload import router as upload_file_router
from .admin import router as admin_router
from .auth import router as auth_router
from .client import router as client_router

from ..deps.authorize import auth_required

router = APIRouter()

dependencies = [Depends(auth_required)]

router.include_router(auth_router)
router.include_router(client_router)
router.include_router(admin_router, dependencies=dependencies)
router.include_router(upload_file_router, dependencies=dependencies)

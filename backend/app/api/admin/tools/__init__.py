from fastapi import APIRouter

from .mail import router as mail_router
from .storage import router as storage_router


router = APIRouter()

router.include_router(mail_router, prefix="/tools")
router.include_router(storage_router, prefix="/tools")

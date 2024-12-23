from fastapi import APIRouter

from .blog import router as blog_router
from .news import router as news_router
from .docs import router as docs_router
from .profile import router as profile_router
from .tools import router as tools_router
from .system import router as system_router
from .userinfo.userinfo import router as userinfo_router
from .dashboard.main import router as dashboard_router
from .signin_log import router as signin_log_router
from .chat.langchain_chat import router as langchain_router

router = APIRouter(prefix="/admin")

router.include_router(dashboard_router)
router.include_router(blog_router)
router.include_router(news_router)
router.include_router(docs_router)
router.include_router(profile_router)
router.include_router(tools_router)
router.include_router(system_router)
router.include_router(userinfo_router)
router.include_router(signin_log_router)
router.include_router(langchain_router)

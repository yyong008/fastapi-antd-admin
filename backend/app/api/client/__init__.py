from fastapi import APIRouter
from .news.news import router as news_router
from .blog.blog import router as blog_router

router = APIRouter()

router.include_router(news_router,prefix='/news')
router.include_router(blog_router,prefix='/blog')

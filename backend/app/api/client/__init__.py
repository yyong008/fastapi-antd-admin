from fastapi import APIRouter
from .news.news import router as news_router

router = APIRouter(prefix='/news')

router.include_router(news_router)

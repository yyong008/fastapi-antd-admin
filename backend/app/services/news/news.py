from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.news.news import get_news_count, get_news_list



def format_news(news):
    item = {
        "id": news.id,
        "title": news.title,
        "content": news.content,
        "author": news.author,
        "source": news.source,
        "viewCount": news.viewCount,
        # "publishAt": news.publishAt,
    }
    return item


def get_news_list_service(category_id, page, pageSize, db: Session):
    try:
        count = get_news_count(category_id,db)
        news = get_news_list(db, page, pageSize, category_id)

        news_list = []
        for n in news:
            item = format_news(n)
            news_list.append(item)

        data = {"total": count, "list": news_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")



from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.news.news_category import get_news_category_count, get_news_category_list


def format_news_category(news_category):
    item = {
        "id": news_category.id,
        "name": news_category.name,
        "description": news_category.description,
        "userId": news_category.user_id,
    }
    return item


def get_news_category_list_service(page, pageSize, db: Session):
    try:
        count = get_news_category_count(db)
        news_category = get_news_category_list(db, page, pageSize)

        nc_list = []
        for nc in news_category:
            item = format_news_category(nc)
            nc_list.append(item)

        data = {"total": count, "list": nc_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.news.news import create_news, get_news_by_id, get_news_count, get_news_list
from app.services.news.format import format_news, format_news_by_id


def get_news_list_service(category_id, page, pageSize, db: Session):
    try:
        count = get_news_count(category_id, db)
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


def get_client_news_list_service(page, pageSize, db: Session):
    category_id = 1
    try:
        count = get_news_count(category_id, db)
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


def get_news_by_id_service(id, db):
    news = get_news_by_id(id, db)
    data = format_news_by_id(news)
    return data

def create_news_service(news, current_user_id, db):
    older_news = news
    news["news_id"] = older_news["categoryId"]
    news["user_id"] = current_user_id
    news["viewCount"] = 0
    del news["categoryId"]
    data = create_news(news, db)
    return format_news(data)

def update_news_service(news, db):
    # TODO: implement update news
    pass

def delete_news_by_ids_service(ids, db):
    # TODO: implement delete news
    pass

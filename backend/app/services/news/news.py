from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.news.news import create_news, get_news_by_id, get_news_count, get_news_list, update_news, delete_news_by_ids
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
    format_news_data = format_news_from_old_news(current_user_id, news)
    data = create_news(format_news_data, db)
    return format_news(data)

def update_news_service(id, news, current_user_id, db):
    format_news_data = format_news_from_old_news
    count = update_news(id, format_news_data, current_user_id, db)
    if count == 0:
        raise HTTPException(status_code=400, detail="Update failed")
    data = get_news_by_id(id, db)
    return format_news(data)

def delete_news_by_ids_service(ids, db):
    count = delete_news_by_ids(ids, db)
    return count

def format_news_from_old_news(current_user_id, news):
    older_news = news
    news["news_id"] = older_news["categoryId"] # TODO: database need change news_id to categoryId
    news["user_id"] = current_user_id
    news["viewCount"] = 0
    del news["categoryId"]
    return news

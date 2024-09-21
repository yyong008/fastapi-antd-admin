from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.news.news_category import (
    get_news_category_by_id,
    get_news_category_by_name,
    get_news_category_count,
    get_news_category_list,
)
from app.models.news import NewsCategory
from app.services.news.format import format_news_category


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


def create_news_category_service(news_category, user_id, db):
    try:
        nc = get_news_category_by_name(news_category["name"], db)
        if nc:
            raise HTTPException(status_code=400, detail="News category already exists")

        nc = NewsCategory(
            name=news_category["name"],
            description=news_category["description"],
            user_id=user_id,
        )
        db.add(nc)
        db.commit()
        db.refresh(nc)

        return format_news_category(nc)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


def update_news_category_service(id, news_category, user_id, db):
    try:
        nc = get_news_category_by_id(id, db)
        if not nc:
            raise HTTPException(
                status_code=400, detail="News category not already exists"
            )

        nc.name = news_category["name"]
        nc.description = news_category["description"]
        nc.user_id = user_id
        db.commit()
        db.refresh(nc)

        return format_news_category(nc)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


def delete_news_category_by_ids_service(ids, db):
    try:
        db.query(NewsCategory).filter(NewsCategory.id.in_(ids)).delete(
            synchronize_session=False
        )
        db.commit()
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")

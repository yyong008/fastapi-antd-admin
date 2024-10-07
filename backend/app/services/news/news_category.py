from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

import app.dal.news.news_category as nc_dals
from ._format import format_news_category

async def get_news_category_list_service(db: AsyncSession, page, pageSize):
    try:
        count = await nc_dals.get_news_category_count(db)
        news_category = await nc_dals.get_news_category_list(db, page, pageSize)

        nc_list = [format_news_category(nc) for nc in news_category]
        data = {"total": count, "list": nc_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_news_category_service(db: AsyncSession, news_category, user_id):
    try:
        nc = await nc_dals.get_news_category_by_name(db, news_category["name"])
        if nc:
            raise HTTPException(status_code=400, detail="News category already exists")

        nc = {
            "name": news_category["name"],
            "description": news_category["description"],
            "user_id": user_id,
        }
        nc = nc_dals.create_news_category(db, nc)

        return format_news_category(nc)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


async def update_news_category_service(db: AsyncSession, id: int, news_category, user_id):
    try:
        nc = await nc_dals.get_news_category_by_id(db, id)
        if not nc:
            raise HTTPException(
                status_code=400, detail="News category not already exists"
            )

        nc.name = news_category["name"]
        nc.description = news_category["description"]
        nc.user_id = user_id
        nc = await nc_dals.update_news_category_by_id(db, id, nc.model_dump())

        return format_news_category(nc)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


async def delete_news_category_by_ids_service(db: AsyncSession, ids: list[int]):
    try:
        count = await nc_dals.delete_news_category_by_ids(db, ids)
        if count == 0:
            raise HTTPException(status_code=400, detail="News category not already exists")
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")

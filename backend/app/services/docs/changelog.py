from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

import app.dal.docs.changelog as cl_dals
from ._format import format_changelog
from app.models.docs.changelog import ChangeLog


async def get_changelog_list_service(db: AsyncSession, page: int, pageSize: int):
    """
    获取更新列表
    """
    try:
        count = await cl_dals.get_changelog_count(db)
        changelogs = await cl_dals.get_changelog_list(db, page, pageSize)

        changelog_list = [format_changelog(cl) for cl in changelogs]

        data = {"total": count, "list": changelog_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def change_log_by_id_service(db: AsyncSession, id: int):
    """
    根据id获取更新
    """
    try:
        changelog = await cl_dals.get_changelog_by_id(db, id)
        return format_changelog(changelog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_change_log_service(db: AsyncSession, changelog, current_user_id):
    """
    创建更新
    """
    try:
        del changelog["user_id"]
        changelog["userId"] = current_user_id
        changelog = ChangeLog(**changelog)
        changelog = await cl_dals.create_changelog(db, changelog)
        return format_changelog(changelog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_change_log_service(db: AsyncSession, id, changelog, current_user_id):
    """
    更新更新
    """
    try:
        changelog_in_db = await cl_dals.get_changelog_by_id(db, id)

        changelog_in_db.userId = current_user_id
        if changelog_in_db is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        for key, value in changelog.items():
            if key == "created_at":
                continue
            setattr(changelog_in_db, key, value)
        changelog_in_db.userId = current_user_id

        changelog = await cl_dals.update_changelog_by_id(db, id, changelog_in_db)
        return format_changelog(changelog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_change_log_by_ids_service(db: AsyncSession, ids: list[int]):
    """
    根据ids删除更新
    """
    try:
        count = await cl_dals.delete_changelog_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

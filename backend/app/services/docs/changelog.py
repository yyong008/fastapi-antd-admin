from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.docs.changelog import (
    get_changelog_count,
    get_changelog_list,
    get_changelog_by_id,
    create_changelog,
    update_changelog_by_id,
    delete_changelog_by_ids,
)
from app.services.docs.format import format_changelog
from app.models.docs.changelog import ChangeLog


def get_user_list_service(page, pageSize, db: Session):
    try:
        count = get_changelog_count(db)
        changelogs = get_changelog_list(db, page, pageSize)

        changelog_list = []
        for cl in changelogs:
            item = format_changelog(cl)
            changelog_list.append(item)

        data = {"total": count, "list": changelog_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def change_log_by_id_service(id, db: Session):
    try:
        changelog = get_changelog_by_id(id, db)
        return format_changelog(changelog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_change_log_service(changelog, current_user_id, db: Session):
    try:
        del changelog['user_id']
        changelog['userId'] = current_user_id
        changelog = ChangeLog(**changelog)
        changelog = create_changelog(changelog, db)
        return format_changelog(changelog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_change_log_service(id, changelog, current_user_id, db: Session):
    try:
        changelog_in_db = get_changelog_by_id(id, db)

        changelog_in_db.userId = current_user_id
        if changelog_in_db is None:
            raise HTTPException(status_code=404, detail="Blog not found")
        
        for key, value in changelog.items():
            if key == "createdAt":
                continue
            setattr(changelog_in_db, key, value)
        changelog_in_db.userId = current_user_id

        changelog = update_changelog_by_id(db, id, changelog_in_db)
        return format_changelog(changelog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_change_log_by_ids_service(ids, db: Session):
    try:
        count = delete_changelog_by_ids(ids, db)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

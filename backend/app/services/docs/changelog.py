

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.docs.changelog import get_changelog_count,get_changelog_list
from app.services.docs.format import format_changelog

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
    pass

def create_change_log_service(name, db: Session):
    pass

def update_change_log_service(id, name, db: Session):
    pass

def delete_change_log_by_ids_service(ids, db: Session):
    pass

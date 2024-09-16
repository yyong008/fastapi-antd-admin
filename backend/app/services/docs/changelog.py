

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.docs.changelog import get_changelog_count,get_changelog_list


def format_changelog(changelog):
    item = {
        "id": changelog.id,
        "userId": changelog.userId,
        "publish_name": changelog.publish_name,
        "publish_version": changelog.publish_version,
        "type": changelog.type,
        "content": changelog.content,
        "url": changelog.url,
        "createdAt": changelog.createdAt,
        "updatedAt": changelog.updatedAt,
    }
    return item


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

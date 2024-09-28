from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.docs.feedback import get_feedback_count, get_feedback_list
from app.services.docs.format import format_feedback

def get_feedback_list_service(page, pageSize, db: Session):
    try:
        count = get_feedback_count(db)
        feedbacks = get_feedback_list(db, page, pageSize)

        feedback_list = []
        for fb in feedbacks:
            item = format_feedback(fb)
            feedback_list.append(item)

        data = {"total": count, "list": feedback_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def create_feedback_service(name, email, content, db: Session):
    pass

def delete_feedback_by_ids_service(ids, db: Session):
    pass

def update_feedback_service(id, name, email, content, db: Session):
    pass

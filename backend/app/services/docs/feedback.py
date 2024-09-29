from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.docs.feedback import (
    create_feedback,
    get_feedback_by_id,
    get_feedback_count,
    get_feedback_list,
)
from app.services.docs.format import format_feedback
from app.models.docs.feedback import FeedBack


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


def create_feedback_service(feedback, current_user_id, db: Session):
    try:
        del feedback['user_id']
        feedback['userId'] = current_user_id
        fb = FeedBack(**feedback)
        data = create_feedback(fb, db)
        return format_feedback(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_feedback_by_ids_service(ids, db: Session):
    try:
        data = delete_feedback_by_ids_service(ids, db)
        return format_feedback(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_feedback_service(id, name, email, content, db: Session):
    try:
        o_data = get_feedback_by_id(id, db)
        if o_data is None:
            raise HTTPException(status_code=400, detail="Feedback not found")
        data = update_feedback_service(id, name, email, content, db)
        return format_feedback(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

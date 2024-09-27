from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.docs.feedback import FeedBack


# =====================================GET===================================================
def get_feedback_count(db: Session):
    count = db.query(FeedBack).count()
    return count


def get_feedback_all(db: Session):
    sort_column = FeedBack.createdAt.desc()
    return db.query(FeedBack).order_by(sort_column).all()


def get_feedback_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    # sort_column = FeedBack.createdAt.desc()
    return db.query(FeedBack).offset(offset).limit(limit).all()

def create_feedback_category(feedback, db: Session):
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def update_feedback_by_id(db: Session, blog_id: int, feedback: FeedBack):
    db.query(FeedBack).filter(FeedBack.id == blog_id).update(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def delete_feedback_by_ids(ids, db):
    try:
        count = (
            db.query(FeedBack).filter(FeedBack.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.tools.mail import Mail


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Mail).count()
    return count


def get_mail_all(db: Session):
    sort_column = Mail.createdAt.desc()
    return db.query(Mail).order_by(sort_column).all()


def get_mail_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Mail.createdAt.desc()
    return db.query(Mail).order_by(sort_column).offset(offset).limit(limit).all()

def create_mail_category(mail, db: Session):
    db.add(mail)
    db.commit()
    db.refresh(mail)
    return mail

def update_mail_by_id(db: Session, mail_id: int, mail: Mail):
    db.query(Mail).filter(Mail.id == mail_id).update(mail)
    db.commit()
    db.refresh(mail)
    return mail

def delete_mail_by_ids(ids, db):
    try:
        count = (
            db.query(Mail).filter(Mail.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

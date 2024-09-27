from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.system.role import Role


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Role).count()
    return count


def get_roles_all(db: Session):
    sort_column = Role.createdAt.desc()
    return db.query(Role).order_by(sort_column).all()


def get_role_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Role.createdAt.desc()
    return db.query(Role).order_by(sort_column).offset(offset).limit(limit).all()

def create_role_category(role, db: Session):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def update_role_by_id(db: Session, mail_id: int, role: Role):
    db.query(Role).filter(Role.id == mail_id).update(role)
    db.commit()
    db.refresh(role)
    return role

def delete_role_by_ids(ids, db):
    try:
        count = (
            db.query(Role).filter(Role.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

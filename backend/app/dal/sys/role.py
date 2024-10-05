from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from app.models.system.role import Role


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Role).count()
    return count


def get_roles_all(db: Session):
    sort_column = Role.createdAt.desc()
    data = db.query(Role).order_by(sort_column).options(joinedload(Role.menus)).all()
    return data

def get_role_by_id(role_id: int, db: Session):
    role = db.query(Role).filter(Role.id == role_id).first()
    return role

def get_role_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Role.createdAt.desc()
    return db.query(Role).options(joinedload(Role.menus)).order_by(sort_column).offset(offset).limit(limit).all()

def create_role(role, db: Session):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def update_role_by_id(db: Session, role_id: int, role: Role):
    # db.query(Role).filter(Role.id == role_id).update(role)
    db.commit()
    db.refresh(role)
    return role

def delete_role_by_ids(ids, db):
    try:
        count = db.query(Role).filter(Role.id.in_(ids)).delete(synchronize_session=False)
        db.commit()
        if count == 0:
            raise HTTPException(status_code=400, detail="No data found")
        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

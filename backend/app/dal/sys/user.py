from sqlalchemy.orm import Session
from app.models.system.department import Department
from app.models.system.user import User
from sqlalchemy.orm import joinedload


# =====================================GET===================================================
def get_user_by_name(name: str, db: Session):
    return db.query(User).filter(User.name == name).first()


def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def get_count(db: Session):
    count = db.query(User).count()
    return count


def get_user_all(db: Session):
    sort_column = User.createdAt.desc()
    return (
        db.query(User)
        .order_by(sort_column)
        .options(joinedload(User.department).load_only(Department.name))
        .all()
    )


def get_user_by_id(user_id, db: Session):
    return (
        db.query(User)
        .filter_by(id=user_id)
        .options(joinedload(User.department).load_only(Department.name))
        .first()
    )


def get_users_by_ids(ids, db: Session):
    return db.query(User).filter(User.id.in_(ids)).all()


# =====================================CREATE===================================================
def create_user(name: str, email: str, hashed_password: str, db: Session):
    user = User(name=name, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# =====================================DELETE===================================================
def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None

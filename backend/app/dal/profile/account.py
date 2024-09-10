from sqlalchemy.orm import Session
from app.models.system.department import Department
from app.models.system.user import User
from sqlalchemy.orm import joinedload


# =====================================GET===================================================
def get_profile_account_by_name(name: str, db: Session):
    return db.query(User).filter(User.name == name).first()


def get_profile_account_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()


def get_profile_account_by_id(user_id, db: Session):
    return (
        db.query(User)
        .filter_by(id=user_id)
        .options(joinedload(User.department).load_only(Department.name))
        .first()
    )

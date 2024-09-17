from sqlalchemy.orm import Session
from app.models.system.loginlog import Loginlog


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Loginlog).count()
    return count


def get_Loginlog_by_name(name: str, db: Session):
    return db.query(Loginlog).filter(Loginlog.name == name).first()


def get_Loginlog_by_email(email: str, db: Session):
    return db.query(Loginlog).filter(Loginlog.email == email).first()


def get_Loginlog_by_id(id: int, db: Session):
    return db.query(Loginlog).filter(Loginlog.id == id).first()


def get_Loginlog_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Loginlog.login_at.desc()
    return db.query(Loginlog).order_by(sort_column).offset(offset).limit(limit).all()

def get_loginlog_latest_by_user_id(db, user_id):
    return db.query(Loginlog).filter(Loginlog.userId == user_id).first()
    
# =====================================CREATE===================================================
def create_loginlog(
    log,
    db: Session,
):
    loginlog_ins = Loginlog(
        name=log["name"],
        ip=log["ip"],
        address=log["address"],
        login_at=log["login_at"],
        system=log["system"],
        browser=log["browser"],
        userId=log["userId"],
    )

    db.add(loginlog_ins)
    db.commit()
    db.refresh(loginlog_ins)
    return loginlog_ins


# =====================================DELETE===================================================
def delete_Loginlog(loginlog_id: int, db: Session):
    loginlog = db.query(Loginlog).filter(Loginlog.id == loginlog_id).first()
    if loginlog:
        db.delete(loginlog)
        db.commit()
        return Loginlog
    return None

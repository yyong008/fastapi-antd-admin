from sqlalchemy.orm import Session
from app.models.system.user import UserSignLog
from app.utils.time import get_today_time
from sqlalchemy import select

# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(UserSignLog).count()
    return count


def get_user_signlog_all(db: Session):
    sort_column = UserSignLog.createdAt.desc()
    return db.query(UserSignLog).order_by(sort_column).all()


def get_user_signlog_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = UserSignLog.createdAt.desc()
    return db.query(UserSignLog).order_by(sort_column).offset(offset).limit(limit).all()


def get_user_today_is_sign_in_by_id(user_id, db: Session):
    start_time, end_time = get_today_time()
    result =  select(UserSignLog).where(
            UserSignLog.userId == user_id,
            UserSignLog.sign_time >= start_time,
            UserSignLog.sign_time < end_time,
        )
    return db.execute(result).scalars().first()


def get_signin_log_latest_by_user_id(db, user_id):
    return db.query(UserSignLog).filter(UserSignLog.userId == user_id).first()
    

# =====================================CREATE===================================================
async def create_user_signlog(sign_log, db: Session):
    # sign_log = UserSignLog(user_signlog)
    db.add(sign_log)
    db.commit()
    db.refresh(sign_log)
    return sign_log

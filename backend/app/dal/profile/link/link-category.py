from sqlalchemy.orm import Session
from app.models.profile.link import Link


# =====================================GET===================================================
def get_link_category_by_name(name: str, db: Session):
    return db.query(Link).filter(Link.name == name).first()


def get_link_category_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Link).offset(skip).limit(limit).all()


def get_link_category_count(db: Session):
    count = db.query(Link).count()
    return count


def get_link_category_all(db: Session):
    sort_column = Link.createdAt.desc()
    return db.query(Link).order_by(sort_column).all()


def get_link_category_by_id(link_id, db: Session):
    return db.query(Link).filter_by(id=link_id).first()


def get_link_category_by_ids(ids, db: Session):
    return db.query(Link).filter(Link.id.in_(ids)).all()

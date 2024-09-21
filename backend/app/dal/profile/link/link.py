from sqlalchemy.orm import Session
from app.models.profile.link import Link


# =====================================GET===================================================
def get_link_by_name(name: str, db: Session):
    return db.query(Link).filter(Link.name == name).first()


def get_link_by_email(email: str, db: Session):
    return db.query(Link).filter(Link.email == email).first()


def get_link_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Link).offset(skip).limit(limit).all()


def get_count(db: Session):
    count = db.query(Link).count()
    return count

def get_link_count_by_category_id(category_id, db: Session):
    count = db.query(Link).filter(Link.category_id == category_id).count()
    return count

def get_link_all(db: Session):
    sort_column = Link.createdAt.desc()
    return db.query(Link).order_by(sort_column).all()


def get_link_by_id(link_id, db: Session):
    return db.query(Link).filter_by(id=link_id).first()


def get_links_by_ids(ids, db: Session):
    return db.query(Link).filter(Link.id.in_(ids)).all()

def get_links_by_category_id(category_id, page, pageSize, db: Session):
    skip = pageSize * (page - 1)
    limit = pageSize
    return db.query(Link).filter(Link.category_id == category_id).offset(skip).limit(limit).all()
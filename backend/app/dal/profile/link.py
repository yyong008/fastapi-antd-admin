from sqlalchemy.orm import Session
from app.models.profile.link import LinkCategory


# =====================================GET===================================================
def get_link_by_name(name: str, db: Session):
    return db.query(LinkCategory).filter(LinkCategory.name == name).first()


def get_link_by_email(email: str, db: Session):
    return db.query(LinkCategory).filter(LinkCategory.email == email).first()


def get_link_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(LinkCategory).offset(skip).limit(limit).all()


def get_count(db: Session):
    count = db.query(LinkCategory).count()
    return count


def get_link_all(db: Session):
    sort_column = LinkCategory.createdAt.desc()
    return db.query(LinkCategory).order_by(sort_column).all()


def get_link_by_id(link_id, db: Session):
    return db.query(LinkCategory).filter_by(id=link_id).first()


def get_links_by_ids(ids, db: Session):
    return db.query(LinkCategory).filter(LinkCategory.id.in_(ids)).all()

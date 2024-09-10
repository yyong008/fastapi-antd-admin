from sqlalchemy.orm import Session
from app.models.blog import Blog


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Blog).count()
    return count


def get_blog_all(db: Session):
    sort_column = Blog.createdAt.desc()
    return db.query(Blog).order_by(sort_column).all()


def get_blog_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Blog.createdAt.desc()
    return db.query(Blog).order_by(sort_column).offset(offset).limit(limit).all()

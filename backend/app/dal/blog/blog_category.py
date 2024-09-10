from sqlalchemy.orm import Session
from app.models.blog import BlogCategory


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(BlogCategory).count()
    return count


def get_blog_category_all(db: Session):
    sort_column = BlogCategory.createdAt.desc()
    return db.query(BlogCategory).order_by(sort_column).all()


def get_blog_category_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = BlogCategory.createdAt.desc()
    return (
        db.query(BlogCategory).order_by(sort_column).offset(offset).limit(limit).all()
    )

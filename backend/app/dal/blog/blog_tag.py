from sqlalchemy.orm import Session
from app.models.blog import BlogTag


# =====================================GET===================================================
def get_blog_tag_count(db: Session):
    count = db.query(BlogTag).count()
    return count


def get_blog_tag_all(db: Session):
    sort_column = BlogTag.createdAt.desc()
    return db.query(BlogTag).order_by(sort_column).all()


def get_blog_tag_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    # sort_column = BlogTag.createdAt.desc()
    return db.query(BlogTag).offset(offset).limit(limit).all()

from fastapi import HTTPException
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

def get_blog_tag_by_id(id: int, db: Session):
    return db.query(BlogTag).filter(BlogTag.id == id).first()

def create_blog_tag(blog_tag, db: Session):
    db.add(blog_tag)
    db.commit()
    db.refresh(blog_tag)
    return blog_tag

def update_blog_tag_by_id(db: Session, blog_id: int, blog: BlogTag):
    db.query(BlogTag).filter(BlogTag.id == blog_id).update(blog)
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog_tag_by_ids(ids, db):
    try:
        count = (
            db.query(BlogTag).filter(BlogTag.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

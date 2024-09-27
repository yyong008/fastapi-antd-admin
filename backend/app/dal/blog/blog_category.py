from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.blog import BlogCategory


# =====================================GET===================================================
def get_blog_category_count(db: Session):
    count = db.query(BlogCategory).count()
    return count


def get_blog_category_all(db: Session):
    sort_column = BlogCategory.createdAt.desc()
    return db.query(BlogCategory).order_by(sort_column).all()


def get_blog_category_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    return (
        db.query(BlogCategory).offset(offset).limit(limit).all()
    )

def get_blog_category_by_id(id: int, db: Session):
    return db.query(BlogCategory).filter(BlogCategory.id == id).first()

def create_blog_category(blog_category, db: Session):
    db.add(blog_category)
    db.commit()
    db.refresh(blog_category)
    return blog_category

def update_blog_category_by_id(db: Session, blog_id: int, blog: BlogCategory):
    db.query(BlogCategory).filter(BlogCategory.id == blog_id).update(blog)
    db.commit()
    db.refresh(blog)
    return blog

def delete_news_by_ids(ids, db):
    try:
        count = (
            db.query(BlogCategory).filter(BlogCategory.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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

# =====================================CREATE===================================================
def create_blog_category(bc, db: Session):
    db.add(bc)
    db.commit()
    db.refresh(bc)
    return bc

# =====================================UPDATE===================================================
def update_blog_category_by_id(bc_id: int, bc, db: Session):
    # db.query(BlogCategory).filter(BlogCategory.id == bc_id).update(bc)
    db.commit()
    db.refresh(bc)
    return bc

# =====================================DELETE===================================================
def delete_news_by_ids(ids, db):
    try:
        count = (
            db.query(BlogCategory).filter(BlogCategory.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

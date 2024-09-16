from sqlalchemy.orm import Session
from app.models.blog import Blog


# =====================================GET===================================================
def get_blog_count(db: Session):
    count = db.query(Blog).count()
    return count


def get_blog_all(db: Session):
    sort_column = Blog.createdAt.desc()
    return db.query(Blog).order_by(sort_column).all()


def get_blog_list(db: Session, categoryId, tagId, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    # sort_column = Blog.createdAt.desc()

      # 构造基础查询
    query = db.query(Blog)

    # 动态添加过滤条件
    if categoryId is not None:
        query = query.filter(Blog.category_id == categoryId)
    if tagId is not None:
        query = query.filter(Blog.tag_id == tagId)
    return (
       query
        .offset(offset)
        .limit(limit)
        .all()
    )

def get_blog_by_id(blog_id: int, db: Session):
    return db.query(Blog).filter(Blog.id == blog_id).first()

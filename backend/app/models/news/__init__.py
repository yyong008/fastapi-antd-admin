from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.client import Base


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=True)
    source = Column(String, nullable=True)
    view_count = Column(Integer, default=0, nullable=False)
    published_at = Column(DateTime(timezone=True), nullable=False)
    news_id = Column(
        Integer, ForeignKey("news_category.id"), nullable=False
    )  # 外键，指向 NewsCategory
    user_id = Column(Integer, nullable=False)  # 上传用户，可能需要外键根据需求

    news = relationship("NewsCategory", back_populates="news")  # 反向关系


class NewsCategory(Base):
    __tablename__ = "news_category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)  # 上传用户，可能需要外键根据需求

    news = relationship("News", back_populates="news")  # 反向关系

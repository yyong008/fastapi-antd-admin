from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from app.db.client import Base


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=True)
    source = Column(String, nullable=True)
    view_count = Column(Integer, default=0, nullable=False)
    published_at = Column(DateTime(timezone=True), nullable=False)
    category_id = Column(Integer, ForeignKey("blog_category.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("blog_tag.id"), nullable=False)
    user_id = Column(Integer, nullable=False)  # 可能需要 ForeignKey 具体看你的需求
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    categories = relationship("BlogCategory", back_populates="blogs")
    tags = relationship("BlogTag", back_populates="blogs")


class BlogCategory(Base):
    __tablename__ = "blog_category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)  # 可能需要 ForeignKey 具体看你的需求
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    blogs = relationship("Blog", back_populates="categories")


class BlogTag(Base):
    __tablename__ = "blog_tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)  # 可能需要 ForeignKey 具体看你的需求

    blogs = relationship("Blog", back_populates="tags")

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.client import Base


class Link(Base):
    __tablename__ = "profile_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False) 
    category_id = Column(
        Integer,
        ForeignKey("profile_link_category.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    category = relationship("LinkCategory", back_populates="links")  # 反向关系


class LinkCategory(Base):
    __tablename__ = "profile_link_category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)  # 上传用户，可能需要外键根据需求
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    links = relationship("Link", back_populates="category")  # 反向关系

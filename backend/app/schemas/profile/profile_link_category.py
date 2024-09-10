from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.client import Base


class LinkCategory(Base):
    __tablename__ = "profile_link_category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, nullable=False)  # 上传用户，可能需要外键根据需求

    links = relationship("Link", back_populates="category")  # 反向关系

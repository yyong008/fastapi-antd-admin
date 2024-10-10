from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.client import Base


class ChangeLog(Base):
    __tablename__ = "change_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)  # 可能需要 ForeignKey，具体看你的需求
    publish_name = Column(String, nullable=False)  # 发布人
    publish_version = Column(String, nullable=False)  # 发布版本
    publish_time = Column(DateTime(timezone=True), nullable=False)  # 发布时间
    type = Column(Integer, nullable=False)  # 1. 大版本更新，2. 功能更新 3. 修复 bug
    content = Column(String, nullable=False)
    url = Column(String, nullable=False)  # 更新地址
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # 数据创建时间
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # 数据更新时间

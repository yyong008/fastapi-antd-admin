from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.client import Base


class FeedBack(Base):
    __tablename__ = "feed_back"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # 可能需要 ForeignKey，具体看你的需求
    content = Column(String, nullable=False)
    url = Column(String, nullable=True)  # 反馈图片地址，可选字段
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # 数据创建时间
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # 数据更新时间

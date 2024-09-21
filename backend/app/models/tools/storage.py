from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.client import Base


class Storage(Base):
    __tablename__ = "tools_storage"

    id = Column(Integer, primary_key=True, autoincrement=True)
    createdAt = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )  # 数据创建时间
    updatedAt = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )  # 数据更新时间
    user_id = Column(Integer, nullable=False)  # 上传用户，可能需要外键根据需求
    name = Column(String, nullable=False)  # 文件名
    file_name = Column(String, nullable=False)  # 真实文件名
    ext_name = Column(String, nullable=False)  # 文件扩展名
    path = Column(String, nullable=False)  # 文件地址
    size = Column(String, nullable=False)  # 文件大小
    type = Column(String, nullable=False)  # 文件类型

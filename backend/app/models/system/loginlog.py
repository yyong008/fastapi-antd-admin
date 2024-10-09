from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.client import Base


class Loginlog(Base):
    __tablename__ = "sys_loginlog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # 登录用户名
    ip = Column(String, nullable=True)  # 登录IP地址
    address = Column(String, nullable=True)  # 登录地址
    login_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )  # 登录时间
    system = Column(String, nullable=True)  # 操作系统
    browser = Column(String, nullable=True)  # 浏览器信息
    userId = Column(Integer, nullable=False)  # 关联用户，可能需要外键根据需求
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

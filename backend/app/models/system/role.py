from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.client import Base
from .user import user_role_association
from .menu import role_menu_association


class Role(Base):
    __tablename__ = "sys_role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # 角色名称
    value = Column(String, nullable=False)  # 角色值
    description = Column(String, nullable=True)  # 描述
    remark = Column(String, nullable=True)  # 备注
    status = Column(Integer, nullable=True)  # 状态
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )  # 创建时间
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )  # 更新时间
    users = relationship(
        "User", secondary=user_role_association, back_populates="roles"
    )
    menus = relationship(
        "Menu", secondary=role_menu_association, back_populates="roles"
    )

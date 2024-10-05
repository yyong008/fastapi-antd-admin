from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.client import Base

role_menu_association = Table(
    "sys_menu_role",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "role_id",
        Integer,
        ForeignKey("sys_role.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    ),
    Column(
        "menu_id",
        Integer,
        ForeignKey("sys_menu.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    ),
    Column(
        "created_at", DateTime(timezone=True), server_default=func.now(), nullable=False
    ),  # 创建时间
    Column(
        "updated_at", DateTime(timezone=True), onupdate=func.now(), nullable=True
    ),  # 更新时间
)


class Menu(Base):
    __tablename__ = "sys_menu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # 菜单名称
    type = Column(Integer, nullable=False)  # 菜单类型
    description = Column(String, nullable=True)  # 描述
    remark = Column(String, nullable=True)  # 备注
    icon = Column(String, nullable=True)  # 图标
    path = Column(String, nullable=True)  # 路径
    path_file = Column(String, nullable=True)  # 文件路径
    status = Column(Integer, nullable=True)  # 状态
    isShow = Column(Integer, nullable=True)  # 是否显示
    isCache = Column(Integer, nullable=True)  # 是否缓存
    permission = Column(String, nullable=True)  # 权限标识
    isLink = Column(Integer, nullable=True)  # 是否外链
    order_no = Column(Integer, nullable=True)  # 排序号
    createdAt = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )  # 创建时间
    updatedAt = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )  # 更新时间

    parent_menu_id = Column(
        Integer,
        ForeignKey("sys_menu.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
    )
    parent_menu = relationship(
        "Menu", remote_side=[id], back_populates="children_menu", cascade="all"
    )

    children_menu = relationship("Menu", back_populates="parent_menu", cascade="all")

    roles = relationship(
        "Role", secondary=role_menu_association, back_populates="menus", cascade="all"
    )

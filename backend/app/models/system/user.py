from sqlalchemy import Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.client import Base

user_role_association = Table(
    "sys_user_role",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "user_id",
        Integer,
        ForeignKey("sys_user.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    ),
    Column(
        "role_id",
        Integer,
        ForeignKey("sys_role.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    ),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)


class User(Base):
    __tablename__ = "sys_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    avatar = Column(String, nullable=True)
    email = Column(String, nullable=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    password = Column(String, nullable=False)
    lang = Column(String, default="en-US", nullable=False)
    theme = Column(String, default="light", nullable=False)
    phone = Column(String, nullable=True)
    remark = Column(String, nullable=True)
    status = Column(Integer, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    department_id = Column(
        Integer,
        ForeignKey("sys_department.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True,
    )
    department = relationship("Department", back_populates="users")
    roles = relationship(
        "Role", secondary=user_role_association, back_populates="users"
    )


class UserSignLog(Base):
    __tablename__ = "user_sign_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)  # 外键关系需要定义 ForeignKey
    sign_type = Column(Integer, nullable=False)
    sign_time = Column(DateTime(timezone=True), default=func.now(), server_default=func.now(), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())


class UserSign(Base):
    __tablename__ = "user_sign"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # 外键关系需要定义 ForeignKey
    resign_nums = Column(Integer, nullable=False)
    signed_nums = Column(Integer, nullable=False)
    continuity_signed_nums = Column(Integer, nullable=False)

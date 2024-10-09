from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.db.client import Base


class Department(Base):
    __tablename__ = "sys_department"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    order_no = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    parent_department_id = Column(
        Integer, ForeignKey("sys_department.id", ondelete="SET NULL"), nullable=True
    )
    parent = relationship("Department", remote_side=[id], back_populates="children")
    children = relationship(
        "Department", back_populates="parent", cascade="all, delete-orphan"
    )
    users = relationship("User", back_populates="department")

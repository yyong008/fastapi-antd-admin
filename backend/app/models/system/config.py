from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db.client import Base


class Config(Base):
    __tablename__ = "sys_config"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, comment="参数名称")
    key = Column(String(255), nullable=False, comment="参数名字")
    value = Column(Text, nullable=False, comment="参数键值")
    description = Column(Text, nullable=True, comment="描述")
    remark = Column(Text, nullable=True, comment="备注")
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), comment="创建时间"
    )
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True, comment="更新时间"
    )

    # Optionally, add a relationship if this table has a relationship with another table.
    # For example:
    # related_entries = relationship("RelatedTable", back_populates="config")

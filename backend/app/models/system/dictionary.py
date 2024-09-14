from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.client import Base


class Dictionary(Base):
    __tablename__ = "sys_dictionary"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    description = Column(String, nullable=True)
    remark = Column(String, nullable=True)
    status = Column(Integer, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())

    entries = relationship(
        "DictionaryEntry", back_populates="dictionary", cascade="all, delete-orphan"
    )


class DictionaryEntry(Base):
    __tablename__ = "sys_dictionary_entry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    order_no = Column(Integer, nullable=True)
    status = Column(Integer, nullable=False)
    remark = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    dictionary_id = Column(
        Integer,
        ForeignKey("sys_dictionary.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    dictionary = relationship("Dictionary", back_populates="entries")

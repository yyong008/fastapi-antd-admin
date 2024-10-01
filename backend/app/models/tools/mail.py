from sqlalchemy import Column, Integer, String

from app.db.client import Base


class Mail(Base):
    __tablename__ = "mail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    title = Column(String, nullable=True)
    host = Column(String, nullable=True)
    port = Column(Integer, nullable=True)
    user = Column(String, nullable=True)
    pass_ = Column("pass", String, nullable=True)
    from_ = Column("from",String, nullable=True)
    to_ = Column("to",String, nullable=True)
    subject = Column(String, nullable=True)
    content = Column(String, nullable=True)
    html = Column(String, nullable=True)
    text = Column(String, nullable=True)

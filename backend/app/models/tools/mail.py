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
    password = Column(
        String, nullable=True
    )  # 用 `password` 代替 `pass`，因为 `pass` 是 Python 的保留字
    from_address = Column(String, nullable=True)  # 用 `from_address` 代替 `from`
    to_address = Column(String, nullable=True)  # 用 `to_address` 代替 `to`
    subject = Column(String, nullable=True)
    content = Column(String, nullable=True)
    html = Column(String, nullable=True)
    text = Column(String, nullable=True)

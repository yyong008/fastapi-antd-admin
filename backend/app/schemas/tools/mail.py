from pydantic import BaseModel, Field
from typing import Optional


class MailBase(BaseModel):
    name: Optional[str] = Field(
        None, title="Name", description="Name associated with the email"
    )
    title: Optional[str] = Field(
        None, title="Title", description="Title or purpose of the email"
    )
    host: Optional[str] = Field(None, title="Host", description="Mail server host")
    port: Optional[int] = Field(None, title="Port", description="Mail server port")
    user: Optional[str] = Field(
        None, title="User", description="Username for mail server"
    )
    password: Optional[str] = Field(
        None, title="Password", description="Password for mail server"
    )
    from_address: Optional[str] = Field(
        None, title="From Address", description="Sender's email address"
    )
    to_address: Optional[str] = Field(
        None, title="To Address", description="Recipient's email address"
    )
    subject: Optional[str] = Field(
        None, title="Subject", description="Subject of the email"
    )
    content: Optional[str] = Field(
        None, title="Content", description="Plain text content of the email"
    )
    html: Optional[str] = Field(
        None, title="HTML", description="HTML content of the email"
    )
    text: Optional[str] = Field(
        None, title="Text", description="Additional text content of the email"
    )


class MailCreate(MailBase):
    pass


class MailUpdate(MailBase):
    pass


class MailInDBBase(MailBase):
    id: int

    class Config:
        from_attributes = True


class Mail(MailInDBBase):
    pass


class MailInDB(MailInDBBase):
    pass

class MailCreateSchema(BaseModel):
    content: str
    host: str
    port: int
    subject: str
    to: str
    user: str
    password: str = Field(..., alias="pass")

class MailUpdateSchema(BaseModel):
    content: str
    host: str
    port: int
    subject: str
    to: str
    user: str
    password: str = Field(..., alias="pass")

class MailDeleteByIdsSchema(BaseModel):
    ids: list[int]

class SendEmailSchema(BaseModel):
    content: str
    host: str
    port: int
    subject: str
    to: str
    user: str
    password: str = Field(..., alias="pass")

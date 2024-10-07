from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.services.tools._format import format_tools_mail
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType # type: ignore
import app.dal.tools.mail as mail_dals
from app.models.tools.mail import Mail
from sqlalchemy.ext.asyncio import AsyncSession 

async def get_mail_list_service(db: AsyncSession, page, pageSize):
    try:
        total = await mail_dals.get_mail_count(db)
        data = await mail_dals.get_mail_list(db, page, pageSize)
        new_data = [format_tools_mail(mail) for mail in data]
        return { "total": total, "list": new_data }
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_mail_by_id_service(db: AsyncSession, id: int):
    try:
        data = await mail_dals.get_mail_by_id(db, id)
        if not data:
            raise HTTPException(status_code=404, detail="Mail not found")
        return format_tools_mail(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_mail_service(db: AsyncSession, mail):
    try:
        mail['from_'] = mail['user']
        mail['to_'] = mail['to']
        mail['pass_'] = mail['password']
        del mail['to']
        del mail['password']
        ml = Mail(**mail)
        ml_in_db = await mail_dals.create_mail_category(db, ml)
        return format_tools_mail(ml_in_db)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_mail_by_id_service(db: AsyncSession, id, mail):
    try:
      ml = await mail_dals.get_mail_by_id(db, id)
      if not ml:
          raise HTTPException(status_code=404, detail="Mail not found")
      for key, value in mail.items():
          if value is not None:
              setattr(ml, key, value)
      new_ml = await mail_dals.update_mail_by_id(db, id, ml)
      return format_tools_mail(new_ml)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_mail_by_ids_service(db: AsyncSession, ids: list[int]):
    try:
        count = await mail_dals.delete_mail_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def send_mail_service(mail, background_tasks):
    conf = ConnectionConfig(
        MAIL_USERNAME=mail['user'],
        MAIL_PASSWORD=mail['password'],
        MAIL_FROM=mail['user'],
        MAIL_PORT=mail['port'],
        MAIL_SERVER=mail['host'],
        MAIL_FROM_NAME=mail['user'],
        MAIL_SSL_TLS=True,
        MAIL_STARTTLS=False,
    )
    message = MessageSchema(
        subject=mail['subject'], recipients=[mail['to']], body=mail['content'],
        subtype=MessageType.html
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return "Email has been sent"

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.services.tools.format import format_tools_mail
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.dal.tools.mail import create_mail_category, get_mail_count, get_mail_list, update_mail_by_id, delete_mail_by_ids, get_mail_by_id
from app.models.tools.mail import Mail

def get_mail_list_service(page, pageSize, db):
    try:
        total = get_mail_count(db)
        data = get_mail_list(db, page, pageSize)
        new_data = []
        for mail in data:
            new_data.append(format_tools_mail(mail))
        return { "total": total, "list": new_data }
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_mail_by_id_service(id, db):
    try:
        data = get_mail_by_id(db, id)
        if not data:
            raise HTTPException(status_code=404, detail="Mail not found")
        return format_tools_mail(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_mail_service(mail, db):
    try:
        mail['from_'] = mail['user']
        mail['to_'] = mail['to']
        mail['pass_'] = mail['password']
        del mail['to']
        del mail['password']
        ml = Mail(**mail)
        ml_in_db = create_mail_category(ml, db)
        return format_tools_mail(ml_in_db)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_mail_by_id_service(id, mail, db):
    try:
      ml = get_mail_by_id(db, id)
      if not ml:
          raise HTTPException(status_code=404, detail="Mail not found")
      for key, value in mail.items():
          if value is not None:
              setattr(ml, key, value)
      new_ml = update_mail_by_id(db, id, ml)
      return format_tools_mail(new_ml)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_mail_by_ids_service(ids, db):
    try:
        count = delete_mail_by_ids(ids, db)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def send_mail_service(mail, background_tasks):
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

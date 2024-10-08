from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from app.schemas.response import RM, RMS
import app.services.tools.mail as m_services
import app.schemas.tools.mail as m_schemas
from app.db.client import get_db
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/mail", tags=["Mail"])


@router.get("/", response_model=RM)
async def get_mail(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_READ)),
):
    data = await m_services.get_mail_list_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_mail_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_READ)),
):
    data = await m_services.get_mail_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_mail(
    mail: m_schemas.MailCreateSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_CREATE)),
):
    mail = mail.model_dump()
    data = await m_services.create_mail_service(db, mail)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_mail_by_id(
    id: int,
    mail: m_schemas.MailUpdateSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_UPDATE)),
):
    mail = mail.model_dump()
    data = await m_services.update_mail_by_id_service(db, id, mail)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_mail(
    ids: m_schemas.MailDeleteByIdsSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_DELETE)),
):
    data = await m_services.delete_mail_by_ids_service(db, ids.ids)
    return RMS(data=data)


@router.post("/send", response_model=RM)
async def send_mail(
    mail: m_schemas.SendEmailSchema,
    background_tasks: BackgroundTasks,
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_SEND)),
):
    mail = mail.model_dump()
    data = await m_services.send_mail_service(mail, background_tasks)
    return RMS(data=data)

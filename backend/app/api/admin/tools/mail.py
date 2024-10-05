from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.tools.mail import (
    delete_mail_by_ids_service,
    get_mail_list_service,
    get_mail_by_id_service,
    create_mail_service,
    send_mail_service,
    update_mail_by_id_service,
)
from app.schemas.tools.mail import (
    MailCreateSchema,
    MailDeleteByIdsSchema,
    MailUpdateSchema,
    SendEmailSchema,
)
from app.db.client import get_db
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/mail", tags=["Mail"])


@router.get("/", response_model=ResponseModel)
def get_mail(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_READ)),
):
    data = get_mail_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_mail_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_READ)),
):
    data = get_mail_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_mail(
    mail: MailCreateSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_CREATE)),
):
    mail = mail.model_dump()
    data = create_mail_service(mail, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_mail_by_id(
    id: int,
    mail: MailUpdateSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_UPDATE)),
):
    mail = mail.model_dump()
    data = update_mail_by_id_service(id, mail, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_mail(
    ids: MailDeleteByIdsSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_DELETE)),
):
    ids = ids.model_dump()
    data = delete_mail_by_ids_service(ids["ids"], db)
    return ResponseSuccessModel(data=data)


@router.post("/send", response_model=ResponseModel)
def send_mail(
    mail: SendEmailSchema,
    background_tasks: BackgroundTasks,
    _: bool = Depends(get_user_permissions(permissions.TOOLS_EMAIL_SEND)),
):
    mail = mail.model_dump()
    data = send_mail_service(mail, background_tasks)
    return ResponseSuccessModel(data=data)

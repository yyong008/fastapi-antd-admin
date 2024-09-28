from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.tools.mail import (
    delete_mail_by_ids_service,
    get_mail_list_service,
    get_mail_by_id_service,
    create_mail_service,
    update_mail_by_id_service,
)

router = APIRouter(prefix="/mail", tags=["Mail"])
router = APIRouter(prefix="/mail", tags=["Mail"])
router = APIRouter(prefix="/mail", tags=["Mail"])


@router.get("/", response_model=ResponseModel)
def get_mail(page: int, pageSize: int, db: Session = Depends(get_mail_list_service)):
    data = get_mail_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_mail_by_id(id: int, db: Session = Depends(get_mail_list_service)):
    data = get_mail_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_mail(mail, db: Session = Depends(create_mail_service)):
    data = create_mail_service(mail, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_mail_by_id(id: int, mail, db: Session = Depends(update_mail_by_id_service)):
    data = update_mail_by_id_service(id, mail, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_mail(ids: list[int], db: Session = Depends(get_mail_list_service)):
    data = delete_mail_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)

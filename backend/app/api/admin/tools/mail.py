from fastapi import APIRouter

from app.schemas.response import ResponseModel, ResponseSuccessModel

router = APIRouter(prefix="/mail", tags=["Mail"])


@router.get("/", response_model=ResponseModel)
def get_mail():
    data = {}
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_mail_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_mail():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_mail_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_mail():
    data = {}
    return ResponseSuccessModel(data=data)

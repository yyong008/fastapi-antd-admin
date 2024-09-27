from fastapi import APIRouter

from app.schemas.response import ResponseModel, ResponseSuccessModel

router = APIRouter(prefix="/config", tags=["Admin System Config"])


@router.get("/", response_model=ResponseModel)
def get_config_list():
    data = {}
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_config_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_config():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_config_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_config():
    data = {}
    return ResponseSuccessModel(data=data)

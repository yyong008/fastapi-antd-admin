import shutil
import os
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.tools.storage import (
    get_tools_storage_list_service,
    get_tools_storage_by_id_service,
    create_tools_storage_service,
    update_tools_storage_by_id_service,
    delete_tools_storage_by_ids_service,
)
from app.constant import STORAGE_MAX_SIZE, STORAGE_ALLOWED_EXTENSIONS
from app.utils.current_user import get_current_user

UPLOAD_DIRECTORY = os.path.join("static", "upload", "storage")
UPLOAD_URL = "/static/upload/storage"
router = APIRouter(prefix="/storage", tags=["Storage"])


def allowed_file(filename: str) -> bool:
    """检查文件类型是否被允许"""
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in STORAGE_ALLOWED_EXTENSIONS
    )


@router.post("/upload")
async def storage_upload(
    file: UploadFile,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail=f"File '{file.filename}' type not allowed. Only images are allowed.",
        )
        # 检查文件大小
    if file.size > STORAGE_MAX_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File '{file.filename}' size exceeds the limit of 5MB.",
        )
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    file_info = {
        "user_id": current_user.id,
        "name": file.filename,
        "file_name": file.filename,
        "ext_name": file.filename.split(".")[-1],
        "path": UPLOAD_URL + "/" + file.filename,
        "size": file.size,
        "type": file.content_type,
    }
    await create_tools_storage_service(file_info, db)
    return ResponseSuccessModel(
        data={
            "filename": file.filename,
        }
    )


@router.get("/", response_model=ResponseModel)
def get_storage_list(
    page: int = Query(1, description="当前页码"),
    pageSize: int = Query(10, description="每页条数"),
    db: Session = Depends(get_db),
):
    data = get_tools_storage_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_storage_by_id(id: int, db: Session = Depends(get_db)):
    data = get_tools_storage_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_storage(storage: dict, db: Session = Depends(get_db)):
    data = create_tools_storage_service(storage, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_storage_by_id(id: int, storage: dict, db: Session = Depends(get_db)):
    data = update_tools_storage_by_id_service(id, storage, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_storage(ids: list[int], db: Session = Depends(get_db)):
    data = delete_tools_storage_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)

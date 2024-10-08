import shutil
import os
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.db.client import get_db
from app.schemas.response import RM, RMS
from app.services.tools.storage import (
    get_tools_storage_list_service,
    get_tools_storage_by_id_service,
    create_tools_storage_service,
    update_tools_storage_by_id_service,
    delete_tools_storage_by_ids_service,
)
from app.constant import STORAGE_MAX_SIZE, STORAGE_ALLOWED_EXTENSIONS
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

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
    _: bool = Depends(get_user_permissions(permissions.TOOLS_STORAGE_UPLOAD)),
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
    await create_tools_storage_service(db, file_info)
    return RMS(
        data={
            "filename": file.filename,
        }
    )


@router.get("/", response_model=RM)
async def get_storage_list(
    page: int = Query(1, description="当前页码"),
    pageSize: int = Query(10, description="每页条数"),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_STORAGE_LIST)),
):
    data = await get_tools_storage_list_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_storage_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_STORAGE_READ)),
):
    data = await get_tools_storage_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_storage(
    storage: dict,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOLLS_STORAGE_CREATE)),
):
    data = await create_tools_storage_service(db, storage)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_storage_by_id(
    id: int,
    storage: dict,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_STORAGE_UPLOAD)),
):
    data = await update_tools_storage_by_id_service(db, id, storage)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_storage(
    ids: list[int],
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.TOOLS_STORAGE_DELETE)),
):
    data = await delete_tools_storage_by_ids_service(db, ids)
    return RMS(data=data)

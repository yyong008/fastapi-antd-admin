from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.schemas.response import ResponseSuccessModel,ResponseModel
from app.services.docs.feedback import get_feedback_list_service

router = APIRouter(prefix="/feedback", tags=["Admin Docs Feedback"])


@router.get("/", response_model=ResponseModel)
def docs_feedback(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_feedback_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def post_docs_feedback():
    return {"success": "ok"}


@router.put("/", response_model=ResponseModel)
def put_docs_feedback():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_by_ids_docs_feedback():
    data = {}
    return ResponseSuccessModel(data=data)

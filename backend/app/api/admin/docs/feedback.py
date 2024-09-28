from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.schemas.response import ResponseSuccessModel, ResponseModel
from app.services.docs.feedback import (
    get_feedback_list_service,
    create_feedback_service,
    update_feedback_service,
    delete_feedback_by_ids_service,
)

router = APIRouter(prefix="/feedback", tags=["Admin Docs Feedback"])


@router.get("/", response_model=ResponseModel)
def docs_feedback(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_feedback_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def post_docs_feedback(feedback: dict, db: Session = Depends(get_db)):
    data = create_feedback_service(feedback, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_docs_feedback(id: int, feedback: dict, db: Session = Depends(get_db)):
    data = update_feedback_service(id, feedback, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_by_ids_docs_feedback(ids: list[int], db: Session = Depends(get_db)):
    data = delete_feedback_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)

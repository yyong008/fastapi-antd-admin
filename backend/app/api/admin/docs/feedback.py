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
from app.schemas.docs.feedback import FeedBack, FeedBackDeleteByIds
from app.utils.current_user import get_current_user

router = APIRouter(prefix="/feedback", tags=["Admin Docs Feedback"])


@router.get("/", response_model=ResponseModel)
def docs_feedback(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_feedback_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def post_docs_feedback(
    feedback: FeedBack,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    feedback = feedback.model_dump()
    data = create_feedback_service(feedback, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_docs_feedback(id: int, feedback: FeedBack, db: Session = Depends(get_db)):
    feedback = feedback.model_dump()
    data = update_feedback_service(id, feedback, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_by_ids_docs_feedback(ids: FeedBackDeleteByIds, db: Session = Depends(get_db)):
    data = delete_feedback_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)

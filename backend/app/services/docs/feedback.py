from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

import app.dal.docs.feedback as fb_dals
from app.services.docs._format import format_feedback
from app.models.docs.feedback import FeedBack


async def get_feedback_list_service(db: AsyncSession, page, pageSize):
    """
    获取反馈列表
    """
    try:
        count = await fb_dals.get_feedback_count(db)
        order_by = FeedBack.created_at.desc()
        filter = None
        options = None
        feedbacks = await fb_dals.get_feedback_list(db, order_by, filter, options, page, pageSize)

        feedback_list = [format_feedback(fb) for fb in feedbacks]
        data = {"total": count, "list": feedback_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_feedback_service(db: AsyncSession, feedback, current_user_id):
    """
    创建反馈
    """
    try:
        del feedback['user_id']
        feedback['userId'] = current_user_id
        fb = FeedBack(**feedback)
        data = await fb_dals.create_feedback(db, fb)
        return format_feedback(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_feedback_by_ids_service(db: AsyncSession, ids):
    """
    删除反馈
    """
    try:
        data = await delete_feedback_by_ids_service(db, ids)
        return format_feedback(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_feedback_service(db: AsyncSession, id, name, email, content):
    """
    更新反馈
    """
    try:
        o_data = await fb_dals.get_feedback_by_id(db, id)
        if o_data is None:
            raise HTTPException(status_code=400, detail="Feedback not found")
        data = await update_feedback_service(db, id, name, email, content)
        return format_feedback(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

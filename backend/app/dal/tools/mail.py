from fastapi import HTTPException
from app.models.tools.mail import Mail
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_mail_count(db: AsyncSession):
    count = await base_crud.get_count(db, Mail)
    return count


async def get_mail_all(db: AsyncSession):
    order_by = Mail.createdAt.desc()
    data = await base_crud.get_all(db=db, model=Mail, order_by=order_by)
    return data


async def get_mail_by_id(db: AsyncSession, mail_id: int):
    return db.query(Mail).filter(Mail.id == mail_id).first()


async def get_mail_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = None
    options = None
    filter = None
    data = await base_crud.get_list(
        db=db,
        model=Mail,
        order_by=order_by,
        filter=filter,
        options=options,
        page=page,
        pageSize=pageSize,
    )
    return data


async def create_mail_category(db: AsyncSession, mail):
    db.add(mail)
    db.commit()
    db.refresh(mail)
    return mail


async def update_mail_by_id(db: AsyncSession, mail_id: int, mail: Mail):
    db.commit()
    db.refresh(mail)
    return mail


async def delete_mail_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Mail).filter(Mail.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()
        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

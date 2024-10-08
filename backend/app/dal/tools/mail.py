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
    data = await base_crud.get_by_id(db=db, model=Mail, id=mail_id)
    return data


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
    data = await base_crud.create(db=db, model=Mail, obj_in=mail)
    return data


async def update_mail_by_id(db: AsyncSession, mail_id: int, mail: Mail):
    data = await base_crud.update_by_id(db=db, model=Mail, id=mail_id, new_data=mail)
    return data


async def delete_mail_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db=db, model=Mail, ids=ids)
    return data

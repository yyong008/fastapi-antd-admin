from app.models.system.config import Config
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_config_by_name(name: str, db: AsyncSession):
    return db.query(Config).filter(Config.name == name).first()


async def get_configs(db: AsyncSession, skip: int = 0, limit: int = 10):
    return db.query(Config).offset(skip).limit(limit).all()


async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, Config)
    return count


async def get_config_all(db: AsyncSession):
    order_by = Config.createdAt.desc()
    data = await base_crud.get_all(db, Config, order_by=order_by)
    return data


async def get_config_by_id(db: AsyncSession, config_id):
    data = await base_crud.get_by_id(db, Config, config_id)
    return data


async def get_configs_by_ids(db: AsyncSession, ids):
    data = await base_crud.get_by_ids(db, Config, ids)
    return data


async def create_config_category(db: AsyncSession, config):
    data = await base_crud.create(db, config)
    return data


async def update_config_by_id(db: AsyncSession, config_id: int, config: Config):
    data = await base_crud.update_by_id(db, Config, config_id, config)
    return data


async def delete_config_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db, Config, ids)
    return data

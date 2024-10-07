from fastapi import HTTPException
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
    return db.query(Config).filter_by(id=config_id).first()


async def get_configs_by_ids(db: AsyncSession, ids):
    return db.query(Config).filter(Config.id.in_(ids)).all()


async def create_config_category(db: AsyncSession, config):
    db.add(config)
    db.commit()
    db.refresh(config)
    return config


async def update_config_by_id(db: AsyncSession, config_id: int, config: Config):
    db.query(Config).filter(Config.id == config_id).update(config)
    db.commit()
    db.refresh(config)
    return config


async def delete_config_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Config)
            .filter(Config.id.in_(ids))
            .delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

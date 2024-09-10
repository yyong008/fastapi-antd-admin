from sqlalchemy.orm import Session
from app.models.system.config import Config


# =====================================GET===================================================
def get_config_by_name(name: str, db: Session):
    return db.query(Config).filter(Config.name == name).first()


def get_configs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Config).offset(skip).limit(limit).all()


def get_count(db: Session):
    count = db.query(Config).count()
    return count


def get_config_all(db: Session):
    sort_column = Config.createdAt.desc()
    return db.query(Config).order_by(sort_column).all()


def get_config_by_id(config_id, db: Session):
    return db.query(Config).filter_by(id=config_id).first()


def get_configs_by_ids(ids, db: Session):
    return db.query(Config).filter(Config.id.in_(ids)).all()

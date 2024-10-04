from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.system.department import Department


# =====================================GET===================================================
async def get_dept_count(db: Session):
    count = db.query(Department).count()
    return count


async def get_dept_all(db: Session):
    sort_column = Department.createdAt.desc()
    return db.query(Department).order_by(sort_column).all()


async def get_dept_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Department.createdAt.desc()
    return db.query(Department).order_by(sort_column).offset(offset).limit(limit).all()

async def create_dept(dept, db: Session):
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept

async def update_dept_by_id(db: Session, dept_id: int, dept: Department):
    db.query(Department).filter(Department.id == dept_id).update(dept)
    db.commit()
    dept = db.query(Department).filter(Department.id == dept_id).first()
    db.refresh(dept)
    return dept

async def delete_dept_by_ids(ids, db):
    try:
        count = db.query(Department).filter(Department.id.in_(ids)).delete(synchronize_session=False)
        
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


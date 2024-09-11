from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.client import get_db
from app.models.system.department import Department

router = APIRouter(prefix="/dept", tags=["Dept"])


@router.get("/")
def get_dict_dept(db: Session = Depends(get_db)):
    try:
        res = db.query(Department).offset(0).limit(10).all()
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        return {"error": "Database query failed"}

    return {"success": "ok", "data": res}


@router.get("/{id}")
def get_dict_dept_by_id():
    return {"success": "ok"}


@router.post("/")
def create_dict_dept():
    return {"success": "ok"}


@router.put("/{id}")
def update_dict_dept_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_dict_dept():
    return {"success": "ok"}

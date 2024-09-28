from typing import List
from sqlalchemy.orm import Session

def get_serve_list(db: Session):
    pass


def get_serve_by_id(serve_id: int, db):
    pass


def create_serve(user, db: Session):
    pass


def update_serve_by_id(serve_id: int, item, db: Session):
    pass


def delete_serve_by_ids(ids: List[int], db: Session):
     pass


def delete_serve_by_id(serve_id: int, db: Session):
    pass

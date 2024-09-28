from typing import List
from sqlalchemy.orm import Session

def get_user_role_list(page: int, pageSize: int, db: Session):
 pass


def get_user_role_by_id(user_role_id: int, db):
    pass

def create_user_role(user_role, db: Session):
    pass


def update_user_role_by_id(user_role_id: int, item, db: Session):
    pass


def delete_user_role_by_ids(ids: List[int], db: Session):
   pass

from app.dal.sys.user import get_user_by_id


def get_user_info(user_id, db):
  userInfo = get_user_by_id(user_id, db)
  user_info = {
    "id": userInfo.id,
    "name": userInfo.name,
  }
  return {"userInfo": user_info, "menu": []}

from app.dal.signin.signinlog import get_user_today_is_sign_in_by_id
from app.dal.sys.monitor.loginlog import get_loginlog_latest_by_user_id

def format_user_loginlog(log):
    return {
        "id": log.id,
        "address": log.address,
        "ip": log.ip,
        "name": log.name,
        "system": log.system,
        "browser": log.browser,
        "userId": log.userId,
        "loginAt": log.login_at
    }


def get_dashboard_data_service(current_user_id: int, db):
    # get to day is sign in
    info = get_user_today_is_sign_in_by_id(current_user_id, db)
    isSignIn = False
    if info:
        isSignIn = True
    # get last login log
    latest_sign_log = get_loginlog_latest_by_user_id(db, current_user_id)
    log = format_user_loginlog(latest_sign_log)
    return {"isSignIn": isSignIn, "latestLoginLog": log }

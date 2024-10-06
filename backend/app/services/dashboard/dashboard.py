from app.dal.signin.signinlog import get_user_today_is_sign_in_by_id
from app.dal.sys.monitor.loginlog import get_loginlog_latest_by_user_id
from app.services.dashboard.format import format_user_loginlog


def get_dashboard_data_service(current_user_id: int, db):
    info = get_user_today_is_sign_in_by_id(current_user_id, db)
    isSignIn = False
    if info:
        isSignIn = True

    latest_sign_log = get_loginlog_latest_by_user_id(db, current_user_id)
    log = format_user_loginlog(latest_sign_log)
    return {"isSignIn": isSignIn, "latestLoginLog": log }

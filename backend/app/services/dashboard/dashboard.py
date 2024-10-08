from app.dal.signin.signinlog import get_user_today_is_sign_in_by_id
from app.dal.sys.monitor.loginlog import get_loginlog_latest_by_user_id
from app.services.dashboard._format import format_user_loginlog
from sqlalchemy.ext.asyncio import AsyncSession

async def get_dashboard_data_service(db: AsyncSession, current_user_id: int):
    """获取仪表盘数据"""
    info = await get_user_today_is_sign_in_by_id(db, current_user_id)
    is_signin = False
    if info:
        is_signin = True

    latest_sign_log = await get_loginlog_latest_by_user_id(db, current_user_id)
    log = format_user_loginlog(latest_sign_log)
    return {"isSignIn": is_signin, "latestLoginLog": log }

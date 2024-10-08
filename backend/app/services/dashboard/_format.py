def format_user_loginlog(log):
    """格式化用户登录日志"""
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

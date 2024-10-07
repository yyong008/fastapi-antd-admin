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

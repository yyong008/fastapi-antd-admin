def format_signin_log(singin_log):
    """
    格式化签到日志
    """
    return {
        "id": singin_log.id,
        "sign_time": singin_log.sign_time,
    }

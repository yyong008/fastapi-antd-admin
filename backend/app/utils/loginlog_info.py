from fastapi import Request
from datetime import datetime
from app.utils.ip_address import get_ip_address
import user_agents  # type: ignore # https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingImports


def get_user_agent_info(request):
    user_agent_str = request.headers.get("user-agent")
    if not user_agent_str:
        return None

    user_agent = user_agents.parse(user_agent_str)
    return {
        "system": f"{user_agent.os.family} {user_agent.os.version_string}",
        "browser": f"{user_agent.browser.family} {user_agent.browser.version_string}",
    }


def get_loginlog_info(request: Request, name, userId):
    ip = request.client.host
    log = {
        "name": name,  # 需要从数据库或认证系统中获取用户名
        "ip": ip,
        "address": "User's address",  # 通常需要调用第三方 API 根据 IP 获取地址
        "login_at": datetime.now().isoformat(),
        "system": "",
        "browser": "",
        "userId": userId,  # 需要从数据库或认证系统中获取用户ID
    }
    info = get_user_agent_info(request)

    if info:
        log["system"] = info["system"]
        log["browser"] = info["browser"]

    address = get_ip_address(ip)
    if address:
        log["address"] = address
    return log

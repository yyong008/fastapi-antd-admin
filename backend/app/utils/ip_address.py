import requests
import json


def is_lan(ip: str) -> bool:
    # 简单判断是否为内网IP
    return ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.")


def get_ip_address(ip: str) -> str:
    if is_lan(ip):
        return "内网IP"

    try:
        url = f"https://whois.pconline.com.cn/ipJson.jsp?ip={ip}&json=true"
        response = requests.get(url)

        # 强制使用 GBK 编码解码响应内容
        decoded_data = response.content.decode("gbk", errors="ignore")

        # 解析JSON数据
        data = json.loads(decoded_data)
        address = data.get("addr", "").strip().split(" ")[0]
        return address

    except Exception as e:
        print(f"{e}")
        return "第三方接口请求失败"

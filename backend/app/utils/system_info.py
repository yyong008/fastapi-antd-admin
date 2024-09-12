import psutil
import platform
import subprocess

def get_system_info():
    node_version = subprocess.check_output(["node", "-v"],  shell=True).decode().strip()
    npm_version = subprocess.check_output(["npm", "-v"], shell=True).decode().strip()
    python_version = subprocess.check_output(["python", "-V"], shell=True).decode().strip()

    # 获取操作系统信息
    os_info = {
        "platform": platform.system(),
        "arch": platform.machine(),
    }

    # 获取 CPU 信息
    cpu_info = {
        "manufacturer": "Unknown",  # psutil 不提供制造商信息
        "brand": platform.processor(),
        "physicalCores": psutil.cpu_count(logical=False),
        "model": platform.processor(),
        "speed": psutil.cpu_freq().current if psutil.cpu_freq() else "Unknown",
    }

    # 获取内存信息
    mem_info = psutil.virtual_memory()
    mem_info_data = {
        "total": mem_info.total,
        "available": mem_info.available,
    }

    # 获取当前系统负载
    current_load = psutil.cpu_percent(percpu=True)
    load_info = {
        "rawCurrentLoad": psutil.cpu_percent(),
        "rawCurrentLoadIdle": 100 - psutil.cpu_percent(),
        "coresLoad": [
            {"rawLoad": load, "rawLoadIdle": 100 - load} for load in current_load
        ],
    }

    # 获取磁盘信息
    disk_info = {
        "size": 0,
        "available": 0,
        "used": 0,
    }
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info["size"] += usage.total
        disk_info["available"] += usage.free
        disk_info["used"] += usage.used

    # 将所有信息组合到一起
    system_info = {
        "pythonRuntime": {
            "version": python_version,
        },
        "nodeRuntime": {
            "node": node_version,
            "npm": npm_version,
        },
        "osRuntime": os_info,
        "cpuInfo": cpu_info,
        "memInfo": mem_info_data,
        "currentLoadInfo": load_info,
        "diskInfo": disk_info,
    }

    return system_info

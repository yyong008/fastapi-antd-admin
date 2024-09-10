from prometheus_client import Counter, generate_latest, CollectorRegistry

# 创建或使用默认的注册表
registry = CollectorRegistry()

# 定义全局的 Prometheus 计数器
REQUESTS_COUNT = Counter(
    "requests_total_count", "Total number of HTTP requests", registry=registry
)


def get_latest_metrics():
    # 生成当前的指标数据
    return generate_latest(registry)

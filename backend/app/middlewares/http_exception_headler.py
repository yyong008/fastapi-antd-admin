from fastapi.middleware.cors import CORSMiddleware


# 自定义中间件（例如CORS）
def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 可以根据需要进行配置
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

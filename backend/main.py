from app.config.config import get_settings

config = get_settings()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_app:app", host=config.SERVER_HOST, port=int(config.SERVER_PORT), reload=True)

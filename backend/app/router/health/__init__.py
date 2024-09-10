from fastapi import APIRouter

router = APIRouter(tags=["Health Check"])


@router.get("/healthcheck")
async def health_check():
    return {"message": "ok"}

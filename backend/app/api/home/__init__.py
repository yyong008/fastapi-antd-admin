from fastapi import APIRouter

router = APIRouter(tags=["Home"])


@router.get("/")
async def home():
    return {"Hello World"}

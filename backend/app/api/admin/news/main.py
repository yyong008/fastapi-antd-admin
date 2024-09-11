from fastapi import APIRouter

router = APIRouter(tags=["News Main"])


@router.get("/{id}")
def get_news_by_id():
    return {"success": "ok"}


@router.get("/")
def get_newss():
    return {"success": "ok"}


@router.post("/")
def create_news():
    return {"success": "ok"}


@router.put("/{id}")
def update_news():
    return {"success": "ok"}


@router.delete("/")
def delete_news_by_ids():
    return {"success": "ok"}

from fastapi import APIRouter

router = APIRouter(prefix="/category", tags=["News Category"])


@router.get("/")
def get_news_category():
    return {"success": "ok"}


@router.get("/{id}")
def get_news_category_by_id():
    return {"success": "ok"}


@router.post("/")
def create_news_category():
    return {"success": "ok"}


@router.put("/{id}")
def update_news_category_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_news_category():
    return {"success": "ok"}

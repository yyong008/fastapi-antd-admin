from fastapi import APIRouter

router = APIRouter(prefix="/tag", tags=["News Tag"])


@router.get("/")
def get_news_tag():
    return {"success": "ok"}


@router.get("/{id}")
def get_news_tag_by_id():
    return {"success": "ok"}


@router.post("/")
def create_news_tag():
    return {"success": "ok"}


@router.put("/{id}")
def update_news_tag_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_news_tag():
    return {"success": "ok"}

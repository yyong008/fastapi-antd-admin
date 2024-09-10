from fastapi import APIRouter

router = APIRouter(tags=["Admin Blog Main"])


@router.get("/{id}")
def get_blog_by_id():
    return {"success": "ok"}


@router.get("/")
def get_blogs():
    return {"success": "ok"}


@router.post("/")
def create_blog():
    return {"success": "ok"}


@router.put("/{id}")
def update_blog():
    return {"success": "ok"}


@router.delete("/")
def delete_blog_by_ids():
    return {"success": "ok"}

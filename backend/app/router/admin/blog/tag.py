from fastapi import APIRouter

router = APIRouter(prefix="/tag", tags=["Admin Blog Category Tag"])


@router.get("/")
def get_blog_tag():
    return {"success": "ok"}


@router.get("/{id}")
def get_blog_tag_by_id():
    return {"success": "ok"}


@router.post("/")
def create_blog_tag():
    return {"success": "ok"}


@router.put("/{id}")
def update_blog_tag_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_blog_tag():
    return {"success": "ok"}

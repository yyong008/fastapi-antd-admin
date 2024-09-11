from fastapi import APIRouter

router = APIRouter(prefix="/category", tags=["Admin Blog Category"])


@router.get("/")
def get_blog_category():
    return {"success": "ok"}


@router.get("/{id}")
def get_blog_category_by_id():
    return {"success": "ok"}


@router.post("/")
def create_blog_category():
    return {"success": "ok"}


@router.put("/{id}")
def update_blog_category_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_blog_category():
    return {"success": "ok"}

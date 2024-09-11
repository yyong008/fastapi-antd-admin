from fastapi import APIRouter

router = APIRouter(prefix="/link/category", tags=["Link Category"])


@router.get("/")
def get_link_category():
    return {"success": "ok"}


@router.get("/{id}")
def get_link_category_by_id():
    return {"success": "ok"}


@router.post("/")
def create_link_category():
    return {"success": "ok"}


@router.put("/{id}")
def update_link_category_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_link_category():
    return {"success": "ok"}

from fastapi import APIRouter

router = APIRouter(prefix="/link", tags=["Link"])


@router.get("/")
def get_link():
    return {"success": "ok"}


@router.get("/{id}")
def get_link_by_id():
    return {"success": "ok"}


@router.post("/")
def create_link():
    return {"success": "ok"}


@router.put("/{id}")
def update_link_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_link():
    return {"success": "ok"}

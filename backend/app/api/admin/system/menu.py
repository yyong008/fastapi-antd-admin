from fastapi import APIRouter

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("/")
def get_menu():
    return {"success": "ok"}


@router.get("/{id}")
def get_menu_by_id():
    return {"success": "ok"}


@router.post("/")
def create_menu():
    return {"success": "ok"}


@router.put("/{id}")
def update_menu_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_menu():
    return {"success": "ok"}

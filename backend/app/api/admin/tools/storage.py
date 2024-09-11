from fastapi import APIRouter

router = APIRouter(prefix="/storage", tags=["Storage"])


@router.get("/")
def get_storage():
    return {"success": "ok"}


@router.get("/{id}")
def get_storage_by_id():
    return {"success": "ok"}


@router.post("/")
def create_storage():
    return {"success": "ok"}


@router.put("/{id}")
def update_storage_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_storage():
    return {"success": "ok"}

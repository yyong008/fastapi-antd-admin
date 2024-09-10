from fastapi import APIRouter

router = APIRouter(prefix="/account", tags=["Account"])


@router.get("/")
def get_account():
    return {"success": "ok"}


@router.get("/{id}")
def get_account_by_id():
    return {"success": "ok"}


@router.post("/")
def create_account():
    return {"success": "ok"}


@router.put("/{id}")
def update_account_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_account():
    return {"success": "ok"}

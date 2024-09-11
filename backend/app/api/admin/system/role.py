from fastapi import APIRouter

router = APIRouter(prefix="/role", tags=["Role"])


@router.get("/")
def get_role():
    return {"success": "ok"}


@router.get("/{id}")
def get_role_by_id():
    return {"success": "ok"}


@router.post("/")
def create_role():
    return {"success": "ok"}


@router.put("/{id}")
def update_role_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_role():
    return {"success": "ok"}

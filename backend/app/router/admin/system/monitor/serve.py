from fastapi import APIRouter

router = APIRouter(prefix="/serve")


@router.get("/")
def get_serve():
    return {"success": "ok"}


@router.get("/{id}")
def get_serve_by_id():
    return {"success": "ok"}


@router.post("/")
def create_serve():
    return {"success": "ok"}


@router.put("/{id}")
def update_serve_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_serve():
    return {"success": "ok"}

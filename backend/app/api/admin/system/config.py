from fastapi import APIRouter

router = APIRouter(prefix="/config", tags=["Admin System Config"])


@router.get("/")
def get_config_list():
    return {"success": "ok"}


@router.get("/{id}")
def get_config_by_id():
    return {"success": "ok"}


@router.post("/")
def create_config():
    return {"success": "ok"}


@router.put("/{id}")
def update_config_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_config():
    return {"success": "ok"}

from fastapi import APIRouter

router = APIRouter(prefix="/dict", tags=["Dict"])


@router.get("/")
def get_dict():
    return {"success": "ok"}


@router.get("/{id}")
def get_dict_by_id():
    return {"success": "ok"}


@router.post("/")
def create_dict():
    return {"success": "ok"}


@router.put("/{id}")
def update_dict_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_dict():
    return {"success": "ok"}

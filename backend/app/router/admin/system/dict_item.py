from fastapi import APIRouter

router = APIRouter(prefix="/dict-item", tags=["Dict Item"])


@router.get("/")
def get_dict_item():
    return {"success": "ok"}


@router.get("/{id}")
def get_dict_item_by_id():
    return {"success": "ok"}


@router.post("/")
def create_dict_item():
    return {"success": "ok"}


@router.put("/{id}")
def update_dict_item_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_dict_item():
    return {"success": "ok"}

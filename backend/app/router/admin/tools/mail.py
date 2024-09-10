from fastapi import APIRouter

router = APIRouter(prefix="/mail", tags=["Mail"])


@router.get("/")
def get_mail():
    return {"success": "ok"}


@router.get("/{id}")
def get_mail_by_id():
    return {"success": "ok"}


@router.post("/")
def create_mail():
    return {"success": "ok"}


@router.put("/{id}")
def update_mail_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_mail():
    return {"success": "ok"}

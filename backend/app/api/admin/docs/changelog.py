from fastapi import APIRouter

router = APIRouter(prefix="/admin/docs", tags=["Admin Docs ChangeLog"])


@router.get("/change-log")
def docs_change_log():
    return {"success": "ok"}


@router.post("/change-log")
def create_docs_change_log():
    return {"success": "ok"}


@router.put("/change-log")
def update_docs_change_log():
    return {"success": "ok"}


@router.delete("/change-log")
def delete_by_ids_docs_change_log():
    return {"success": "ok"}

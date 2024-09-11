from fastapi import APIRouter

router = APIRouter(prefix="/admin/docs/feedback", tags=["Admin Docs Feedback"])


@router.get("/")
def docs_feedback():
    return {"success": "ok"}


@router.post("/")
def post_docs_feedback():
    return {"success": "ok"}


@router.put("/")
def put_docs_feedback():
    return {"success": "ok"}


@router.delete("/")
def delete_by_ids_docs_feedback():
    return {"success": "ok"}

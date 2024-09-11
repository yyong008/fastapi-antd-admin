from fastapi import UploadFile, APIRouter
from datetime import datetime

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def create_upload_file(file: UploadFile):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    path = f"/static/upload/uploaded_{timestamp}_{file.filename}"

    with open(f".{path}", "wb") as f:
        content = await file.read()
        f.write(content)

    return {"filename": file.filename, "url": path}

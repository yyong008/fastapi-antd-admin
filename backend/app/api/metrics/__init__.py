from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from prometheus_client import CONTENT_TYPE_LATEST

from app.utils.prometheus import get_latest_metrics


router = APIRouter(tags=["Metrics"])


@router.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    return PlainTextResponse(
        get_latest_metrics(), headers={"Content-Type": CONTENT_TYPE_LATEST}
    )

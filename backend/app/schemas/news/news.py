from pydantic import BaseModel
from datetime import datetime

class NewsCreate(BaseModel):
    author: str
    categoryId: int
    content: str
    publishedAt: datetime
    source: str
    title: str

class NewsUpdate(BaseModel):
    author: str
    categoryId: int
    content: str
    publishedAt: datetime
    source: str
    title: str

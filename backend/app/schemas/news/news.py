from pydantic import BaseModel
from datetime import datetime

class NewsCreate(BaseModel):
    author: str
    categoryId: int
    content: str
    published_at: datetime
    source: str
    title: str

class NewsUpdate(BaseModel):
    author: str
    categoryId: int
    content: str
    published_at: datetime
    source: str
    title: str

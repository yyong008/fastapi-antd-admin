from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NewsCreate(BaseModel):
    author: str
    categoryId: int
    content: str
    publishedAt: datetime
    source: str
    title: str

class NewsBase(BaseModel):
    title: str = Field(..., title="Title", description="The title of the news article")
    content: str = Field(
        ..., title="Content", description="The content of the news article"
    )
    author: Optional[str] = Field(
        None, title="Author", description="The author of the news article"
    )
    source: Optional[str] = Field(
        None, title="Source", description="The source of the news article"
    )
    view_count: int = Field(
        0, title="View Count", description="Number of views the article has received"
    )
    published_at: datetime = Field(
        ...,
        title="Published At",
        description="The publication date and time of the article",
    )
    news_id: int = Field(
        ...,
        title="News Category ID",
        description="The ID of the category this news article belongs to",
    )
    user_id: int = Field(
        ...,
        title="User ID",
        description="The ID of the user who uploaded the news article",
    )



class NewsUpdate(NewsBase):
    pass


class NewsInDBBase(NewsBase):
    id: int

    class Config:
        from_attributes = True


class News(NewsInDBBase):
    news: Optional["NewsCategory"] = None  # Forward reference to NewsCategory


class NewsInDB(NewsInDBBase):
    pass
